(()=>{const e=function e(t){if("pepephone.com"===t)return{strict:!0,key:"cookiesChosen",value:"done"};const o=t.split(".");return o.length>2&&(o.shift(),e(o.join(".")))}(document.location.hostname.replace(/^w{2,3}\d*\./i,""));if(e){const t=sessionStorage.getItem(e.key);(null==t||e.strict&&t!=e.value)&&(sessionStorage.setItem(e.key,e.value),document.location.reload())}})();