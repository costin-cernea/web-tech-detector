TECH_RULES = [
    {
        "name": "Google Analytics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"googletagmanager\.com/gtag/js\?id=(?:G|UA)-"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"google-analytics\.com/(?:analytics|ga)\.js"
            },
            {
                "source": "cookies",
                "key": "_ga",
                "pattern": r"^GA1\."
            },
            {
                "source": "cookies",
                "key": "_gid",
                "pattern": r"^GA1\."
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"gtag\(['\"]config['\"],\s*['\"](?:G|UA)-[A-Z0-9-]+['\"]"
            }
        ]
    },
    {
        "name": "Adobe Analytics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"assets\.adobedtm\.com/.*AppMeasurement"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"AppMeasurement(?:\.min)?\.js"
            },
            {
                "source": "cookies",
                "key": "s_cc",
                "pattern": r"^(?:true|false)$"
            },
            {
                "source": "cookies",
                "key": "s_vi",
                "pattern": r"\[CS\]"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:omtrdc\.net|2o7\.net)/b/ss/"
            }
        ]
    },
    {
        "name": "Adobe Experience Platform Web SDK",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn1\.adoberesources\.net/alloy/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn1\.adoberesources\.net/alloy/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"alloy\(['\"]configure['\"]"
            }
        ]
    },
    {
        "name": "Matomo",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:matomo|piwik)\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.matomo\.cloud/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_paq\.push\("
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:matomo|piwik)\.php\?idsite="
            }
        ]
    },
    {
        "name": "Piwik PRO",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"containers\.piwik\.pro/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"piwik\.pro/ppms\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"containers\.piwik\.pro/"
            }
        ]
    },
    {
        "name": "Yandex Metrica",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"mc\.yandex\.ru/metrika/(?:tag|watch)\.js"
            },
            {
                "source": "cookies",
                "key": "_ym_uid",
                "pattern": r"^\d+$"
            },
            {
                "source": "cookies",
                "key": "_ym_d",
                "pattern": r"^\d+$"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"mc\.yandex\.ru/watch/\d+"
            }
        ]
    },
    {
        "name": "Baidu Tongji",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"hm\.baidu\.com/hm\.js"
            },
            {
                "source": "cookies",
                "key": "HMACCOUNT",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"hm\.baidu\.com/hm\.js\?"
            }
        ]
    },
    {
        "name": "Clicky",
        "categories": ["Analytics", "Heatmaps"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.getclicky\.com/(?:js|\d+\.js)"
            },
            {
                "source": "cookies",
                "key": "_jsuid",
                "pattern": r"^\d+$"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"in\.getclicky\.com/\d+ns\.gif"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"clicky_site_ids"
            }
        ]
    },
    {
        "name": "Statcounter",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"statcounter\.com/counter/counter\.js"
            },
            {
                "source": "cookies",
                "key": "sc_is_visitor_unique",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"c\.statcounter\.com/\d+/0/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"var\s+sc_project\s*=\s*\d+"
            }
        ]
    },
    {
        "name": "AT Internet",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"tag\.aticdn\.net/\d+/smarttag\.js"
            },
            {
                "source": "cookies",
                "key": "atuserid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "atidvisitor",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Piano Analytics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"tag\.aticdn\.net/piano-analytics\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.piano\.io/api/tinypass\.min\.js"
            },
            {
                "source": "cookies",
                "key": "_pctx",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_pcid",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Chartbeat",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.chartbeat\.com/js/chartbeat(?:_video)?\.js"
            },
            {
                "source": "cookies",
                "key": "_chartbeat2",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_sf_async_config"
            }
        ]
    },
    {
        "name": "Parse.ly",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.parsely\.com/keys/"
            },
            {
                "source": "meta_tags",
                "key": "parsely-page",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "parsely-title",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "parsely-metadata",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_parsely_visitor",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_parsely_session",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Comscore",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sb\.scorecardresearch\.com/(?:cs/\d+/)?beacon\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"sb\.scorecardresearch\.com/p\?"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_comscore\.push\("
            }
        ]
    },
    {
        "name": "Quantcast Measure",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:secure|edge)\.quantserve\.com/quant\.js"
            },
            {
                "source": "cookies",
                "key": "__qca",
                "pattern": r"^P0-"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"pixel\.quantserve\.com/pixel/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_qevents\.push\("
            }
        ]
    },
    {
        "name": "Nielsen Digital Measurement",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"secure-(?:us|au|uk|dk|it|gl)\.imrworldwide\.com/v60\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn-gl\.imrworldwide\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"imrworldwide\.com/cgi-bin/"
            }
        ]
    },
    {
        "name": "Webtrends",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"s\.webtrends\.com/js/webtrends(?:\.min)?\.js"
            },
            {
                "source": "cookies",
                "key": "WT_FPC",
                "pattern": r"id="
            },
            {
                "source": "meta_tags",
                "key": "WT.ti",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "WT.cg_n",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Mapp Intelligence",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"responder\.wt-safetag\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"webtrekk_v\d+\.min\.js"
            },
            {
                "source": "cookies",
                "key": "wt_rla",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "wt_nbg_Q3",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Etracker",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:code|static)\.etracker\.com/code/e\.js"
            },
            {
                "source": "cookies",
                "key": "_et_coid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "et_allow_cookies",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"etracker\.com/code/e\.js"
            }
        ]
    },
    {
        "name": "Siteimprove Analytics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"siteimproveanalytics\.com/js/siteanalyze_\d+\.js"
            },
            {
                "source": "cookies",
                "key": "nmstat",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "CNZZ",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:s\d+|v1)\.cnzz\.com/z_stat\.php"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cnzz\.com/z_stat\.php\?id="
            }
        ]
    },
    {
        "name": "51.la",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sdk\.51\.la/js-sdk-pro\.min\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.users\.51\.la/\d+\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"sdk\.51\.la/js-sdk-pro\.min\.js"
            }
        ]
    },
    {
        "name": "Cloudflare Web Analytics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.cloudflareinsights\.com/beacon\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-cf-beacon="
            }
        ]
    },
    {
        "name": "Vercel Analytics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/_vercel/insights/script\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"va\.vercel-scripts\.com/v\d+/script"
            }
        ]
    },
    {
        "name": "Jetpack Stats",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"stats\.wp\.com/[es]-\d+\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"stats\.wp\.com/e-\d+\.js"
            }
        ]
    },
    {
        "name": "Shopify Analytics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.shopify\.com/shopifycloud/trekkie/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.shopify\.com/shopifycloud/web-pixels-manager/"
            },
            {
                "source": "cookies",
                "key": "_shopify_y",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_shopify_s",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.ShopifyAnalytics"
            }
        ]
    },
    {
        "name": "Woopra",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.woopra\.com/js/w\.js"
            },
            {
                "source": "cookies",
                "key": "wooTracker",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"woopra\.config\("
            }
        ]
    },
    {
        "name": "GoSquared",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"d1l6p2sc9645hc\.cloudfront\.net/(?:gosquared|tracker)\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_gs\(['\"]GSN-\d+"
            }
        ]
    },
    {
        "name": "Histats",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"s\d+\.histats\.com/js\d+(?:_as)?\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"sstatic1\.histats\.com/0\.gif"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_Hasync\.push\("
            }
        ]
    },
    {
        "name": "LiveInternet",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"counter\.yadro\.ru/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"counter\.yadro\.ru/hit"
            }
        ]
    },
    {
        "name": "Top.Mail.Ru",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"top-fwz1\.mail\.ru/js/code\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"top-fwz1\.mail\.ru/counter\?id="
            }
        ]
    },
    {
        "name": "Naver Analytics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"wcs\.naver\.net/wcslog\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"wcs_add\[['\"]wa['\"]\]"
            }
        ]
    },
    {
        "name": "Gemius",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"\.hit\.gemius\.pl/x?gemius\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"pp_gemius_identifier"
            }
        ]
    },
    {
        "name": "ShinyStat",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"codice(?:isp|pro|business)?\.shinystat\.com/cgi-bin/getcod\.cgi"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"shinystat\.com/cgi-bin/shinystat\.cgi"
            }
        ]
    },
    {
        "name": "Gauges",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"secure\.gaug\.es/track\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"id=['\"]gauges-tracker['\"]"
            }
        ]
    },
    {
        "name": "Open Web Analytics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"owa\.tracker(?:-combined)?-min\.js"
            },
            {
                "source": "cookies",
                "key": "owa_v",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "owa_s",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"owa_cmds\.push\("
            }
        ]
    },
    {
        "name": "Snowplow Analytics",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"d1fc8wv8zag5ca\.cloudfront\.net/[\d.]+/sp\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jsdelivr\.net/npm/@snowplow/browser-tracker"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.snowplow\(['\"]newTracker['\"]"
            }
        ]
    },
    {
        "name": "W3Counter",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"w3counter\.com/tracker\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"w3counter\.com/tracker\.js\?id="
            }
        ]
    },
    {
        "name": "Firebase Analytics",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"gstatic\.com/firebasejs/[\d.]+/firebase-analytics(?:-compat)?\.js"
            }
        ]
    },
    {
        "name": "Mixpanel",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\d*\.mxpnl\.com/libs/mixpanel"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.mixpanel\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"mixpanel\.init\("
            }
        ]
    },
    {
        "name": "Amplitude",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.amplitude\.com/(?:libs/amplitude|script/)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"amplitude\.(?:getInstance\(\)|init)\("
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.amplitude\.com/"
            }
        ]
    },
    {
        "name": "Heap",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.heapanalytics\.com/js/heap-\d+\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"heap\.load\(['\"]\d+['\"]\)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.heapanalytics\.com/js/heap-"
            }
        ]
    },
    {
        "name": "PostHog",
        "categories": ["Analytics", "Product Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:us|eu|app)\.posthog\.com/static/array\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:us-assets|eu-assets)\.i\.posthog\.com/static/array\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"posthog\.init\("
            }
        ]
    },
    {
        "name": "Pendo",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn(?:\.eu)?\.pendo\.io/agent/static/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"pendo\.initialize\("
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn(?:\.eu)?\.pendo\.io/agent/static/"
            }
        ]
    },
    {
        "name": "Segment",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.segment\.(?:com|io)/analytics\.js/"
            },
            {
                "source": "cookies",
                "key": "ajs_anonymous_id",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "ajs_user_id",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.segment\.com/analytics\.js/"
            }
        ]
    },
    {
        "name": "RudderStack",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.rudderlabs\.com/v[\d.]+/(?:rsa|rudder-analytics)\.min\.js"
            },
            {
                "source": "cookies",
                "key": "rl_anonymous_id",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "rl_user_id",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"rudderanalytics\.load\("
            }
        ]
    },
    {
        "name": "mParticle",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"jssdkcdns\.mparticle\.com/js/v\d+/"
            },
            {
                "source": "cookies",
                "key": "mprtcl-v4",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.mParticle"
            }
        ]
    },
    {
        "name": "Kissmetrics",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:i|scripts)\.kissmetrics\.(?:com|io)/"
            },
            {
                "source": "cookies",
                "key": "km_ai",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "km_lv",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_kmq\.push\("
            }
        ]
    },
    {
        "name": "Countly",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jsdelivr\.net/npm/countly-sdk-web"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"countly\.min\.js"
            },
            {
                "source": "cookies",
                "key": "cly_id",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Countly\.(?:init|q\.push)\("
            }
        ]
    },
    {
        "name": "June",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:unpkg\.com|cdn\.jsdelivr\.net/npm)/@june-so/analytics-next"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"@june-so/analytics-next"
            }
        ]
    },
    {
        "name": "Indicative",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.indicative\.com/js/Indicative\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Indicative\.initialize\("
            }
        ]
    },
    {
        "name": "Freshpaint",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"perfalytics\.com/static/js/freshpaint\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"freshpaint\.init\("
            }
        ]
    },
    {
        "name": "Lytics",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"c\.lytics\.io/api/tag/"
            },
            {
                "source": "cookies",
                "key": "seerid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "seerses",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"c\.lytics\.io/api/tag/"
            }
        ]
    },
    {
        "name": "Gainsight PX",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"web-sdk(?:-eu)?\.aptrinsic\.com/api/aptrinsic\.js"
            },
            {
                "source": "cookies",
                "key": "apt.uid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "apt.sid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"aptrinsic\(['\"]init['\"]"
            }
        ]
    },
    {
        "name": "WalkMe",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.walkme\.com/users/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.walkme\.com/users/"
            }
        ]
    },
    {
        "name": "Appcues",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"fast\.appcues\.com/\d+\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Appcues\.identify\("
            }
        ]
    },
    {
        "name": "Userpilot",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.userpilot\.io/sdk/latest\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"userpilot\.identify\("
            }
        ]
    },
    {
        "name": "Chameleon",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"fast\.trychameleon\.com/messo/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"chmln\.init\("
            }
        ]
    },
    {
        "name": "Statsig",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jsdelivr\.net/npm/(?:statsig-js|@statsig/js-client)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"statsig\.initialize\("
            }
        ]
    },
    {
        "name": "Eppo",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jsdelivr\.net/npm/@eppo/js-client-sdk"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"fscdn\.eppo\.cloud/"
            }
        ]
    },
    {
        "name": "Jitsu",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jsdelivr\.net/npm/@jitsu/sdk-js"
            },
            {
                "source": "cookies",
                "key": "__eventn_id",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"jitsu\.track\("
            }
        ]
    },
    {
        "name": "Dreamdata",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.dreamdata\.cloud/scripts/analytics/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.dreamdata\.cloud/scripts/analytics/"
            }
        ]
    },
    {
        "name": "Factors.ai",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"app\.factors\.ai/assets/factors\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"faitracker\.init\("
            }
        ]
    },
    {
        "name": "HockeyStack",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jsdelivr\.net/npm/hockeystack"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.hockeystack\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.hockeystack\.com/"
            }
        ]
    },
    {
        "name": "FoxMetrics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"d35tca7vmefkrc\.cloudfront\.net/scripts/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_fxm\.push\("
            }
        ]
    },
    {
        "name": "Keen IO",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jsdelivr\.net/npm/keen-tracking"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"d26b395fwzu5fz\.cloudfront\.net/keen-tracking"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"new\s+KeenTracking\("
            }
        ]
    },
    {
        "name": "Sensors Data",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.sensorsdata\.cn/sdk/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sensorsdata\.min\.js"
            },
            {
                "source": "cookies",
                "key": "sensorsdata2015jssdkcross",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "GrowingIO",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"assets\.giocdn\.com/(?:vds|gio)\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"assets\.giocdn\.com/"
            }
        ]
    },
    {
        "name": "Hotjar",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.hotjar\.com/c/hotjar-\d+\.js"
            },
            {
                "source": "cookies",
                "key": "_hjid",
                "pattern": r"^[0-9a-f-]{36}$"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\._hjSettings"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"static\.hotjar\.com/c/hotjar-"
            }
        ]
    },
    {
        "name": "Microsoft Clarity",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"clarity\.ms/(?:tag|s)/"
            },
            {
                "source": "cookies",
                "key": "_clck",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_clsk",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"clarity\.ms/tag/"
            }
        ]
    },
    {
        "name": "FullStory",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:edge\.)?fullstory\.com/s/fs\.js"
            },
            {
                "source": "cookies",
                "key": "fs_uid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_fs_uid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\[['\"]_fs_org['\"]\]"
            }
        ]
    },
    {
        "name": "LogRocket",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.(?:lr-ingest\.(?:io|com)|logrocket\.io|lr-in(?:-prod)?\.com)/LogRocket\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"LogRocket\.init\("
            }
        ]
    },
    {
        "name": "Lucky Orange",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"tools\.luckyorange\.com/core/lo\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"d10lpsik1i8c69\.cloudfront\.net/w\.js"
            },
            {
                "source": "cookies",
                "key": "_lo_uid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_lo_v",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"__lo_site_id"
            }
        ]
    },
    {
        "name": "Crazy Egg",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"script\.crazyegg\.com/pages/scripts/"
            },
            {
                "source": "cookies",
                "key": "_ce.s",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"script\.crazyegg\.com/pages/scripts/"
            }
        ]
    },
    {
        "name": "Mouseflow",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.mouseflow\.com/projects/"
            },
            {
                "source": "cookies",
                "key": "mf_user",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\._mfq"
            }
        ]
    },
    {
        "name": "Smartlook",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:web-sdk|rec)\.smartlook\.com/recorder\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"smartlook\(['\"]init['\"]"
            }
        ]
    },
    {
        "name": "Contentsquare",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"t\.contentsquare\.net/uxa/"
            },
            {
                "source": "cookies",
                "key": "_cs_id",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_cs_s",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"t\.contentsquare\.net/uxa/"
            }
        ]
    },
    {
        "name": "Quantum Metric",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.quantummetric\.com/qscripts/quantum-"
            },
            {
                "source": "cookies",
                "key": "QuantumMetricUserID",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "QuantumMetricSessionID",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.quantummetric\.com/qscripts/"
            }
        ]
    },
    {
        "name": "Glassbox",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.gbqofs\.com/"
            },
            {
                "source": "cookies",
                "key": "_cls_v",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_cls_s",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_cls_detector"
            }
        ]
    },
    {
        "name": "Decibel",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.decibelinsight\.net/i/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"decibelInsight\("
            }
        ]
    },
    {
        "name": "SessionCam",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"d2oh4tlt9mrke9\.cloudfront\.net/Record/js/sessioncam\.recorder\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"sessioncam\.recorder\.js"
            }
        ]
    },
    {
        "name": "Inspectlet",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.inspectlet\.com/inspectlet\.js"
            },
            {
                "source": "cookies",
                "key": "__insp_wid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "__insp_uid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"__insp\.push\("
            }
        ]
    },
    {
        "name": "FullSession",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.fullsession\.io/fs\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.fullsession\.io/"
            }
        ]
    },
    {
        "name": "SessionStack",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.sessionstack\.com/sessionstack\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.sessionstack\.com/sessionstack\.js"
            }
        ]
    },
    {
        "name": "OpenReplay",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.openreplay\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"static\.openreplay\.com/"
            }
        ]
    },
    {
        "name": "Highlight.io",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:unpkg\.com|cdn\.jsdelivr\.net/npm)/highlight\.run"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"pub\.highlight\.io"
            }
        ]
    },
    {
        "name": "LiveSession",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.livesession\.io/track\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"__ls\(['\"]init['\"]"
            }
        ]
    },
    {
        "name": "Zoho PageSense",
        "categories": ["Analytics", "Heatmaps", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn(?:-eu)?\.pagesense\.io/js/"
            },
            {
                "source": "cookies",
                "key": "zabUserId",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn(?:-eu)?\.pagesense\.io/js/"
            }
        ]
    },
    {
        "name": "Ptengine",
        "categories": ["Analytics", "Heatmaps"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.ptengine\.(?:com|jp)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\._pt_sp_2"
            }
        ]
    },
    {
        "name": "Plerdy",
        "categories": ["Analytics", "Heatmaps", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"a\.plerdy\.com/public/js/click/main\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"a\.plerdy\.com/public/js/"
            }
        ]
    },
    {
        "name": "VWO",
        "categories": ["Analytics", "Conversion Analytics", "Heatmaps"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"dev\.visualwebsiteoptimizer\.com/(?:j\.php|lib/)"
            },
            {
                "source": "cookies",
                "key": "_vwo_uuid_v2",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_vis_opt_s",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"dev\.visualwebsiteoptimizer\.com/"
            }
        ]
    },
    {
        "name": "Heatmap.com",
        "categories": ["Analytics", "Heatmaps", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:dashboard|cdn)\.heatmap\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"dashboard\.heatmap\.com/f/heatmap\.js"
            }
        ]
    },
    {
        "name": "ReplayBird",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.replaybird\.com/agent/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.replaybird\.com/"
            }
        ]
    },
    {
        "name": "UserReplay",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.userreplay\.net/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.userreplay\.net/"
            }
        ]
    },
    {
        "name": "Noibu",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.noibu\.com/collect\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.noibu\.com/collect\.js"
            }
        ]
    },
    {
        "name": "ClickTale",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdnssl\.clicktale\.net/www"
            },
            {
                "source": "cookies",
                "key": "WRUID",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdnssl\.clicktale\.net/"
            }
        ]
    },
    {
        "name": "Acoustic Tealeaf",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"tealeaf(?:\.min)?\.js"
            },
            {
                "source": "cookies",
                "key": "TLTSID",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "TLTHID",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"TLT\.init\("
            }
        ]
    },
    {
        "name": "Cux.io",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"dc\.cux\.io/analyzer\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"dc\.cux\.io/analyzer\.js"
            }
        ]
    },
    {
        "name": "Browsee",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.browsee\.io/js/browsee\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.browsee\.io/js/browsee\.min\.js"
            }
        ]
    },
    {
        "name": "Capturly",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.capturly\.com/capturly-latest-min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.capturly\.com/"
            }
        ]
    },
    {
        "name": "Howuku",
        "categories": ["Analytics", "Heatmaps", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.howuku\.com/js/track\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.howuku\.com/js/track\.js"
            }
        ]
    },
    {
        "name": "Freshmarketer",
        "categories": ["Analytics", "Heatmaps", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn(?:\.eu)?\.freshmarketer\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn(?:\.eu)?\.freshmarketer\.com/"
            }
        ]
    },
    {
        "name": "UXtweak",
        "categories": ["Analytics", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"s\.uxtweak\.com/uxt\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"s\.uxtweak\.com/uxt\.js"
            }
        ]
    },
    {
        "name": "Maze",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"snippet\.maze\.co/maze-universal-loader\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"snippet\.maze\.co/maze-universal-loader\.js"
            }
        ]
    },
    {
        "name": "Sprig",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.sprig\.com/shim\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.sprig\.com/shim\.js"
            }
        ]
    },
    {
        "name": "Dynatrace RUM",
        "categories": ["Analytics", "Real User Monitoring"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js-cdn\.dynatrace\.com/jstag/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"ruxitagentjs_"
            },
            {
                "source": "cookies",
                "key": "dtCookie",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "rxVisitor",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-oneagent-js-injection",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Datadog RUM",
        "categories": ["Analytics", "Real User Monitoring", "Session Replay"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"datadoghq-browser-agent\.com/.*datadog-rum"
            },
            {
                "source": "cookies",
                "key": "_dd_s",
                "pattern": r"rum="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"DD_RUM\.init\("
            }
        ]
    },
    {
        "name": "New Relic Browser",
        "categories": ["Analytics", "Real User Monitoring"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js-agent\.newrelic\.com/nr-"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"NREUM\.loader_config"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"bam\.nr-data\.net"
            }
        ]
    },
    {
        "name": "SpeedCurve",
        "categories": ["Analytics", "Real User Monitoring"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.speedcurve\.com/js/lux\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.speedcurve\.com/js/lux\.js"
            }
        ]
    },
    {
        "name": "Akamai mPulse",
        "categories": ["Analytics", "Real User Monitoring"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"s\.go-mpulse\.net/boomerang/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"go-mpulse\.net/boomerang/"
            }
        ]
    },
    {
        "name": "Pingdom RUM",
        "categories": ["Analytics", "Real User Monitoring"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"rum-static\.pingdom\.net/pa-"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"rum-static\.pingdom\.net/pa-"
            }
        ]
    },
    {
        "name": "Raygun RUM",
        "categories": ["Analytics", "Real User Monitoring"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.raygun\.io/raygun4js/raygun\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.raygun\.io/raygun4js/"
            }
        ]
    },
    {
        "name": "Plausible Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"plausible\.io/js/(?:script|plausible)(?:\.[a-z-]+)*\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"plausible\.io/js/(?:script|plausible)"
            }
        ]
    },
    {
        "name": "Fathom Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.usefathom\.com/script\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.usefathom\.com/script\.js"
            }
        ]
    },
    {
        "name": "Umami",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:cloud|analytics)\.umami\.is/script\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/umami(?:\.min)?\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-website-id=['\"][0-9a-f-]{36}['\"].*umami"
            }
        ]
    },
    {
        "name": "Simple Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"scripts\.simpleanalyticscdn\.com/(?:latest|auto-events)\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"queue\.simpleanalyticscdn\.com/noscript\.gif"
            }
        ]
    },
    {
        "name": "Pirsch Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"api\.pirsch\.io/(?:pa\.js|pirsch(?:-extended)?\.min\.js)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"api\.pirsch\.io/(?:pa\.js|pirsch)"
            }
        ]
    },
    {
        "name": "GoatCounter",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"gc\.zgo\.at/count\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-goatcounter=['\"]https?://"
            }
        ]
    },
    {
        "name": "Ackee",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"data-ackee-server="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-ackee-domain-id="
            }
        ]
    },
    {
        "name": "Swetrix",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"swetrix\.org/swetrix\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jsdelivr\.net/npm/swetrix"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"swetrix\.init\("
            }
        ]
    },
    {
        "name": "Cabin Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"scripts\.withcabin\.com/hello\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"scripts\.withcabin\.com/hello\.js"
            }
        ]
    },
    {
        "name": "Counter.dev",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.counter\.dev/script\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.counter\.dev/script\.js"
            }
        ]
    },
    {
        "name": "Panelbear",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.panelbear\.com/analytics\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"panelbear\(['\"]config['\"]"
            }
        ]
    },
    {
        "name": "Splitbee",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.splitbee\.io/sb\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.splitbee\.io/sb\.js"
            }
        ]
    },
    {
        "name": "TinyAnalytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"app\.tinyanalytics\.io/pixel/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"app\.tinyanalytics\.io/pixel/"
            }
        ]
    },
    {
        "name": "Microanalytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.microanalytics\.io/js/script\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.microanalytics\.io/js/script\.js"
            }
        ]
    },
    {
        "name": "Independent Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/independent-analytics/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"iawp-tracking"
            }
        ]
    },
    {
        "name": "Koko Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/koko-analytics/assets/dist/js/script\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"koko_analytics"
            }
        ]
    },
    {
        "name": "Burst Statistics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/burst-statistics/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"burst_settings"
            }
        ]
    },
    {
        "name": "WP Statistics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/wp-statistics/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"WP_Statistics_Tracker_Object"
            }
        ]
    },
    {
        "name": "Beam Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"beamanalytics\.b-cdn\.net/beam\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"beamanalytics\.b-cdn\.net/beam\.min\.js"
            }
        ]
    },
    {
        "name": "Ahrefs Web Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"analytics\.ahrefs\.com/analytics\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"analytics\.ahrefs\.com/analytics\.js"
            }
        ]
    },
    {
        "name": "Seline Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.seline\.(?:so|com)/seline\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.seline\.(?:so|com)/seline\.js"
            }
        ]
    },
    {
        "name": "DataFast",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"datafa\.st/js/script\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"datafa\.st/js/script\.js"
            }
        ]
    },
    {
        "name": "Rybbit",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"app\.rybbit\.io/api/script\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"app\.rybbit\.io/api/script\.js"
            }
        ]
    },
    {
        "name": "OpenPanel",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"openpanel\.dev/op1\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"openpanel\.dev/op1\.js"
            }
        ]
    },
    {
        "name": "Sealmetrics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"t\.sealmetrics\.com/t\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"t\.sealmetrics\.com/"
            }
        ]
    },
    {
        "name": "Wide Angle Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"stats\.wideangle\.co/script/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"stats\.wideangle\.co/script/"
            }
        ]
    },
    {
        "name": "Tinybird Web Analytics",
        "categories": ["Analytics", "Privacy Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"unpkg\.com/@tinybirdco/flock\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"@tinybirdco/flock\.js"
            }
        ]
    },
    {
        "name": "Triple Whale",
        "categories": ["Analytics", "Marketing Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.triplewhale\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"api\.config-security\.com/event"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"TriplePixel"
            }
        ]
    },
    {
        "name": "Northbeam",
        "categories": ["Analytics", "Marketing Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"j\.northbeam\.io/ota-sp/"
            },
            {
                "source": "cookies",
                "key": "nb_cid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"j\.northbeam\.io/ota-sp/"
            }
        ]
    },
    {
        "name": "Elevar",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"shopify-gtm-suite\.getelevar\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"ElevarGtmSuite"
            }
        ]
    },
    {
        "name": "Littledata",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.littledata\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"LittledataLayer"
            }
        ]
    },
    {
        "name": "Blotout EdgeTag",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"edgetag\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"edgetag\(['\"]init['\"]"
            }
        ]
    },
    {
        "name": "Polar Analytics",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:cdn|pixel)\.polaranalytics\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"polaranalytics\.com/"
            }
        ]
    },
    {
        "name": "Hyros",
        "categories": ["Analytics", "Marketing Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"t\.hyros\.com/v\d+/lst/universal-script"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"t\.hyros\.com/"
            }
        ]
    },
    {
        "name": "Wicked Reports",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"widget\.wickedreports\.com/v\d+/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"widget\.wickedreports\.com/"
            }
        ]
    },
    {
        "name": "Rockerbox",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"getrockerbox\.com/assets/"
            },
            {
                "source": "cookies",
                "key": "rbuid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"getrockerbox\.com/assets/"
            }
        ]
    },
    {
        "name": "Attribution",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"scripts\.attributionapp\.com/attribution\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"scripts\.attributionapp\.com/attribution\.js"
            }
        ]
    },
    {
        "name": "Cometly",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"t\.cometlytrack\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"t\.cometlytrack\.com/"
            }
        ]
    },
    {
        "name": "SegMetrics",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"tag\.segmetrics\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"tag\.segmetrics\.io/"
            }
        ]
    },
    {
        "name": "AnyTrack",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"assets\.anytrack\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"AnyTrack\("
            }
        ]
    },
    {
        "name": "RedTrack",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "cookies",
                "key": "rtkclickid-store",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"rtkclickid-store"
            }
        ]
    },
    {
        "name": "Converge",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.runconverge\.com/pixels/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"static\.runconverge\.com/pixels/"
            }
        ]
    },
    {
        "name": "Black Crow AI",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"init\.blackcrow\.ai/js/core/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"init\.blackcrow\.ai/js/core/"
            }
        ]
    },
    {
        "name": "Intelligems",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.intelligems\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.intelligems\.io/"
            }
        ]
    },
    {
        "name": "Retention.com",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:cdn|app)\.retention\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"geq\.load\("
            }
        ]
    },
    {
        "name": "Trackify X",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"app\.redretarget\.com/sapp/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"app\.redretarget\.com/sapp/"
            }
        ]
    },
    {
        "name": "Funnelytics",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:cdn|track-v\d+)\.funnelytics\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"funnelytics\.io/track"
            }
        ]
    },
    {
        "name": "Ruler Analytics",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"analytics\.ruleranalytics\.com/lib/"
            },
            {
                "source": "cookies",
                "key": "__raclid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"analytics\.ruleranalytics\.com/"
            }
        ]
    },
    {
        "name": "Klaviyo",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.klaviyo\.com/onsite/js/klaviyo\.js"
            },
            {
                "source": "cookies",
                "key": "__kla_id",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_learnq\.push\("
            }
        ]
    },
    {
        "name": "Meta Pixel",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"connect\.facebook\.net/[a-zA-Z_]+/fbevents\.js"
            },
            {
                "source": "cookies",
                "key": "_fbp",
                "pattern": r"^fb\."
            },
            {
                "source": "cookies",
                "key": "_fbc",
                "pattern": r"^fb\."
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"fbq\(['\"]init['\"],\s*['\"]\d+['\"]"
            }
        ]
    },
    {
        "name": "TikTok Pixel",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"analytics\.tiktok\.com/i18n/pixel/events\.js"
            },
            {
                "source": "cookies",
                "key": "_ttp",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_tt_enable_cookie",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"ttq\.load\("
            }
        ]
    },
    {
        "name": "Pinterest Tag",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"s\.pinimg\.com/ct/core\.js"
            },
            {
                "source": "cookies",
                "key": "_pin_unauth",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_derived_epik",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"pintrk\(['\"]load['\"]"
            }
        ]
    },
    {
        "name": "Snap Pixel",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sc-static\.net/scevent\.min\.js"
            },
            {
                "source": "cookies",
                "key": "_scid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_sctr",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"snaptr\(['\"]init['\"]"
            }
        ]
    },
    {
        "name": "LinkedIn Insight Tag",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"snap\.licdn\.com/li\.lms-analytics/insight\.min\.js"
            },
            {
                "source": "cookies",
                "key": "li_fat_id",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_linkedin_partner_id"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"px\.ads\.linkedin\.com/collect/"
            }
        ]
    },
    {
        "name": "X Pixel",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.ads-twitter\.com/uwt\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"twq\(['\"](?:init|config)['\"]"
            }
        ]
    },
    {
        "name": "Reddit Pixel",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"redditstatic\.com/ads/pixel\.js"
            },
            {
                "source": "cookies",
                "key": "_rdt_uuid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"rdt\(['\"]init['\"]"
            }
        ]
    },
    {
        "name": "Quora Pixel",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"a\.quora\.com/qevents\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"qp\(['\"]init['\"]"
            }
        ]
    },
    {
        "name": "Microsoft Advertising UET",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"bat\.bing\.com/bat\.js"
            },
            {
                "source": "cookies",
                "key": "_uetsid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_uetvid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"uetq\.push\("
            }
        ]
    },
    {
        "name": "Google Ads Conversion Tracking",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"googletagmanager\.com/gtag/js\?id=AW-"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"googleadservices\.com/pagead/conversion"
            },
            {
                "source": "cookies",
                "key": "_gcl_au",
                "pattern": r"^1\.1\."
            },
            {
                "source": "cookies",
                "key": "_gcl_aw",
                "pattern": r"^GCL\."
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"gtag\(['\"]config['\"],\s*['\"]AW-\d+['\"]"
            }
        ]
    },
    {
        "name": "Criteo OneTag",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:dynamic\.criteo\.com|static\.criteo\.net)/js/ld/ld\.js"
            },
            {
                "source": "cookies",
                "key": "cto_bundle",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.criteo_q"
            }
        ]
    },
    {
        "name": "Taboola Pixel",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.taboola\.com/libtrc/unip/\d+/tfa\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_tfa\.push\("
            }
        ]
    },
    {
        "name": "Outbrain Pixel",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"amplify\.outbrain\.com/cp/obtp\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"obApi\(['\"]track['\"]"
            }
        ]
    },
    {
        "name": "HubSpot Analytics",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js(?:-eu1)?\.hs-analytics\.net/analytics/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js(?:-eu1)?\.hs-scripts\.com/\d+\.js"
            },
            {
                "source": "cookies",
                "key": "hubspotutk",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "__hstc",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "__hssc",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Marketo Munchkin",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"munchkin\.marketo\.net/(?:\d+/)?munchkin\.js"
            },
            {
                "source": "cookies",
                "key": "_mkto_trk",
                "pattern": r"^id:"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Munchkin\.init\("
            }
        ]
    },
    {
        "name": "Salesforce Account Engagement",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"pi\.pardot\.com/pd\.js"
            },
            {
                "source": "cookies",
                "key": "pardot",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"pi\.pardot\.com/pd\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"piAId\s*=\s*['\"]\d+['\"]"
            }
        ]
    },
    {
        "name": "ActiveCampaign Site Tracking",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"diffuser-cdn\.app-us1\.com/diffuser/diffuser\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"vgo\(['\"]setAccount['\"]"
            }
        ]
    },
    {
        "name": "Brevo Tracker",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sibautomation\.com/sa\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.brevo\.com/js/sdk-loader\.js"
            },
            {
                "source": "cookies",
                "key": "sib_cuid",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Customer.io",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"assets\.customer\.io/assets/track(?:-eu)?\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdp\.customer\.io/v1/analytics-js/"
            },
            {
                "source": "cookies",
                "key": "_cioid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_cio\.push\("
            }
        ]
    },
    {
        "name": "Braze",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.appboycdn\.com/web-sdk/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"braze\.initialize\("
            }
        ]
    },
    {
        "name": "CleverTap",
        "categories": ["Analytics", "Product Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"d2r1yp2w7bby2u\.cloudfront\.net/js/(?:clevertap|a)\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"clevertap\.event\.push\("
            }
        ]
    },
    {
        "name": "MoEngage",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.moengage\.com/webpush/moe_webSdk\.min\.latest\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.moengage\.com/"
            }
        ]
    },
    {
        "name": "WebEngage",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:widgets\.in|ssl\.widgets)\.webengage\.com/js/webengage-min-"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"webengage\.init\("
            }
        ]
    },
    {
        "name": "Insider",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"api\.useinsider\.com/ins\.js"
            },
            {
                "source": "cookies",
                "key": "insdrSV",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"api\.useinsider\.com/ins\.js"
            }
        ]
    },
    {
        "name": "Bloomreach Engagement",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"api(?:\.uk)?\.exponea\.com/js/exponea\.min\.js"
            },
            {
                "source": "cookies",
                "key": "__exponea_etc__",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "__exponea_time2__",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"exponea\.start\("
            }
        ]
    },
    {
        "name": "Dynamic Yield",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn(?:-eu)?\.dynamicyield\.com/api/\d+/api_(?:dynamic|static)\.js"
            },
            {
                "source": "cookies",
                "key": "_dyid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_dyid_server",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_dyjsession",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Kameleoon",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"\.kameleoon\.(?:eu|io)/kameleoon\.js"
            },
            {
                "source": "cookies",
                "key": "kameleoonVisitorCode",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "AB Tasty",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"try\.abtasty\.com/[a-f0-9]+\.js"
            },
            {
                "source": "cookies",
                "key": "ABTasty",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "ABTastySession",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Optimizely",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.optimizely\.com/(?:js/\d+\.js|public/)"
            },
            {
                "source": "cookies",
                "key": "optimizelyEndUserId",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.optimizely\.com/js/"
            }
        ]
    },
    {
        "name": "Convert Experiences",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn-\d+\.convertexperiments\.com/js/"
            },
            {
                "source": "cookies",
                "key": "_conv_v",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_conv_s",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Adobe Target",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "cookies",
                "key": "mbox",
                "pattern": r"session#"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"adobe\.target\.getOffer"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"tt\.omtrdc\.net/m2/"
            }
        ]
    },
    {
        "name": "Monetate",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"se\.monetate\.net/js/"
            },
            {
                "source": "cookies",
                "key": "mt.v",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"monetateQ"
            }
        ]
    },
    {
        "name": "Salesforce Marketing Cloud Personalization",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.evgnet\.com/beacon/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.evgnet\.com/beacon/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.Evergage"
            }
        ]
    },
    {
        "name": "Qubit",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.goqubit\.com/smartserve-"
            },
            {
                "source": "cookies",
                "key": "_qubitTracker",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Intellimize",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.intellimize\.co/snippet/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.intellimize\.co/snippet/"
            }
        ]
    },
    {
        "name": "Mutiny",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"client-registry\.mutinycdn\.com/personalize/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"client-registry\.mutinycdn\.com/personalize/"
            }
        ]
    },
    {
        "name": "Nosto",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"connect\.nosto\.com/include/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"connect\.nosto\.com/include/"
            }
        ]
    },
    {
        "name": "Ometria",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.ometria\.com/tags/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"ometria\.track\("
            }
        ]
    },
    {
        "name": "SAP Emarsys",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.scarabresearch\.com/js/"
            },
            {
                "source": "cookies",
                "key": "scarab.visitor",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"ScarabQueue\.push\("
            }
        ]
    },
    {
        "name": "Bluecore",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"www\.bluecore\.com/triggermail\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"www\.triggermail\.io/js/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"triggermail\.push\("
            }
        ]
    },
    {
        "name": "BlueConic",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"\.blueconic\.net/frontend/static/javascript/blueconic/blueconic\.min\.js"
            },
            {
                "source": "cookies",
                "key": "BCSessionID",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Treasure Data",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.treasuredata\.com/sdk/"
            },
            {
                "source": "cookies",
                "key": "_td",
                "pattern": r"^[0-9a-f-]{36}$"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.treasuredata\.com/sdk/"
            }
        ]
    },
    {
        "name": "Zeotap",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"content\.zeotap\.com/sdk/idm\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"content\.zeotap\.com/sdk/"
            }
        ]
    },
    {
        "name": "Clearbit",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"tag\.clearbitscripts\.com/v1/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"tag\.clearbitscripts\.com/v1/"
            }
        ]
    },
    {
        "name": "6sense",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"j\.6sc\.co/6si\.min\.js"
            },
            {
                "source": "cookies",
                "key": "_6senseCompanyDetails",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"j\.6sc\.co/6si\.min\.js"
            }
        ]
    },
    {
        "name": "Demandbase",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:tag|scripts)\.demandbase\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:tag|scripts)\.demandbase\.com/"
            }
        ]
    },
    {
        "name": "Leadfeeder",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sc\.lfeeder\.com/lftracker_v1_"
            },
            {
                "source": "cookies",
                "key": "_lfa",
                "pattern": r"^LF1\."
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"sc\.lfeeder\.com/lftracker_v1_"
            }
        ]
    },
    {
        "name": "Albacross",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"serve\.albacross\.com/track\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"serve\.albacross\.com/track\.js"
            }
        ]
    },
    {
        "name": "Leadinfo",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.leadinfo\.net/ping\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.leadinfo\.net/ping\.js"
            }
        ]
    },
    {
        "name": "RB2B",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"ddwl4m2hdecbv\.cloudfront\.net/b/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"s3-us-west-2\.amazonaws\.com/b2bjsstore/b/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"reb2b\.load\("
            }
        ]
    },
    {
        "name": "Warmly",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"opps-widget\.getwarmly\.com/warmly\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"opps-widget\.getwarmly\.com/warmly\.js"
            }
        ]
    },
    {
        "name": "ZoomInfo WebSights",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"ws\.zoominfo\.com/pixel/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"ws\.zoominfo\.com/pixel/"
            }
        ]
    },
    {
        "name": "Apollo Visitor Tracking",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"assets\.apollo\.io/micro/website-tracker/tracker\.iife\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"assets\.apollo\.io/micro/website-tracker/"
            }
        ]
    },
    {
        "name": "Lead Forensics",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"secure\.leadforensics\.com/js/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"secure\.leadforensics\.com/js/"
            }
        ]
    },
    {
        "name": "Snitcher",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"radar\.snitcher\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"radar\.snitcher\.com/"
            }
        ]
    },
    {
        "name": "Visitor Queue",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"t\.visitorqueue\.com/p/tracking\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"t\.visitorqueue\.com/p/tracking\.min\.js"
            }
        ]
    },
    {
        "name": "Happierleads",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"m\.happierleads\.com/v\d+/script"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"m\.happierleads\.com/"
            }
        ]
    },
    {
        "name": "CallRail",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.callrail\.com/companies/"
            },
            {
                "source": "cookies",
                "key": "calltrk_referrer",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "calltrk_landing",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "calltrk_session_id",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Invoca",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"solutions\.invocacdn\.com/js/"
            },
            {
                "source": "cookies",
                "key": "invoca_session",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Infinity Call Tracking",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"d30ke5tqu2tkyx\.cloudfront\.net/infinity_common\.min\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.infinity-tracking\.net/"
            },
            {
                "source": "cookies",
                "key": "ictf_master",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "WhatConverts",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"scripts\.iconnode\.com/\d+\.js"
            },
            {
                "source": "cookies",
                "key": "wc_visitor",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "wc_client",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Marfeel",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sdk\.mrf\.io/statics/marfeel-sdk\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"sdk\.mrf\.io/statics/marfeel-sdk\.js"
            }
        ]
    },
    {
        "name": "Cxense",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.cxense\.com/cx\.js"
            },
            {
                "source": "cookies",
                "key": "cX_P",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "cX_S",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cX\.callQueue\.push\("
            }
        ]
    },
    {
        "name": "Permutive",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.permutive\.com/[a-f0-9-]+-web\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"permutive\.addon\("
            }
        ]
    },
    {
        "name": "Lotame",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"tags\.crwdcntrl\.net/c/\d+/cc(?:_af)?\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"tags\.crwdcntrl\.net/c/"
            }
        ]
    },
    {
        "name": "Oracle BlueKai",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"tags\.bkrtx\.com/js/bk-coretag\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"tags\.bkrtx\.com/js/bk-coretag\.js"
            }
        ]
    },
    {
        "name": "Oracle Infinity",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"c\.oracleinfinity\.io/acs/account/"
            },
            {
                "source": "cookies",
                "key": "ORA_FPC",
                "pattern": r"id="
            }
        ]
    },
    {
        "name": "SAS Customer Intelligence 360",
        "categories": ["Analytics", "Customer Data Platform"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"execution-ci360\.sas\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"ot-\d+\.cid\.sas\.com/"
            }
        ]
    },
    {
        "name": "Acoustic Digital Analytics",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"libs\.coremetrics\.com/eluminate\.js"
            },
            {
                "source": "cookies",
                "key": "CoreID6",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "cmTPSet",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cmSetClientID\("
            }
        ]
    },
    {
        "name": "AppsFlyer Web SDK",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"websdk\.appsflyer\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"websdk\.appsflyer\.com/"
            }
        ]
    },
    {
        "name": "Branch",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.branch\.io/branch-latest\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"branch\.init\("
            }
        ]
    },
    {
        "name": "Adjust Web SDK",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.adjust\.com/adjust-latest\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.adjust\.com/adjust-latest\.min\.js"
            }
        ]
    },
    {
        "name": "Singular Web SDK",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"web-sdk-cdn\.singular\.net/singular-sdk/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"web-sdk-cdn\.singular\.net/singular-sdk/"
            }
        ]
    },
    {
        "name": "Airbridge",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.airbridge\.io/sdk/latest/airbridge\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"airbridge\.init\("
            }
        ]
    },
    {
        "name": "Frosmo",
        "categories": ["Analytics", "Conversion Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"in\.frosmo\.com/frosmo\.easy\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"in\.frosmo\.com/frosmo\.easy\.js"
            }
        ]
    },
    {
        "name": "UserZoom",
        "categories": ["Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\d*\.userzoom\.com/trueintent/js/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"userzoom\.com/trueintent/js/"
            }
        ]
    },
    {
        "name": "Marin Software",
        "categories": ["Analytics", "Marketing Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"tracker\.marinsm\.com/tp"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"tracker\.marinsm\.com/tp"
            }
        ]
    }
]