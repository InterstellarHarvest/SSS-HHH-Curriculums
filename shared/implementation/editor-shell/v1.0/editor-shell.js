(() => {
'use strict';
const STATE_KEY='sss-c1-case02-v1-state';
const CONTENT_KEY='sss-c1-case02-v1-content';
const DEFAULT_STATE=Object.freeze({role:'student',marginTop:.5,marginRight:.5,marginBottom:.5,marginLeft:.5,density:'normal',editMode:false,fillMode:true,grayscale:false,guides:false,boundaries:true});
let state={...DEFAULT_STATE};
const body=document.body;
const exportRole=body.dataset.exportRole||'';
const exportGray=body.dataset.exportGrayscale==='true';
const $=(s)=>document.querySelector(s);
const $$=(s)=>Array.from(document.querySelectorAll(s));
function safeJSON(value,fallback){if(value==null||value==='')return fallback;try{const parsed=JSON.parse(value);return parsed==null?fallback:parsed}catch{return fallback}}
function loadState(){const saved=safeJSON(localStorage.getItem(STATE_KEY),{});state={...DEFAULT_STATE,...saved};if(exportRole)state.role=exportRole;if(exportGray)state.grayscale=true;}
function saveState(patch={}){state={...state,...patch};localStorage.setItem(STATE_KEY,JSON.stringify(state));applyState();$('#stateStatus')&&($('#stateStatus').textContent='SAVED LOCALLY');}
function setRole(role){if(exportRole)return;saveState({role});}
function applyState(){
 body.dataset.role=state.role;body.classList.toggle('edit-mode',state.editMode);body.classList.toggle('grayscale',state.grayscale);body.classList.toggle('show-guides',state.guides);body.classList.toggle('hide-boundaries',!state.boundaries);body.classList.remove('density-normal','density-compact','density-spacious');body.classList.add('density-'+state.density);
 const r=document.documentElement.style;r.setProperty('--margin-top',state.marginTop+'in');r.setProperty('--margin-right',state.marginRight+'in');r.setProperty('--margin-bottom',state.marginBottom+'in');r.setProperty('--margin-left',state.marginLeft+'in');
 const controls={roleControl:state.role,marginTop:state.marginTop,marginRight:state.marginRight,marginBottom:state.marginBottom,marginLeft:state.marginLeft,densityControl:state.density};for(const [id,v] of Object.entries(controls)){const el=$('#'+id);if(el)el.value=v;}
 const checks={editControl:state.editMode,fillControl:state.fillMode,grayControl:state.grayscale,guideControl:state.guides,boundaryControl:state.boundaries};for(const [id,v] of Object.entries(checks)){const el=$('#'+id);if(el)el.checked=v;}
 applyEditable();requestAnimationFrame(checkOverflow);
}
function isActiveRole(el){const page=el.closest('.page');return !!page&&(state.role==='all'||page.dataset.role===state.role);}
function applyEditable(){
 $$('[data-editable]').forEach(el=>{const active=isActiveRole(el)&&state.editMode;el.contentEditable=active?'true':'false';el.tabIndex=active?0:-1;});
 $$('[data-response]').forEach(el=>{const page=el.closest('.page');const role=page?page.dataset.role:'';const fillAllowed=state.fillMode&&(role==='student'||role==='accessible');const active=isActiveRole(el)&&(state.editMode||fillAllowed);el.contentEditable=active?'true':'false';el.tabIndex=active?0:-1;});
}
function loadPersistentContent(){const saved=safeJSON(localStorage.getItem(CONTENT_KEY),{});$$('[data-persist-id]').forEach(el=>{const id=el.dataset.persistId;if(Object.prototype.hasOwnProperty.call(saved,id))el.innerHTML=saved[id];});}
function persistElement(el){const saved=safeJSON(localStorage.getItem(CONTENT_KEY),{});saved[el.dataset.persistId]=el.innerHTML;localStorage.setItem(CONTENT_KEY,JSON.stringify(saved));$('#stateStatus')&&($('#stateStatus').textContent='SAVED LOCALLY');}
function clearCurrentRole(force=false){if(state.role==='all'&&!force){alert('Choose one role before clearing responses.');return false;}if(!force&&!confirm('Clear responses for the current role only?'))return false;const roles=state.role==='all'?['student','teacher','answer','accessible']:[state.role];const saved=safeJSON(localStorage.getItem(CONTENT_KEY),{});roles.forEach(role=>{$$('.page[data-role="'+role+'"] [data-response]').forEach(el=>{el.innerHTML='';delete saved[el.dataset.persistId];});});localStorage.setItem(CONTENT_KEY,JSON.stringify(saved));checkOverflow();return true;}
function resetSource(force=false){if(!force&&!confirm('Reset all local edits, responses, and settings to the source validation build?'))return false;localStorage.removeItem(STATE_KEY);localStorage.removeItem(CONTENT_KEY);if(force){state={...DEFAULT_STATE};applyState();$$('[data-response]').forEach(el=>el.innerHTML='');return true;}location.reload();}
function serializePortableHTML(){
 const clone=document.documentElement.cloneNode(true);const live=new Map($$('[data-persist-id]').map(el=>[el.dataset.persistId,el]));clone.querySelectorAll('[data-persist-id]').forEach(el=>{const src=live.get(el.dataset.persistId);if(src)el.innerHTML=src.innerHTML;el.removeAttribute('contenteditable');el.removeAttribute('tabindex');});
 const cb=clone.querySelector('body');cb.dataset.initialState=encodeURIComponent(JSON.stringify(state));cb.classList.remove('edit-mode');clone.querySelectorAll('.page').forEach(p=>p.classList.remove('has-overflow'));return '<!doctype html>\n'+clone.outerHTML;
}
function downloadPortableHTML(){const html=serializePortableHTML();const blob=new Blob([html],{type:'text/html;charset=utf-8'});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download='SSS_C1_CASE02_EDITABLE_MASTER_v1.0_CUSTOM.html';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);}
function checkOverflow(){let count=0;$$('.page').forEach(page=>{if(getComputedStyle(page).display==='none'){page.classList.remove('has-overflow');return;}const frame=page.querySelector('.page-frame');const overflow=frame.scrollHeight>frame.clientHeight+2||frame.scrollWidth>frame.clientWidth+2;page.classList.toggle('has-overflow',overflow);if(overflow)count++;});const out=$('#overflowStatus');if(out){out.textContent=count+' overflow';out.classList.toggle('toolbar-overflow',count>0);}return count;}
function bind(){
 $('#roleControl')?.addEventListener('change',e=>setRole(e.target.value));$('#fillControl')?.addEventListener('change',e=>saveState({fillMode:e.target.checked}));$('#editControl')?.addEventListener('change',e=>saveState({editMode:e.target.checked}));$('#grayControl')?.addEventListener('change',e=>saveState({grayscale:e.target.checked}));$('#guideControl')?.addEventListener('change',e=>saveState({guides:e.target.checked}));$('#boundaryControl')?.addEventListener('change',e=>saveState({boundaries:e.target.checked}));$('#densityControl')?.addEventListener('change',e=>saveState({density:e.target.value}));
 for(const side of ['Top','Right','Bottom','Left'])$('#margin'+side)?.addEventListener('change',e=>saveState({['margin'+side]:Math.max(.25,Math.min(1,Number(e.target.value)||.5))}));
 $('#marginReset')?.addEventListener('click',()=>saveState({marginTop:.5,marginRight:.5,marginBottom:.5,marginLeft:.5}));$('#printButton')?.addEventListener('click',()=>{checkOverflow();window.print();});$('#downloadButton')?.addEventListener('click',downloadPortableHTML);$('#clearButton')?.addEventListener('click',()=>clearCurrentRole(false));$('#resetButton')?.addEventListener('click',()=>resetSource(false));
 document.addEventListener('input',e=>{const el=e.target.closest('[data-persist-id]');if(el)persistElement(el);});window.addEventListener('resize',checkOverflow);window.addEventListener('beforeprint',checkOverflow);
}
function loadInitialPortableState(){const raw=body.dataset.initialState;if(raw){const initial=safeJSON(decodeURIComponent(raw),null);if(initial)state={...DEFAULT_STATE,...initial};}}
loadState();loadInitialPortableState();loadPersistentContent();bind();applyState();
window.__case02={getState:()=>({...state}),saveState,setRole,applyState,applyEditable,clearCurrentRole,resetSource,serializePortableHTML,downloadPortableHTML,checkOverflow,keys:{STATE_KEY,CONTENT_KEY}};
})();
