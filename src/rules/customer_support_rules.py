TECH_RULES = [
    {
        "name": "Zendesk",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.zdassets\.com/ekr/snippet\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"v2\.zopim\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"id=[\"']ze-snippet[\"']|zE\(['\"]webWidget"
            }
        ]
    },
    {
        "name": "Gorgias",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"config\.gorgias\.chat/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"bundle\.gorgias\.chat/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"gorgias-chat-container|GorgiasChat\.init\("
            }
        ]
    },
    {
        "name": "Intercom",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"widget\.intercom\.io/widget/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.intercomcdn\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.intercomSettings\s*=|intercom-lightweight-app"
            }
        ]
    },
    {
        "name": "Freshdesk",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:euc-|ind-|au-)?widget\.freshworks\.com/widgets/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"wchat\.freshchat\.com/js/widget\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"FreshworksWidget\(|window\.fcWidget\."
            }
        ]
    },
    {
        "name": "Help Scout",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"beacon-v2\.helpscout\.net"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Beacon\(['\"]init['\"]"
            }
        ]
    },
    {
        "name": "Kustomer",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.kustomerapp\.com/chat-web/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Kustomer\.start\(|kustomer-chat-container"
            }
        ]
    },
    {
        "name": "Salesforce Service Cloud",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"service\.force\.com/embeddedservice/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"salesforceliveagent\.com/content/g/js/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"embedded_svc\.init\(|liveagent\.init\("
            }
        ]
    },
    {
        "name": "Tidio",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"code\.tidio\.co/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"id=[\"']tidio-chat[\"']|tidioChatApi"
            }
        ]
    },
    {
        "name": "LiveChat",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.livechatinc\.com/tracking\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.__lc\s*=|LiveChatWidget\.(?:init|call)\("
            }
        ]
    },
    {
        "name": "Crisp",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"client\.crisp\.chat/l\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.\$crisp\s*=|CRISP_WEBSITE_ID"
            }
        ]
    },
    {
        "name": "Tawk.to",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"embed\.tawk\.to/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Tawk_API\s*=|Tawk_LoadStart"
            }
        ]
    },
    {
        "name": "Olark",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.olark\.com/jsclient/loader"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"olark\.identify\(|id=[\"']olark-wrapper[\"']"
            }
        ]
    },
    {
        "name": "Re:amaze",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.reamaze\.com/assets/reamaze"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"_support\[['\"]account['\"]\]|data-reamaze-"
            }
        ]
    },
    {
        "name": "Gladly",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.gladly\.com/(?:gladly/)?chat-sdk/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Gladly\.init\(|id=[\"']gladlyChat_container[\"']"
            }
        ]
    },
    {
        "name": "Drift",
        "categories": ["Customer Support"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.driftt\.com/include/"
            },
            {
                "source": "cookies",
                "key": "driftt_aid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"drift\.load\(['\"][a-z0-9]+['\"]\)|id=[\"']drift-frame-controller[\"']"
            }
        ]
    }
]