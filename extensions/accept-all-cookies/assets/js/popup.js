(()=>{const e=document.getElementById("cookie_host_name"),t=document.getElementById("cookie_handler"),o=document.getElementById("cookie_settings_iframe");let n=!1;function a(a){!function(){for(const e of document.querySelectorAll("[data-translate]"))e.textContent=chrome.i18n.getMessage(e.dataset.translate)}(),chrome.tabs.query({active:!0,currentWindow:!0},(function(e){chrome.runtime.sendMessage({command:"isContentExists",tabId:e[0].id},(function(e){}))})),chrome.tabs.query({active:!0,currentWindow:!0},(function(a){chrome.runtime.sendMessage({command:"get_active_tab",tabId:a[0].id},(function(a){n=!!(a=a||{}).tab&&a.tab,a.tab&&a.tab.hostname?(a.tab.whitelisted?t.textContent=chrome.i18n.getMessage("removeFromWhitelist"):t.textContent=chrome.i18n.getMessage("addToWhitelist"),a.tab.whitelisted?$("#cookie_handler").css("background","#489FF8"):$("#cookie_handler").css("color","#66BE99"),e.textContent=a.tab.hostname):(e.textContent=a.tab.url.split("/?")[0],t.textContent=chrome.i18n.getMessage("notWorkingOnThisPage"),$("#cookie_handler").css("background","#95A9B7"),o.style.display="none",$(".cookie_popup_wrapper").css("height","100px"))}))}))}t.addEventListener("click",(function(e){chrome.runtime.sendMessage({command:"toggle_extension",tabId:n.id},(()=>{window.location.reload(),chrome.tabs.query({active:!0,currentWindow:!0},(function(e){chrome.tabs.reload(e[0].id)})),a()}))})),chrome.runtime.onMessage.addListener(((e,t,o)=>{"collapse_popup_on"===e.command&&(document.getElementsByClassName("cookie_popup_wrapper")[0].style.height="250px",a()),"collapse_popup_off"===e.command&&(document.getElementsByClassName("cookie_popup_wrapper")[0].style.height="540px",a())})),a()})();