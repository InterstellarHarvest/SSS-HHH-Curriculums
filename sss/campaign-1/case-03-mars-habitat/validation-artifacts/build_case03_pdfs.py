#!/usr/bin/env python3
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Flowable, ListFlowable, ListItem
)
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

BASE = Path(__file__).resolve().parents[1]
PUB = BASE / 'published'
PUB.mkdir(parents=True, exist_ok=True)

INK = colors.HexColor('#18212b')
MUTED = colors.HexColor('#4b5967')
RULE = colors.HexColor('#8c9aa8')
PANEL = colors.HexColor('#edf1f4')
WASH = colors.HexColor('#f7f9fa')
PRIMARY = colors.HexColor('#0b6f82')
SECONDARY = colors.HexColor('#147a45')
CAUTION = colors.HexColor('#6b5922')
WHITE = colors.white

PAGE_W, PAGE_H = letter
LEFT = RIGHT = 0.5 * inch
TOP_FRAME = PAGE_H - 1.18 * inch
BOTTOM_FRAME = 0.62 * inch
FRAME_H = TOP_FRAME - BOTTOM_FRAME
FRAME_W = PAGE_W - LEFT - RIGHT

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyC3', parent=styles['BodyText'], fontName='Helvetica', fontSize=9.2, leading=11.4, textColor=INK, spaceAfter=4))
styles.add(ParagraphStyle(name='BodySmallC3', parent=styles['BodyText'], fontName='Helvetica', fontSize=8.3, leading=10.1, textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle(name='BodyAccessC3', parent=styles['BodyText'], fontName='Helvetica', fontSize=11.5, leading=14.7, textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name='PageTitleC3', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=14.5, leading=17, textColor=INK, spaceAfter=7, borderColor=PRIMARY, borderWidth=0, borderPadding=0))
styles.add(ParagraphStyle(name='SectionC3', parent=styles['Heading3'], fontName='Helvetica-Bold', fontSize=10.8, leading=13, textColor=PRIMARY, spaceBefore=6, spaceAfter=3))
styles.add(ParagraphStyle(name='TaskC3', parent=styles['Heading3'], fontName='Helvetica-Bold', fontSize=11.2, leading=13.4, textColor=PRIMARY, spaceBefore=5, spaceAfter=3, borderColor=RULE, borderWidth=0, borderPadding=0))
styles.add(ParagraphStyle(name='TaskAccessC3', parent=styles['Heading3'], fontName='Helvetica-Bold', fontSize=13.2, leading=16, textColor=PRIMARY, spaceBefore=7, spaceAfter=4))
styles.add(ParagraphStyle(name='LabelC3', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=7, leading=8.5, textColor=MUTED, spaceAfter=2))
styles.add(ParagraphStyle(name='CaptionC3', parent=styles['BodyText'], fontName='Helvetica', fontSize=7.2, leading=8.7, textColor=MUTED, spaceBefore=3, spaceAfter=4))
styles.add(ParagraphStyle(name='AnswerC3', parent=styles['BodyText'], fontName='Helvetica', fontSize=8.8, leading=11, textColor=INK, leftIndent=7, rightIndent=7, spaceBefore=2, spaceAfter=5, borderColor=SECONDARY, borderWidth=0.8, borderPadding=5, backColor=WASH))
styles.add(ParagraphStyle(name='FootSmallC3', parent=styles['BodyText'], fontName='Helvetica', fontSize=7.5, leading=9.2, textColor=MUTED, spaceAfter=2))


def P(text, style='BodyC3'):
    return Paragraph(text, styles[style])


TASK_LABELS = {
    1: 'REFERENCE',
    2: 'DATA ANALYSIS',
    3: 'DATA ANALYSIS',
    4: 'PATTERN ANALYSIS',
    5: 'DIAGNOSIS',
    6: 'MECHANISM MODEL',
    7: 'EXPLANATION',
    8: 'TRANSFER CHECK',
    9: 'EXIT TICKET',
}


def task(n, title, access=False):
    return P(
        f'<font size="7">{TASK_LABELS[n]}</font><br/><b>{n} · {title}</b>',
        'TaskAccessC3' if access else 'TaskC3'
    )


def bullets(items, access=False, level=0):
    style = styles['BodyAccessC3'] if access else styles['BodyC3']
    return ListFlowable(
        [ListItem(Paragraph(x, style), leftIndent=10) for x in items],
        bulletType='bullet', start='circle', leftIndent=16 + level * 8, bulletFontName='Helvetica', bulletFontSize=6.5,
        spaceBefore=1, spaceAfter=4
    )


class ResponseBox(Flowable):
    def __init__(self, height=45, label=None):
        super().__init__(); self.width = FRAME_W; self.height = height; self.label = label
    def draw(self):
        c = self.canv
        c.setStrokeColor(INK); c.setLineWidth(0.9)
        c.rect(0, 0, self.width, self.height)
        if self.label:
            c.setFillColor(MUTED); c.setFont('Helvetica-Bold', 7)
            c.drawString(5, self.height - 11, self.label.upper())


class IDRow(Flowable):
    def __init__(self): super().__init__(); self.width=FRAME_W; self.height=22
    def draw(self):
        c=self.canv; c.setFillColor(INK); c.setStrokeColor(INK); c.setLineWidth(.6); c.setFont('Helvetica-Bold',8)
        fields=[('Name',0,300),('Date',318,135),('Period',468,64)]
        for label,x,w in fields:
            c.drawString(x,13,label); c.line(x+36,10,x+w,10)


class RuleTitle(Flowable):
    def __init__(self, title, size=10.8, color=PRIMARY):
        super().__init__(); self.title=title; self.size=size; self.color=color; self.width=FRAME_W; self.height=18
    def draw(self):
        c=self.canv; c.setFillColor(self.color); c.setFont('Helvetica-Bold',self.size); c.drawString(0,6,self.title)
        c.setStrokeColor(RULE); c.setLineWidth(.55); c.line(0,2,self.width,2)


class TransmissionChart(Flowable):
    def __init__(self, height=205, compact=False):
        super().__init__(); self.width=FRAME_W; self.height=height; self.compact=compact
    def _pattern_bar(self,c,x,y,w,h,kind,gray):
        c.setFillColor(colors.Color(gray,gray,gray)); c.setStrokeColor(INK); c.setLineWidth(.7); c.rect(x,y,w,h,fill=1,stroke=1)
        c.saveState(); p=c.beginPath(); p.rect(x,y,w,h); c.clipPath(p,stroke=0,fill=0); c.setStrokeColor(MUTED); c.setLineWidth(.55)
        if kind=='diag':
            step=8
            for k in range(-int(h),int(w+h),step): c.line(x+k,y,x+k+h,y+h)
        elif kind=='dots':
            c.setFillColor(MUTED)
            for xx in range(int(x)+4,int(x+w),8):
                for yy in range(int(y)+4,int(y+h),8): c.circle(xx,yy,1.1,fill=1,stroke=0)
        elif kind=='cross':
            step=10
            for k in range(-int(h),int(w+h),step):
                c.line(x+k,y,x+k+h,y+h); c.line(x+k,y+h,x+k+h,y)
        else:
            for yy in range(int(y)+5,int(y+h),7): c.line(x,yy,x+w,yy)
        c.restoreState()
    def draw(self):
        c=self.canv; W=self.width; H=self.height
        c.setFillColor(INK); c.setFont('Helvetica-Bold',8.5); c.drawString(0,H-10,'Surface intake to habitat output transmission')
        plot_x=48; plot_y=38; plot_w=W-58; plot_h=H-64
        c.setStrokeColor(RULE); c.setFillColor(MUTED); c.setFont('Helvetica',6.8)
        for val in range(0,101,20):
            yy=plot_y+plot_h*val/100
            c.setStrokeColor(colors.HexColor('#c6cdd1')); c.setLineWidth(.35); c.line(plot_x,yy,plot_x+plot_w,yy)
            c.setFillColor(MUTED); c.drawRightString(plot_x-5,yy-2,str(val))
        c.setStrokeColor(INK); c.setLineWidth(.8); c.line(plot_x,plot_y,plot_x,plot_y+plot_h); c.line(plot_x,plot_y,plot_x+plot_w,plot_y)
        c.saveState(); c.translate(12,plot_y+plot_h/2); c.rotate(90); c.setFont('Helvetica-Bold',7); c.setFillColor(INK); c.drawCentredString(0,0,'Transmission (%)'); c.restoreState()
        vals=[92,88,31,12]; names=['Blue','Green','Red','Deep red']; bands=['400-500 nm','500-600 nm','600-700 nm','700 nm+']; kinds=['diag','dots','cross','solid']; grays=[.91,.82,.67,.54]
        centers=[]; bw=54; gap=(plot_w-4*bw)/5
        for i,(v,n,b,k,g) in enumerate(zip(vals,names,bands,kinds,grays)):
            x=plot_x+gap+(bw+gap)*i; bh=plot_h*v/100; centers.append(x+bw/2)
            self._pattern_bar(c,x,plot_y,bw,bh,k,g)
            c.setFillColor(INK); c.setFont('Helvetica-Bold',7.5); c.drawCentredString(x+bw/2,plot_y+bh+4,f'{v}%')
            c.setFont('Helvetica-Bold',6.8); c.drawCentredString(x+bw/2,22,n)
            c.setFont('Helvetica',6.2); c.drawCentredString(x+bw/2,12,b)
        c.setFont('Helvetica-Bold',7); c.drawCentredString(plot_x+plot_w/2,0,'Wavelength band')


class QuantitySpectrum(Flowable):
    def __init__(self, height=150): super().__init__(); self.width=FRAME_W; self.height=height
    def draw(self):
        c=self.canv; W=self.width; H=self.height
        c.setStrokeColor(RULE); c.setFillColor(WASH); c.rect(0,0,W,H,fill=1,stroke=1)
        c.setFillColor(INK); c.setFont('Helvetica-Bold',8.5); c.drawString(8,H-15,'Quantity check')
        c.setFont('Helvetica-Bold',15); c.setFillColor(PRIMARY); c.drawString(8,H-38,'280')
        c.setFillColor(INK); c.setFont('Helvetica',7.6); c.drawString(52,H-34,'umol m-2 s-1 combined PPFD')
        c.setFont('Helvetica-Bold',7.2); c.drawString(8,H-52,'Runtime status: adequate total photon quantity')
        c.setStrokeColor(RULE); c.line(W*.40,8,W*.40,H-8)
        c.setFillColor(INK); c.setFont('Helvetica-Bold',8.5); c.drawString(W*.43,H-15,'Spectral transmission by band')
        vals=[92,88,31,12]; names=['Blue','Green','Red','Deep red']; patterns=['///','...','xxx','===']
        y=H-36
        for n,v,pat in zip(names,vals,patterns):
            c.setFont('Helvetica-Bold',7); c.drawString(W*.43,y,n)
            x=W*.55; maxw=W*.38; bw=maxw*v/100
            c.setFillColor(PANEL); c.setStrokeColor(INK); c.rect(x,y-1,maxw,9,fill=0,stroke=1)
            c.setFillColor(colors.HexColor('#aeb7bc')); c.rect(x,y-1,bw,9,fill=1,stroke=0)
            c.setFillColor(INK); c.setFont('Helvetica-Bold',6.5); c.drawRightString(x+maxw,y+1,f'{v}%  {pat}')
            y-=22
        c.setFont('Helvetica-Bold',7); c.setFillColor(CAUTION); c.drawString(8,11,'Analytical conclusion: adequate total does not prove an adequate wavelength distribution.')


class MechanismDiagram(Flowable):
    def __init__(self, filled=False, height=112): super().__init__(); self.width=FRAME_W; self.height=height; self.filled=filled
    def draw(self):
        c=self.canv; W=self.width; H=self.height
        labels=(['47-sol filter replacement','BP-4 rejects red/deep red','case-critical red delivery low','new chlorophyll development impaired','pale new growth'] if self.filled else ['47-sol filter replacement','Complete filter problem','Complete spectral result','Complete pigment result','Pale new growth'])
        n=5; aw=16; bw=(W-(n-1)*aw-4)/n; y=18; h=H-34
        for i,label in enumerate(labels):
            x=i*(bw+aw); c.setStrokeColor(INK); c.setFillColor(WASH if i in (1,2,3) else WHITE); c.rect(x,y,bw,h,fill=1,stroke=1)
            c.setFillColor(INK); c.setFont('Helvetica-Bold',6.6)
            words=label.split(); lines=[]; cur=''
            for word in words:
                test=(cur+' '+word).strip()
                if stringWidth(test,'Helvetica-Bold',6.6)<=bw-8: cur=test
                else: lines.append(cur);cur=word
            if cur: lines.append(cur)
            yy=y+h-14
            for line in lines[:5]: c.drawCentredString(x+bw/2,yy,line); yy-=9
            if i<n-1:
                c.setStrokeColor(INK); c.line(x+bw+2,y+h/2,x+bw+aw-2,y+h/2)
                c.line(x+bw+aw-6,y+h/2+3,x+bw+aw-2,y+h/2); c.line(x+bw+aw-6,y+h/2-3,x+bw+aw-2,y+h/2)
        c.setFillColor(MUTED); c.setFont('Helvetica',6.8); c.drawString(0,4,'Case mechanism model. General plant-light responses also involve blue, green, and red wavelengths.')


class EvidenceCards(Flowable):
    def __init__(self, cards, height=120): super().__init__(); self.cards=cards; self.width=FRAME_W; self.height=height
    def draw(self):
        c=self.canv; cols=2; gap=7; cw=(self.width-gap)/2; rows=(len(self.cards)+1)//2; rh=(self.height-(rows-1)*gap)/rows
        for i,(title,text) in enumerate(self.cards):
            col=i%2; row=i//2; x=col*(cw+gap); y=self.height-(row+1)*rh-row*gap
            c.setFillColor(WASH); c.setStrokeColor(RULE); c.rect(x,y,cw,rh,fill=1,stroke=1)
            c.setFillColor(PRIMARY); c.setFont('Helvetica-Bold',7.5); c.drawString(x+6,y+rh-12,title)
            c.setFillColor(INK); c.setFont('Helvetica',7.1)
            words=text.split(); lines=[];cur=''
            for w in words:
                t=(cur+' '+w).strip()
                if stringWidth(t,'Helvetica',7.1)<=cw-12:cur=t
                else:lines.append(cur);cur=w
            if cur:lines.append(cur)
            yy=y+rh-24
            for line in lines[:5]:c.drawString(x+6,yy,line);yy-=9


class C3Doc(BaseDocTemplate):
    def __init__(self, filename, role, total, accessible=False, grayscale=False, **kw):
        self.role=role; self.total=total; self.accessible=accessible; self.grayscale=grayscale
        super().__init__(filename,pagesize=letter,leftMargin=LEFT,rightMargin=RIGHT,topMargin=1.18*inch,bottomMargin=.62*inch,**kw)
        frame=Frame(LEFT,BOTTOM_FRAME,FRAME_W,FRAME_H,id='normal',leftPadding=4,rightPadding=4,topPadding=2,bottomPadding=2)
        self.addPageTemplates(PageTemplate(id='all',frames=frame,onPage=self._decorate))
    def _decorate(self,c,doc):
        p=doc.page; first=(p==1)
        accent=colors.HexColor('#465159') if self.grayscale else PRIMARY
        c.saveState(); c.setStrokeColor(accent); c.setLineWidth(3); c.line(LEFT,PAGE_H-.93*inch,LEFT,PAGE_H-.47*inch)
        c.setFillColor(INK); c.setFont('Helvetica-Bold',22 if first else 13); c.drawString(LEFT+8,PAGE_H-.67*inch,'Mars Habitat')
        c.setFillColor(MUTED); c.setFont('Helvetica',8); sub='Campaign 1 - Case 03 - Arcadia Planitia, Mars' if first else f'{self.role} - Continued'; c.drawString(LEFT+8,PAGE_H-.84*inch,sub)
        c.setFillColor(INK); c.setFont('Helvetica-Bold',7); c.drawRightString(PAGE_W-RIGHT,PAGE_H-.55*inch,'SOLAR'); c.drawRightString(PAGE_W-RIGHT,PAGE_H-.67*inch,'AGRICULTURAL'); c.drawRightString(PAGE_W-RIGHT,PAGE_H-.79*inch,'AGENCY')
        c.setStrokeColor(RULE); c.setLineWidth(.55); c.line(LEFT,PAGE_H-1.0*inch,PAGE_W-RIGHT,PAGE_H-1.0*inch)
        c.line(LEFT,.47*inch,PAGE_W-RIGHT,.47*inch); c.setFillColor(MUTED); c.setFont('Helvetica-Bold',7); c.drawRightString(PAGE_W-RIGHT,.31*inch,f'{self.role} {p} of {self.total}')
        c.restoreState()


def tdata(rows, colwidths, font=8.1, header=True):
    data=[[Paragraph(str(x),styles['BodySmallC3']) for x in row] for row in rows]
    t=Table(data,colWidths=colwidths,repeatRows=1 if header else 0,hAlign='LEFT')
    cmd=[('GRID',(0,0),(-1,-1),.55,RULE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('TEXTCOLOR',(0,0),(-1,-1),INK)]
    if header:cmd += [('BACKGROUND',(0,0),(-1,0),PANEL),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold')]
    t.setStyle(TableStyle(cmd)); return t


def build_doc(path, role, total, pages, accessible=False, grayscale=False):
    story=[]
    for i,flows in enumerate(pages):
        story.extend(flows)
        if i < len(pages)-1: story.append(PageBreak())
    doc=C3Doc(str(path),role,total,accessible=accessible,grayscale=grayscale,pageCompression=0,title=f'Mars Habitat - {role}')
    doc.build(story)
    # Replace ReportLab's four binary marker bytes with same-length ASCII.
    b=path.read_bytes(); b=b.replace(b'%\x93\x8c\x8b\x9e',b'%ASCI'); path.write_bytes(b)


def student_pages(accessible=False):
    body='BodyAccessC3' if accessible else 'BodyC3'; rb=60 if accessible else 42
    pages=[]
    # Page 1
    p=[IDRow(), Spacer(1,3), P('Mission question','SectionC3'), P('<b>How can the habitat receive an adequate total amount of light while potato plants still fail to form normal green new growth?</b>',body),
       EvidenceCards([('CREW','Top-canopy and newest leaves bleach after three weeks; added iron and nitrogen did not help.'),('SENSORS','Combined PPFD is 280 umol m-2 s-1, described as adequate; primary path is a 12 m light pipe plus white LEDs.'),('PLANTS','Older lower leaves retain green; new tissue is pale yellow-white; roots are healthy.'),('LOGS','Spectral analysis was skipped because total PAR was considered sufficient.')],height=138 if not accessible else 166),
       task(1,'Define the measurement',accessible),P('State what the 280 PPFD reading measures and one important feature it cannot show.',body),ResponseBox(64 if accessible else 47),
       task(2,'Read the spectral-transmission data',accessible),P('Read the four exact runtime values. Identify the lowest transmission inside 400-700 nm. Do not invent intermediate measurements.',body),TransmissionChart(235 if accessible else 205),
       P('<b>SOURCE STATUS:</b> Whole-number transmission values are game-provided. The graph does not imply a continuous measured spectrum.','CaptionC3'),ResponseBox(52 if accessible else 35,'Lowest in-PAR transmission and evidence')]
    pages.append(p)
    # Page 2
    p=[task(3,'Compare quantity and quality',accessible),P('Compare the adequate total PPFD reading with the wavelength distribution. Explain why “not enough total light” does not fit the measured quantity.',body),QuantitySpectrum(180 if accessible else 150),ResponseBox(100 if accessible else 68),
       Spacer(1,8),task(4,'Connect the symptom pattern',accessible),P('Use the old-versus-new leaf pattern, healthy roots, and failed nutrient additions. Explain why the evidence points to a problem in forming new chlorophyll.',body),
       tdata([['Observation','What it supports'],['Older leaves retain green','Existing pigment was already present.'],['Newest tissue becomes pale first','New pigment formation is the affected step.'],['Roots are healthy','Root poisoning is not supported.'],['Iron and nitrogen did not help','Simple nutrient shortage is weakened.']],[2.0*inch,5.25*inch]),ResponseBox(136 if accessible else 105)]
    pages.append(p)
    # Page 3
    diagnoses=['Mars soil perchlorates are poisoning the roots.','CO2 concentration is too high.','The Mars sol is disrupting the photoperiod.','The light-delivery system filters red wavelengths needed for chlorophyll biosynthesis.']
    p=[task(5,'Select and reject diagnoses',accessible),P('Mark the diagnosis that fits all evidence. Then reject one tempting alternative with a specific observation or measurement.',body),
       tdata([['Select','Diagnosis']]+[['[ ]',d] for d in diagnoses],[.55*inch,6.7*inch]),Spacer(1,5),ResponseBox(98 if accessible else 88,'Rejected alternative and evidence'),
       Spacer(1,8),task(6,'Model the mechanism',accessible),P('Complete the middle steps. Your chain must connect wavelength-selective transmission to the location of the symptom.',body),MechanismDiagram(False,height=150 if accessible else 118),ResponseBox(105 if accessible else 90,'Mechanism explanation'),
       P('<b>SCIENCE BOUNDARY:</b> This case isolates a red-band rejection. Plants do not use only red light; blue, green, and red wavelengths can all affect plant function.','CaptionC3')]
    pages.append(p)
    # Page 4
    p=[task(7,'Claim-Evidence-Reasoning',accessible),P('Write a concise Claim-Evidence-Reasoning conclusion. Use the 280 PPFD value, at least two spectral values, and the symptom pattern.',body),
       P('<b>Claim</b>',body),ResponseBox(62 if accessible else 42),P('<b>Evidence</b>',body),ResponseBox(105 if accessible else 72),P('<b>Reasoning</b>',body),ResponseBox(132 if accessible else 92),
       task(8,'Transfer the analysis',accessible),P('Explain why making the system brighter without correcting the spectrum might fail. Name the next measurement or engineering check.',body),ResponseBox(90 if accessible else 61),
       task(9,'Exit ticket',accessible),P('In a new controlled-environment lighting failure, what two measurements would you compare first, and why?',body),ResponseBox(90 if accessible else 59)]
    pages.append(p)
    return pages


def accessible_pages():
    # six-page continuous-flow accessible edition, preserving task order.
    pages=[]; body='BodyAccessC3'
    pages.append([IDRow(),P('Mission question','SectionC3'),P('<b>How can the habitat receive an adequate total amount of light while potato plants still fail to form normal green new growth?</b>',body),EvidenceCards([('CREW','New growth bleaches first. Added iron and nitrogen did not help.'),('SENSORS','PPFD is 280 umol m-2 s-1. Light travels through a 12 m pipe plus LEDs.'),('PLANTS','Old leaves retain green. Roots are healthy.'),('LOGS','No spectral test was done before the failure.')],height=180),task(1,'Define the measurement',True),P('Complete both statements.',body),P('<b>PPFD tells us:</b>',body),ResponseBox(90),P('<b>PPFD does not tell us:</b>',body),ResponseBox(90)])
    pages.append([task(2,'Read the spectral-transmission data',True),P('Use only the four values shown. Which band inside 400-700 nm has the lowest transmission?',body),tdata([['Band','Range','Transmission'],['Blue','400-500 nm','92%'],['Green','500-600 nm','88%'],['Red','600-700 nm','31%'],['Deep red','700 nm+','12%']],[1.5*inch,2.2*inch,1.1*inch]),TransmissionChart(250),P('<b>SOURCE STATUS:</b> These four whole-number transmission values are game-provided.','CaptionC3'),ResponseBox(88,'Lowest in-PAR transmission and how you know')])
    pages.append([task(3,'Compare quantity and quality',True),P('The total PPFD is 280 umol m-2 s-1 and the game describes it as adequate. Compare that quantity with the uneven distribution below.',body),QuantitySpectrum(205),P('Why does the explanation “not enough total light” conflict with the sensor reading?',body),ResponseBox(115),P('What is wrong with the delivered light instead?',body),ResponseBox(100)])
    pages.append([task(4,'Connect the symptom pattern',True),P('Old leaves retain green. New leaves become pale first. Roots are healthy. Nutrient additions did not help.',body),tdata([['Observation','Meaning'],['Old tissue remains green','Existing chlorophyll is still present.'],['New tissue bleaches first','New chlorophyll formation is disrupted.'],['Healthy roots','Root poisoning is not supported.']],[2.1*inch,5.15*inch]),ResponseBox(126,'Explain the pattern'),task(5,'Select and reject diagnoses',True),P('Choose the diagnosis that fits all evidence. Then reject one other option.',body),ResponseBox(115)])
    pages.append([task(6,'Model the mechanism',True),P('Complete the causal chain from the light-delivery system to the visible symptom.',body),MechanismDiagram(False,height=170),ResponseBox(125,'Explain the chain in words'),P('<b>SCIENCE BOUNDARY:</b> The case focuses on red-band rejection. Real plants also respond to blue, green, and other red wavelengths.','CaptionC3'),task(7,'Claim-Evidence-Reasoning',True),P('Write the claim and evidence. Reasoning continues on the next page.',body),P('<b>Claim</b>',body),ResponseBox(82),P('<b>Evidence</b>',body),ResponseBox(128)])
    pages.append([P('Reasoning · continued','SectionC3'),P('<b>Reasoning</b>: connect the data to the mechanism and symptom pattern.',body),ResponseBox(180),task(8,'Transfer the analysis',True),P('Why might making every wavelength brighter be the wrong first fix? What should the analyst measure next?',body),ResponseBox(140),task(9,'Exit ticket',True),P('Name the first two lighting measurements you would compare in a new case and explain why both are needed.',body),ResponseBox(135)])
    return pages


ANS={
1:'PPFD tells how many photons in the defined photosynthetic waveband reach each square meter per second. It does not show how those photons are divided among blue, green, and red wavelengths.',
2:'Blue transmission = 92%; green = 88%; red = 31%; deep red = 12%. Red is the lowest-transmission band inside 400-700 nm. Deep red is lower but is listed at 700 nm+.',
3:'The 280 umol m-2 s-1 PPFD is described as adequate, so simple low total light conflicts with the sensor. The distribution is uneven: blue and green transmit 92% and 88%, while red and deep red transmit only 31% and 12%.',
4:'Older leaves already contain chlorophyll, while new leaves must make it. New tissue bleaching first therefore fits a failure in new chlorophyll formation better than root poisoning.',
5:'Select the wavelength-filtering diagnosis. Reject perchlorates because the roots are healthy and the crop uses a prepared nutrient system. CO2 and photoperiod also do not fit the controlled evidence.',
6:'Filter replaced 47 sols ago without a logged part number -> wrong BP-4 BLUE PASS filter -> blue/green remain high while red/deep red fall to 31%/12% transmission -> the game-defined light-dependent chlorophyll step is impaired -> pale or white new growth.',
7:'Claim: Wavelength-selective filtering, not low total light, causes the failure. Evidence: PPFD is adequate at 280; blue/green transmission is 92%/88%; red/deep-red transmission is 31%/12%; the filter was replaced 47 sols ago without a logged part number; new growth bleaches while older leaves retain green. Reasoning: PPFD combines photon quantity across wavelengths, so an adequate total can hide an unbalanced spectrum. The wrong BP-4 filter fits the selective pattern and the game-defined chlorophyll mechanism, matching the tissue pattern.',
8:'Increasing all wavelengths equally may raise PPFD without restoring the missing red proportion. First check the spectral distribution at canopy level, then correct the source or transmission path and remeasure.',
9:'Compare total PPFD with a wavelength-resolved spectral measurement. One measures total photon quantity; the other shows how that quantity is distributed.'}


def answer_pages():
    return [
      [P('Completed exemplar answer key','PageTitleC3'),task(1,'Define the measurement'),P(ANS[1],'AnswerC3'),task(2,'Read the spectral-transmission data'),TransmissionChart(215),P(ANS[2],'AnswerC3')],
      [task(3,'Compare quantity and quality'),QuantitySpectrum(170),P(ANS[3],'AnswerC3'),task(4,'Connect the symptom pattern'),P(ANS[4],'AnswerC3'),EvidenceCards([('OLD LEAVES','Existing chlorophyll remains.'),('NEW LEAVES','New chlorophyll formation is disrupted.'),('ROOTS','Healthy roots weaken poisoning.'),('NUTRIENTS','Added iron and nitrogen did not help.')],height=130)],
      [task(5,'Select and reject diagnoses'),P(ANS[5],'AnswerC3'),task(6,'Model the mechanism'),MechanismDiagram(True,height=150),P(ANS[6],'AnswerC3'),P('<b>Acceptable alternatives:</b> Equivalent wording is acceptable when it preserves selective attenuation, the case-specific POR/chlorophyll step, and new-tissue bleaching. Do not accept “plants only use red light.”','BodySmallC3')],
      [task(7,'Claim-Evidence-Reasoning'),P(ANS[7],'AnswerC3'),task(8,'Transfer the analysis'),P(ANS[8],'AnswerC3'),task(9,'Exit ticket'),P(ANS[9],'AnswerC3'),P('<b>Scoring note:</b> Require accurate game values, a clear quantity-versus-spectrum distinction, a mechanistic link, and evidence-based alternative rejection. Game score and speed are excluded.','BodySmallC3')]
    ]


def teacher_pages():
    pages=[]
    pages.append([P('Teacher quick start','PageTitleC3'),P('<b>Students act as Data Analysts.</b> They compare spectral distribution with an adequate total PPFD reading, reject “not enough total light,” diagnose selective red/deep-red rejection by the collector filter, and write CER.','BodyC3'),
        tdata([['At a glance','Case 03 - Mars Habitat'],['Duration','60 minutes; gameplay target 18-20 minutes'],['Correct diagnosis','Light-delivery filtering removes red wavelengths needed in the game chlorophyll-biosynthesis mechanism.'],['Core evidence','280 PPFD; 12 m silica light pipe; 68% aggregate transmission; filter replaced 47 sols ago; 92%, 88%, 31%, and 12% band transmission; FS-7 required and BP-4 incorrect.'],['Collect','Student Mission or selected Tasks 3, 5, 7, and 9.'],['Fallback','Use the controlled evidence digest; keep all tasks and rubric unchanged.']],[1.45*inch,5.8*inch]),
        P('60-minute timeline','SectionC3'),tdata([['Time','Teacher move','Student action'],['0-5','Launch the adequate-light/yellow-growth contradiction.','Read mission question; predict needed evidence.'],['5-10','Frame quantity versus distribution without revealing diagnosis.','Complete Task 1.'],['10-28','Circulate; redirect to sensors, plants, and archive.','Play and collect targeted evidence.'],['28-38','Check exact values and no invented data.','Complete Tasks 2-4.'],['38-50','Prompt mechanism and alternative rejection.','Complete Tasks 5-7.'],['50-60','Transfer and exit ticket.','Complete Tasks 8-9.']],[.65*inch,3.05*inch,3.55*inch]),
        P('<b>Likely sticking point:</b> “Adequate” describes total photon quantity, not complete spectral adequacy. Ask: Adequate total of what, distributed how?','BodyC3')])
    pages.append([P('Formal lesson plan: outcomes and standards','PageTitleC3'),P('Overview','SectionC3'),P('Students investigate a Mars potato-growth failure by distinguishing a scalar quantity measurement from spectral distribution. They use direct game-provided transmission values, the collector-filter record, tissue pattern, and controlled conditions to reject alternatives and explain the case mechanism.','BodyC3'),P('Measurable learning objectives','SectionC3'),bullets(['Interpret PPFD as photon quantity over a defined waveband rather than a complete spectrum.','Graph and compare wavelength-band transmission without inventing missing measurements.','Use symptom location and timing to infer a failure in new pigment formation.','Reject an alternative that conflicts with adequate total intensity and healthy roots.','Write a concise Claim-Evidence-Reasoning explanation.']),P('Standards alignment','SectionC3'),bullets(['NGSS MS-LS1-6: construct a scientific explanation based on evidence for the role of photosynthesis.','NGSS MS-PS4-2: model reflection, absorption, and transmission of waves through materials.','Practices: analyzing and interpreting data; constructing explanations; argument from evidence.','Crosscutting concepts: cause and effect; systems and system models; energy and matter.']),P('Success criteria','SectionC3'),bullets(['Uses 280 umol m-2 s-1 and all four exact transmission values.','Explains that adequate total photon quantity does not guarantee adequate spectral distribution.','Identifies red at 31% as the lowest-transmission band within 400-700 nm.','Explains why new tissue is affected before older tissue.','Avoids “more brightness always fixes it” and “plants use only red” claims.'])])
    pages.append([P('Formal lesson plan: preparation and procedure','PageTitleC3'),P('Materials and preparation','SectionC3'),bullets(['Game or technical fallback digest; role-appropriate mission packet; pencil.','Open Case 03 and confirm audio/headphone expectations.','Print at 100% / Actual Size. Keep the Answer Key private.','Do not preview the correct diagnosis or describe red light as the only useful wavelength.']),P('Procedure','SectionC3'),tdata([['Phase','Teacher actions','Student evidence product'],['Launch','Present the contradiction: an adequate PPFD reading with bleaching new growth. Ask what one total number cannot reveal.','Task 1: measurement limits.'],['Gameplay','Prompt students to revisit crew, sensors, plants, logs, and deep archive rather than relying on symptoms alone.','Runtime notes and exact values.'],['Data checkpoint','At Task 2, require only the four provided values. At Task 3, require explicit rejection of low total PPFD.','Transmission comparison and quantity-quality explanation.'],['Diagnosis','At Task 5, require one selected and one rejected diagnosis. At Task 6, require a complete causal chain.','Diagnosis and mechanism model.'],['CER/transfer','Require data-specific evidence and a next measurement, not a generic “add brighter lights” fix.','Tasks 7-9.']],[1.0*inch,3.6*inch,2.65*inch]),P('Checks for understanding','SectionC3'),bullets(['Can the student explain why two lights with the same PPFD can have different spectra?','Can the student identify red at 31% as the lowest transmission inside 400-700 nm?','Does the student separate the game mechanism from broader red/blue/green plant responses?'])])
    pages.append([P('Teacher case analysis','PageTitleC3'),P('Story problem','SectionC3'),P('Potato plants grew normally for about three weeks. Then top-canopy and newest leaves became pale yellow to white while older lower leaves retained green. Roots remained healthy, and iron/nitrogen additions did not help.','BodyC3'),P('Evidence channels','SectionC3'),EvidenceCards([('CREW','Top-down progression; nutrient additions failed.'),('SENSORS','12 m light pipes plus white LEDs; 280 PPFD.'),('PLANTS','Healthy roots; pigment failure concentrated in new tissue.'),('LOGS / ARCHIVE','Filter replaced 47 sols ago without a logged part number; FS-7 required and BP-4 incorrect.')],height=145),P('Essential versus supporting evidence','SectionC3'),tdata([['Evidence','Instructional weight'],['280 PPFD described as adequate','Essential: rejects simple low total light.'],['31% red transmission; 12% deep-red transmission','Essential: reveals selective rejection.'],['New tissue bleaches first','Essential: points to new chlorophyll formation.'],['Healthy roots; nutrients failed','Essential for rejecting root/nutrient alternatives.'],['20 C, CO2 1200 ppm, UV index 0.1','Supporting controls; do not overinterpret.']],[3.15*inch,4.1*inch]),TransmissionChart(185),P('<b>SOURCE STATUS:</b> Numerical bars are exact game values; general plant-light principles come from primary research.','CaptionC3')])
    pages.append([P('Mechanism, distractors, and misconceptions','PageTitleC3'),P('Correct case mechanism','SectionC3'),MechanismDiagram(True,height=145),P('Within the game model, the collector/light-pipe system delivers enough total photons for an adequate PPFD value while a likely BP-4 filter disproportionately rejects red/deep-red wavelengths. New tissue must form new chlorophyll; the game links the light-dependent POR step to that process. The pattern therefore appears first in new growth.','BodyC3'),P('Why the wrong answers are tempting','SectionC3'),tdata([['Option','Why tempting','Why it fails'],['Perchlorates poison roots','Mars setting activates prior knowledge.','Roots are healthy; crop uses a prepared nutrient system.'],['CO2 too high','1200 ppm sounds extreme.','Runtime states it is within tolerance and symptoms do not fit.'],['Mars sol disrupts photoperiod','Mars day length is memorable.','Does not explain wavelength data or new-tissue pattern.'],['Not enough total light','Bleaching suggests weak light.','PPFD is 280 and described as adequate.']],[1.55*inch,2.3*inch,3.4*inch]),P('Misconceptions to prevent','SectionC3'),bullets(['PPFD is a complete description of light quality.','A brighter lamp always fixes a lighting failure.','Green photons are useless.','Only red light matters to every plant process.','Yellowing automatically proves nutrient deficiency.'])])
    pages.append([P('Assessment, rubrics, and supports','PageTitleC3'),P('Quick rubric','SectionC3'),tdata([['Dimension','Secure','Developing','Beginning'],['Data use','Uses 280 and all four exact transmission values.','Minor omission or error.','Omits or invents values.'],['Quantity vs spectrum','Clear distinction and rejection.','Partial distinction.','Treats PPFD as a complete spectrum.'],['Mechanism','Complete data-to-symptom chain.','Cause identified; chain incomplete.','Conclusion without mechanism.'],['Alternatives','Rejects with evidence.','Weak rejection.','No evaluation.'],['Communication','Clear CER and vocabulary.','Understandable but incomplete.','Major gaps.']],[1.1*inch,2.1*inch,2.1*inch,1.95*inch]),P('Formal analytic rubric','SectionC3'),bullets(['Accurate game data','Graph interpretation and quantitative comparison','Quantity-versus-distribution distinction','Mechanistic reasoning','Competing-diagnosis evaluation','Source-status and uncertainty awareness','Scientific communication and completion']),P('Differentiation and accessibility','SectionC3'),bullets(['Use the six-page Accessible Mission with larger type and linear tables.','Permit oral dictation, speech-to-text, or typed response.','Read source-status labels aloud.','No arithmetic is required; students compare direct measurements.','Provide the technical fallback without reducing reasoning demand.']),P('Academic grading boundary','SectionC3'),P('Assess evidence, mechanism, reasoning, vocabulary, alternative evaluation, and completion. Do not grade game score, speed, rapport, optional dialogue, or clue-discovery order.','BodyC3')])
    pages.append([P('References and source-status guidance','PageTitleC3'),P('Authoritative and primary sources','SectionC3'),bullets(['Illuminating Engineering Society: PPFD definition as photon quantity per area and time in the 400-700 nm band.','McCree (1971/1972): wavelength-dependent action spectra across 22 crop species with broad blue and red maxima.','Hogewoning et al. (2010): equal irradiance with different blue:red composition produced different plant function.','Heyes, Ruban, and Hunter (2003): POR is a light-driven chlorophyll-biosynthesis enzyme.','Armstrong et al. (1995): light-dependent protochlorophyllide reduction in angiosperm chlorophyll biosynthesis.','Bula et al. (NASA/HortScience, 1991/1994): controlled-environment LED sources provide specified PAR flux and spectral regions.']),P('Game-specific and curriculum-original data','SectionC3'),tdata([['Item','Status'],['280 PPFD; 12 m silica pipe; aggregate transmission 68%','Game-provided Case 03 runtime data.'],['92%, 88%, 31%, 12% transmission','Direct game-provided band readings.'],['47-sol replacement; FS-7 and BP-4 filter models','Game-specific maintenance and hardware records.'],['Mars symptoms and diagnosis','Game-specific controlled case model.'],['Graphs and mechanism diagrams','Curriculum-original vector constructions.']],[4.5*inch,2.75*inch]),P('Rights and precision','SectionC3'),P('No publisher figure is copied or adapted. The graphs use whole-number values and do not interpolate a continuous spectrum or imply greater instrument precision. NASA records are cited for facts; no external imagery is reproduced.','BodyC3')])
    pages.append([P('Technical fallback and release gate','PageTitleC3'),P('Fallback principle','SectionC3'),P('<b>Technical failure must not become academic failure.</b> Give students the same controlled evidence, exact tasks, and rubric. Do not provide the diagnosis.','BodyC3'),P('Controlled evidence digest','SectionC3'),EvidenceCards([('CREW','Three weeks of normal growth; newest leaves become washed out; iron and nitrogen do not help.'),('SENSORS','12 m light pipe plus white LEDs; combined PPFD 280; no spectral analysis had been performed.'),('PLANTS','Healthy roots; older leaves retain green; new growth is pale yellow-white.'),('ARCHIVE','Filter replaced 47 sols ago without a logged part number. Required FS-7; incorrect BP-4 passes blue/green and rejects most red/deep red. Transmission: 92%, 88%, 31%, 12%.')],height=155),P('Facilitation','SectionC3'),bullets(['Read the digest once and allow students to revisit it.','Require Tasks 1-9 unchanged.','Use the same quick or formal rubric.','Allow speech-to-text or oral response as documented accommodations; arithmetic is not required.']),P('Physical-print gate','SectionC3'),P('Automated static, browser, PDF, portability, accessibility, overflow, checksum, and rendered-review checks may pass while the release remains unreleased. Owner physical 100%-scale printing must still verify clipping, line survival, patterns, direct labels, and writing usability before approval.','BodyC3'),P('Owner print checks','SectionC3'),bullets(['Print each role at 100% / Actual Size on ordinary classroom equipment.','Confirm compact page identity and role-specific N of total footers.','Confirm graph axes, units, data labels, and patterns survive black-and-white copying.','Confirm response boxes match expected answer length and bottom reserve remains intentional.','Confirm no production metadata appears on ordinary printable pages.'])])
    return pages


build_doc(PUB/'SSS_C1_CASE03_STUDENT_MISSION_v1.0.pdf','Student Mission',4,student_pages(False),False,False)
build_doc(PUB/'SSS_C1_CASE03_GRAYSCALE_MISSION_v1.0.pdf','Student Mission',4,student_pages(False),False,True)
build_doc(PUB/'SSS_C1_CASE03_ACCESSIBLE_MISSION_v1.0.pdf','Accessible Mission',6,accessible_pages(),True,False)
build_doc(PUB/'SSS_C1_CASE03_ANSWER_KEY_v1.0.pdf','Answer Key',4,answer_pages(),False,False)
build_doc(PUB/'SSS_C1_CASE03_TEACHER_GUIDE_v1.0.pdf','Teacher Guide',8,teacher_pages(),False,False)
print('rebuilt PDFs')
