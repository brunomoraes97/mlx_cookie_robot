(()=>{const e=document.location.hostname.replace(/^w{2,3}\d*\./i,"");let t=0;const s=function e(t){switch(t){case"ants.gouv.fr":return{strict:!0,key:"cookieConsent",value:"true"};case"eqmac.app":return{strict:!1,key:"EQM_PRIVACY_CONSENT_CHOSEN",value:"true"};case"figuya.com":return{strict:!1,key:"cookie-dialog",value:"closed"};case"scoodleplay.be":return{strict:!1,key:"scoodleAllowCookies",value:"true"};case"lifesum.com":return{strict:!1,key:"accepted-cookies",value:"[]"};case"programmitv.it":return{strict:!1,key:"privacy_choices_made",value:"OK"};case"nexus.gg":return{strict:!0,key:"cookie-notice:accepted",value:"true"};case"streamelements.com":return{strict:!0,key:"StreamElements.gdprNoticeAccepted",value:"true"};case"phoenix.de":return{strict:!1,key:"user_anonymous_profile",value:'{"config":{"tracking":false,"userprofile":false,"youtube":false,"twitter":false,"facebook":false,"iframe":false,"video":{"useSubtitles":false,"useAudioDescription":false}},"votings":[],"msgflash":[],"history":[]}'};case"klarna.com":return[{strict:!0,key:"safe-storage/v1/tracking-consent/trackingConsentAnalyticsKey",value:"KEEP_ALWAYS;;false"},{strict:!0,key:"safe-storage/v1/tracking-consent/trackingConsentMarketingKey",value:"KEEP_ALWAYS;;false"}];case"volkskrant.nl":case"dg.nl":case"demorgen.be":case"trouw.nl":case"ad.nl":case"parool.nl":case"ed.nl":case"bndestem.nl":case"weser-kurier.de":return[{strict:!1,key:"vl_disable_tracking",value:"true"},{strict:!1,key:"vl_disable_usecookie",value:"necessary"}];case"blaetterkatalog.welt.de":return{strict:!0,key:"DM_prefs",value:'{"cookie_hint":true,"accept_cookies":false,"_childs":[],"_type":1}'};case"yellow.systems":return{strict:!1,key:"isCookiesNotificationHidden",value:!0};case"schlauer-shop24.de":return{strict:!1,key:"Shop4CookieConsentAdv",value:!1};case"gbnews.uk":return{strict:!1,key:"mol.ads.cmp.tcf.cache",value:'{"getTCData":{"cmpId":27,"cmpVersion":3,"gdprApplies":true,"tcfPolicyVersion":2,"eventStatus":"tcloaded","cmpStatus":"loaded","tcString":"CPgwfhMPgwfljAbADCENBwCgAAAAAAAAAAwIAAAQUgFgA4AM-AwQBuIDcwG-AOxAdsA7kB3gEFAAg0CYAKwAXABDADIAGWANkAfgBAACCgEYAKWAU8Aq8BaAFpANYAbwA6oB8gEOgIqAReAkQBNgCdgFIgLkAYEAwkBh4DGAGTgM5AZ4Az4ByQDlAHWAPwEQHwArACGAGQAMsAbIA_ACAAEYAKWAU8Aq4BrADqgHyAQ6Ai8BIgCbAE7AKRAXIAwIBhIDDwGTgM5AZ8A5IBygDrAH4AAA.f_gAAagAAAAA","isServiceSpecific":true,"useNonStandardStacks":false,"purposeOneTreatment":false,"publisherCC":"GB","addtlConsent":"1~","repromptVersion":1,"outOfBand":{"allowedVendors":{},"disclosedVendors":{}},"purpose":{"consents":{},"legitimateInterests":{}},"vendor":{"consents":{},"legitimateInterests":{}},"specialFeatureOptins":{},"publisher":{"consents":{},"customPurpose":{"consents":{},"legitimateInterests":{}},"restrictions":{"3":{}}}},"getStoredRepromptVersion":1,"getValidTCData":{"cmpId":27,"cmpVersion":3,"gdprApplies":true,"tcfPolicyVersion":2,"eventStatus":"tcloaded","cmpStatus":"loaded","listenerId":2,"tcString":"CPgwfhMPgwfljAbADCENBwCgAAAAAAAAAAwIAAAQUgFgA4AM-AwQBuIDcwG-AOxAdsA7kB3gEFAAg0CYAKwAXABDADIAGWANkAfgBAACCgEYAKWAU8Aq8BaAFpANYAbwA6oB8gEOgIqAReAkQBNgCdgFIgLkAYEAwkBh4DGAGTgM5AZ4Az4ByQDlAHWAPwEQHwArACGAGQAMsAbIA_ACAAEYAKWAU8Aq4BrADqgHyAQ6Ai8BIgCbAE7AKRAXIAwIBhIDDwGTgM5AZ8A5IBygDrAH4AAA.f_gAAagAAAAA","isServiceSpecific":true,"useNonStandardStacks":false,"purposeOneTreatment":false,"publisherCC":"GB","addtlConsent":"1~","repromptVersion":1,"outOfBand":{"allowedVendors":{},"disclosedVendors":{}},"purpose":{"consents":{},"legitimateInterests":{}},"vendor":{"consents":{},"legitimateInterests":{}},"specialFeatureOptins":{},"publisher":{"consents":{},"customPurpose":{"consents":{},"legitimateInterests":{}},"restrictions":{"3":{},"4":{}}}}}'};case"palmangels.com":return{strict:!1,key:"SHOW_COOKIE_BANNER",value:"no"};case"parfimo.ro":return[{strict:!1,key:"consent_is_set",value:"true"},{strict:!1,key:"consent_personalization_storage",value:"denied"},{strict:!1,key:"consent_analytics_storage",value:"denied"},{strict:!1,key:"consent_ad_storage",value:"denied"}];case"hardware.info":return{strict:!1,key:"consentData",value:'{"relevantAds":{"version":1,"approved":false},"youtube":{"version":1,"approved":false}}'};case"coquedetelephone.fr":return{strict:!1,key:"mage_consent",value:'{"data":{"functional":true,"marketing":false}}'};case"zugportal.de":return{strict:!1,key:"consent-settings",value:'{"version":1,"permissionStatusEssentials":false,"permissionStatusAnalytics":false,"lastUpdated":"2022-11-01T00:00:00.000Z"}'};case"geotastic.net":return{strict:!1,key:"privacy-policy-accepted",value:"true"};case"bionic-reading.com":return{strict:!1,key:"accept_all_cookies",value:"false"};case"nightcafe.studio":return{strict:!1,key:"acceptsNonCriticalCookies",value:"accepted"};case"defence24.pl":case"cyberdefence24.pl":case"energetyka24.com":case"space24.pl":case"defence24.com":case"infosecurity24.pl":return{strict:!1,key:"privacy2022",value:'{"required":true,"performance":false,"functional":false,"marketing":false,"analytics":false}'};case"modivo.lt":case"modivo.pl":case"modivo.it":case"modivo.ro":case"modivo.sk":case"modivo.hu":case"modivo.bg":case"modivo.gr":case"modivo.de":case"modivo.fr":case"modivo.it":case"modivo.hr":case"modivo.cz":case"modivo.ua":case"modivo.lv":case"modivo.si":case"modivo.at":return[{strict:!1,key:"__MODIVO__hide_modal_consents",value:'{"expires":1875041510390,"data":true}'},{strict:!1,key:"__MODIVO__consents_accepted",value:"true"},{strict:!1,key:"__MODIVO__items_consents_codes",value:'["category_advertisement","category_analysis_and_research","category_location","category_processes","category_service_configuration","Zowie","Synerise","Double Take","Wirtualna Polska Media","Onet","Playlink","INIS sp z o.o.","Tradedoubler","Google Ads","Snowdog","Ringier Axel Springer Polska","Facebook","Verizon Media","Microsoft Corporation","Criteo GmbH","RTB House","TikTok","Hotjar"]'}];case"vicampo.de":return{strict:!1,key:"temp-cookiefirst-consent",value:'{"necessary":false,"performance":false,"functional":false,"advertising":false,"timestamp":0}'};case"data-driven-forms.org":return{strict:!1,key:"data-driven-forms-cookie-consent",value:"neccessary"};case"reservations.hotel-spider.com":return{strict:!1,key:"SB4.Cookies",value:"true"};case"buki.org.pl":return{strict:!1,key:"cookiesInfo",value:"1"}}const s=t.split(".");return s.length>2&&(s.shift(),e(s.join(".")))}(e);s&&((s instanceof Array?s:[s]).forEach((function(e){const s=localStorage.getItem(e.key);(null==s||e.strict&&s!=e.value)&&(localStorage.setItem(e.key,e.value),t++)})),t>0&&document.location.reload())})();