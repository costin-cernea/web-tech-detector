TECH_RULES = [
    {
        "name": "Klaviyo",
        "categories": ["Marketing", "Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.klaviyo\.com/onsite/js/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"a\.klaviyo\.com/media/js/"
            },
            {
                "source": "cookies",
                "key": "__kla_id",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"klaviyo-form-|_learnq\.push\("
            }
        ]
    },
    {
        "name": "Mailchimp",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"chimpstatic\.com/mcjs-connected/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"s3\.amazonaws\.com/downloads\.mailchimp\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"list-manage\.com/subscribe/post|id=[\"']mc_embed_signup[\"']"
            }
        ]
    },
    {
        "name": "Omnisend",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"omnisnippet1\.com/inshop/launcher"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"omnisend\.com/"
            },
            {
                "source": "cookies",
                "key": "omnisendSessionID",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.omnisend\s*="
            }
        ]
    },
    {
        "name": "Attentive",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.attn\.tv/"
            },
            {
                "source": "cookies",
                "key": "__attentive_id",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.__attentive|attn\.tv/tag/"
            }
        ]
    },
    {
        "name": "Braze",
        "categories": ["Marketing", "Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.appboycdn\.com/web-sdk/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sdk\.(?:iad|fra)-\d+\.braze\.(?:com|eu)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"braze\.initialize\(|appboy\.initialize\("
            }
        ]
    },
    {
        "name": "Iterable",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.iterable\.com/"
            },
            {
                "source": "cookies",
                "key": "iterableEndUserId",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_iaq\.push\(|api\.iterable\.com/"
            }
        ]
    },
    {
        "name": "ActiveCampaign",
        "categories": ["Marketing", "Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"diffuser-cdn\.app-us1\.com/diffuser/diffuser\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"trackcmp\.net/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"trackcmp\.net/visit|vgo\(['\"]setAccount['\"]"
            }
        ]
    },
    {
        "name": "HubSpot",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js(?:-eu1|-na1)?\.hs-scripts\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js(?:-eu1|-na1)?\.hsforms\.net/"
            },
            {
                "source": "cookies",
                "key": "hubspotutk",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"hbspt\.forms\.create\("
            }
        ]
    },
    {
        "name": "Salesforce Marketing Cloud",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"collect\.igodigital\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_etmc\.push\(|exacttarget\.com/"
            }
        ]
    },
    {
        "name": "Brevo",
        "categories": ["Marketing", "Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sibautomation\.com/sa\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.brevo\.com/"
            },
            {
                "source": "cookies",
                "key": "sib_cuid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"sibforms\.com/forms/|window\.sendinblue\b"
            }
        ]
    },
    {
        "name": "Drip",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:tag|dc)\.getdrip\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_dcq\.push\(|getdrip\.com/forms/"
            }
        ]
    },
    {
        "name": "Campaign Monitor",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:js\.)?createsend1?\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"createsend\.com/t/[a-z]/|class=[\"'][^\"']*js-cm-form"
            }
        ]
    },
    {
        "name": "Postscript",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sdk\.postscript\.io/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.postscript\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"postscript-popup|window\.postscript\b"
            }
        ]
    },
    {
        "name": "Yotpo",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"staticw2\.yotpo\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn-widgetsrepository\.yotpo\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"forms-akamai\.smsbump\.com/|cdn-loyalty\.yotpo\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"yotpo-widget-instance|class=[\"'][^\"']*yotpo-main-widget"
            }
        ]
    },
    {
        "name": "LoyaltyLion",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sdk\.loyaltylion\.net/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"loyaltylion\.init\(|data-lion-"
            }
        ]
    },
    {
        "name": "Smile.io",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.smile\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"smile-ui-lite-container|class=[\"'][^\"']*sweettooth-init|SmileUI\.init\("
            }
        ]
    },
    {
        "name": "ReferralCandy",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"portal\.referralcandy\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.referralcandy\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-refcandy-|referralcandy\.com/assets/"
            }
        ]
    },
    {
        "name": "Recharge",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.rechargecdn\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.rechargepayments\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"rc-widget__|rechargepayments\.com/|data-recharge-"
            }
        ]
    },
    {
        "name": "Privy",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"widget\.privy\.com/assets/widget\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"privy-popup-content|privy-embedded-form|window\.Privy\b"
            }
        ]
    },
    {
        "name": "Justuno",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.justuno\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jst\.ai/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.ju_num\s*=|juapp\(['\"]"
            }
        ]
    },
    {
        "name": "OptinMonster",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"a\.omappapi\.com/app/js/api\.min\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"a\.optmnstr\.com/app/js/api\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"om-holder|data-omapp-"
            }
        ]
    },
    {
        "name": "Wisepops",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"loader\.wisepops\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"wisepops\.net/loader\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"wisepops\(['\"]|wisepops-root"
            }
        ]
    },
    {
        "name": "Sumo",
        "categories": ["Marketing"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"load\.sumo\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"load\.sumome\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-sumo-site-id|sumome-react-wysiwyg"
            }
        ]
    }
]