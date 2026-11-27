TECH_RULES = [
    {
        "name": "WordPress",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-pingback",
                "pattern": r"/xmlrpc\.php"
            },
            {
                "source": "headers",
                "key": "link",
                "pattern": r"https?://api\.w\.org/"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"^wordpress\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-includes/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/wp-content/(?:themes|plugins|uploads)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/wp-includes/js/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/wp-json/wp/v2/"
            }
        ]
    },
    {
        "name": "Drupal",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-generator",
                "pattern": r"\bdrupal\b"
            },
            {
                "source": "headers",
                "key": "x-drupal-cache",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-drupal-dynamic-cache",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bdrupal\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/core/misc/drupal\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/misc/drupal\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/sites/default/files/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-drupal-selector="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-drupal-settings-selector=[\"']drupal-settings-json[\"']"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"jQuery\.extend\(Drupal\.settings"
            }
        ]
    },
    {
        "name": "Joomla",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bjoomla!"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/media/system/js/core(?:\.min)?\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/media/jui/js/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/media/com_content/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bjoomla-script-options\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/media/system/js/core(?:\.min)?\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/media/templates/site/cassiopeia/"
            }
        ]
    },
    {
        "name": "TYPO3",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-typo3-cache",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "fe_typo_user",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\btypo3\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/typo3conf/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/typo3temp/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"This website is powered by TYPO3"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/typo3conf/ext/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/typo3temp/assets/"
            }
        ]
    },
    {
        "name": "Ghost",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"^ghost\b"
            },
            {
                "source": "headers",
                "key": "x-ghost-cache-status",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"^ghost\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"@tryghost/(?:portal|sodo-search|comments-ui)"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/public/cards\.min\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-ghost="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bkg-card\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/ghost/api/content/"
            }
        ]
    },
    {
        "name": "HubSpot CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-hs-content-id",
                "pattern": r"^\d+$"
            },
            {
                "source": "headers",
                "key": "x-hs-content-group-id",
                "pattern": r"^\d+$"
            },
            {
                "source": "headers",
                "key": "x-hs-hub-id",
                "pattern": r"^\d+$"
            },
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bhubspot\b"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bhubspot\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/hs/hsstatic/cos-i18n/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/hs-fs/hub/\d+/hub_generated/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bhs_cos_wrapper\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bhs-content-id-\d+\b"
            }
        ]
    },
    {
        "name": "Adobe Experience Manager",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/etc\.clientlibs/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/etc/clientlibs/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/etc/designs/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/etc\.clientlibs/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/content/dam/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\baem-Grid\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bcmp-experiencefragment\b"
            }
        ]
    },
    {
        "name": "Sitecore",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "SC_ANALYTICS_GLOBAL_COOKIE",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "sc_expview",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "website#lang",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bsitecore\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/-/media/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/sitecore/shell/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/-/media/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/-/jssmedia/"
            }
        ]
    },
    {
        "name": "Umbraco",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-umbraco-version",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "UMB_UCONTEXT",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "UMB_UPDCHK",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "UMB_XSRF_TOKEN",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bumbraco\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/umbraco/lib/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/App_Plugins/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/umbraco/surface/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bumb-grid\b"
            }
        ]
    },
    {
        "name": "Optimizely CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "EPiStateMarker",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "EPiServerLogin",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"(?:\bepiserver\b|\boptimizely\s+cms\b)"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/EPiServer/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/Util/Find/epi-util/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"dl\.episerver\.net"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/EPiServer\.Forms/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bEPiServerForms\b"
            }
        ]
    },
    {
        "name": "Kentico",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "CMSPreferredCulture",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "CMSCsrfCookie",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "CMSCurrentTheme",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "CMSCookieLevel",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bkentico\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/CMSPages/GetResource\.ashx"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/Kentico\.(?:Content|Resource)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/CMSPages/GetResource\.ashx"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/getmedia/[a-f0-9-]{36}/"
            }
        ]
    },
    {
        "name": "Progress Sitefinity",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bsitefinity\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/Frontend-Assembly/Telerik\.Sitefinity"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"Telerik\.Sitefinity\.Resources"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/Frontend-Assembly/Telerik\.Sitefinity"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bsf_colsIn\b"
            }
        ]
    },
    {
        "name": "Craft CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bcraft\s+cms\b"
            },
            {
                "source": "cookies",
                "key": "CraftSessionId",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "CRAFT_CSRF_TOKEN",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/cpresources/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"name=[\"']CRAFT_CSRF_TOKEN[\"']"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/cpresources/"
            }
        ]
    },
    {
        "name": "Statamic",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bstatamic\b"
            },
            {
                "source": "headers",
                "key": "x-statamic-static-cache",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bstatamic\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/!/statamic/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"statamic_csrf"
            }
        ]
    },
    {
        "name": "Kirby",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bkirby\b"
            },
            {
                "source": "cookies",
                "key": "kirby_session",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bkirby\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/media/site/[a-f0-9]+-\d+/"
            }
        ]
    },
    {
        "name": "ProcessWire",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bprocesswire\b"
            },
            {
                "source": "cookies",
                "key": "wires_challenge",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bprocesswire\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wire/modules/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/site/assets/files/\d+/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/wire/modules/"
            }
        ]
    },
    {
        "name": "Silverstripe",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-silverstripe-cache",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bsilverstripe\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/_resources/vendor/silverstripe/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/_resources/vendor/silverstripe/"
            }
        ]
    },
    {
        "name": "Contao",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bcontao\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/bundles/contaocore/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/assets/contao/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<!--\s*indexer::stop\s*-->"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/bundles/contaocore/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bce_text\s+block\b"
            }
        ]
    },
    {
        "name": "Concrete CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "CONCRETE5",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "CONCRETE",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bconcrete(?:5|\s+cms)\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/concrete/js/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/packages/concrete_"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"var\s+CCM_DISPATCHER_FILENAME\s*="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/concrete/css/"
            }
        ]
    },
    {
        "name": "MODX",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bmodx\b"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bmodx\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"powered by\s+modx"
            }
        ]
    },
    {
        "name": "ExpressionEngine",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "exp_last_visit",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "exp_last_activity",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "exp_tracker",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "exp_csrf_token",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bexpressionengine\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/themes/ee/"
            }
        ]
    },
    {
        "name": "October CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "october_session",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/modules/system/assets/js/framework(?:\.extras)?(?:\.min)?\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/modules/system/assets/js/framework(?:\.extras)?(?:\.min)?\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-request-flash"
            }
        ]
    },
    {
        "name": "Winter CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "winter_session",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/modules/system/assets/js/snowboard"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/modules/system/assets/js/snowboard"
            }
        ]
    },
    {
        "name": "Grav",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"^grav(?:\s*cms)?\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-grav-"
            }
        ]
    },
    {
        "name": "Backdrop CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-generator",
                "pattern": r"\bbackdrop\s+cms\b"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bbackdrop\s+cms\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/core/misc/backdrop\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Backdrop\.settings"
            }
        ]
    },
    {
        "name": "Neos CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-flow-powered",
                "pattern": r"\bneos\b"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bneos\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/_Resources/Static/Packages/Neos\."
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/_Resources/Static/Packages/Neos\."
            }
        ]
    },
    {
        "name": "Pimcore",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bpimcore\b"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bpimcore\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/bundles/pimcore"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/bundles/pimcore"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"pimcore_area_"
            }
        ]
    },
    {
        "name": "Wagtail",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bwagtail\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/static/wagtail"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/static/wagtail"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\brichtext-image\b"
            }
        ]
    },
    {
        "name": "Django CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/static/cms/js/dist/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bcms-structure-mode\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-cms-toolbar"
            }
        ]
    },
    {
        "name": "Plone",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bplone\b"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bplone\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/\+\+plone\+\+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/\+\+resource\+\+plone"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/\+\+plone\+\+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bportaltype-"
            }
        ]
    },
    {
        "name": "SPIP",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "composed-by",
                "pattern": r"\bspip\b"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bspip\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/prive/javascript/spip"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"spip\.php\?(?:article|rubrique|page)="
            }
        ]
    },
    {
        "name": "1C-Bitrix",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-cms",
                "pattern": r"bitrix"
            },
            {
                "source": "cookies",
                "key": "BITRIX_SM_GUEST_ID",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "BITRIX_SM_LAST_VISIT",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "BITRIX_SM_SALE_UID",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/bitrix/(?:js|cache/js)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/bitrix/templates/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"BX\.setJSList\("
            }
        ]
    },
    {
        "name": "DataLife Engine",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"datalife\s+engine"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/engine/classes/js/dle_js\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"var\s+dle_root\s*="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"var\s+dle_skin\s*="
            }
        ]
    },
    {
        "name": "Contentful",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:cdn|graphql)\.contentful\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:images|downloads|videos|assets)\.(?:eu\.)?ctfassets\.net/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:cdn|graphql)\.contentful\.com"
            }
        ]
    },
    {
        "name": "Sanity",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.sanity\.io"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.sanity\.io/(?:images|files)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"apicdn\.sanity\.io"
            }
        ]
    },
    {
        "name": "Storyblok",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"app\.storyblok\.com/f/storyblok-v2-latest\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"a2?\.storyblok\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"a2?\.storyblok\.com/f/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"img2\.storyblok\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"api(?:-us)?\.storyblok\.com"
            }
        ]
    },
    {
        "name": "Prismic",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.cdn\.prismic\.io/prismic\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"images\.prismic\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"\.cdn\.prismic\.io/api/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"static\.cdn\.prismic\.io/prismic\.js"
            }
        ]
    },
    {
        "name": "DatoCMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"www\.datocms-assets\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"graphql\.datocms\.com"
            }
        ]
    },
    {
        "name": "Hygraph",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"media\.graphassets\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"media\.graphcms\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"[a-z0-9-]+\.graphassets\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"api-[a-z0-9-]+\.(?:hygraph|graphcms)\.com"
            }
        ]
    },
    {
        "name": "Strapi",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bstrapi\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"\.media\.strapiapp\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"\.strapiapp\.com/uploads/"
            }
        ]
    },
    {
        "name": "Directus",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bdirectus\b"
            },
            {
                "source": "cookies",
                "key": "directus_refresh_token",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "directus_session_token",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"\.directus\.app/assets/"
            }
        ]
    },
    {
        "name": "Builder.io",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.builder\.io"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.builder\.io/api/v\d+/image/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bbuilder-blocks\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bbuilder-component\b"
            }
        ]
    },
    {
        "name": "Contentstack",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:eu-|au-|azure-na-|azure-eu-|gcp-na-|gcp-eu-)?images\.contentstack\.(?:io|com)/v3/assets/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"assets\.contentstack\.io/"
            }
        ]
    },
    {
        "name": "Amplience",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.(?:media|graphics)\.amplience\.net/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"i\d*\.adis\.ws/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.c\d+\.amplience\.net/"
            }
        ]
    },
    {
        "name": "Kontent.ai",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"assets-[a-z0-9-]+\.kc-usercontent\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"deliver\.kontent\.ai/"
            }
        ]
    },
    {
        "name": "ButterCMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.buttercms\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"api\.buttercms\.com/"
            }
        ]
    },
    {
        "name": "microCMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"images\.microcms-assets\.io/assets/"
            }
        ]
    },
    {
        "name": "Agility CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.aglty\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"api\.aglty\.io/"
            }
        ]
    },
    {
        "name": "Cosmic",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"imgix\.cosmicjs\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.cosmicjs\.com/"
            }
        ]
    },
    {
        "name": "Crystallize",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"media\.crystallize\.com/"
            }
        ]
    },
    {
        "name": "Prepr",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"\.stream\.prepr\.io/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.prepr\.io/"
            }
        ]
    },
    {
        "name": "TinaCMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"assets\.tina\.io/"
            }
        ]
    },
    {
        "name": "Liferay",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "liferay-portal",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "GUEST_LANGUAGE_ID",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/o/frontend-js-web/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/html/js/liferay/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Liferay\.ThemeDisplay"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/o/frontend-css-web/"
            }
        ]
    },
    {
        "name": "Magnolia",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-magnolia-registration",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/\.resources/[^/]+/webresources/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/\.resources/[^\"']+/webresources/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/\.imaging/"
            }
        ]
    },
    {
        "name": "CoreMedia",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/blueprint/servlet/resource/blob/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/blueprint/servlet/resource/blob/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-cm-refreshable-fragment"
            }
        ]
    },
    {
        "name": "Bloomreach Experience Manager",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"<!--\s*\{\"HST-Type\":"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"hst-cmseditlink"
            }
        ]
    },
    {
        "name": "DNN",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "dnn_IsMobile",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": ".DOTNETNUKE",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bdotnetnuke\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/DesktopModules/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/js/dnncore\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/Portals/_default/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/DesktopModules/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/Portals/\d+/"
            }
        ]
    },
    {
        "name": "Orchard Core",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\borchard(?:\s+core)?\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/OrchardCore\."
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/OrchardCore\."
            }
        ]
    },
    {
        "name": "RWS Tridion",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\btridion\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"tcm:\d+-\d+"
            }
        ]
    },
    {
        "name": "Squiz Matrix",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bsquiz\s+matrix\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Running\s+(?:MySource|Squiz)\s+Matrix"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/__data/assets/"
            }
        ]
    },
    {
        "name": "Omni CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"<!--\s*com\.omniupdate\."
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"a\.cms\.omniupdate\.com"
            }
        ]
    },
    {
        "name": "TERMINALFOUR",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bterminalfour\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<!--\s*navigation object\s*:"
            }
        ]
    },
    {
        "name": "Jahia",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bjahia\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/files/live/sites/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/files/live/sites/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"jahiaGWTParameters"
            }
        ]
    },
    {
        "name": "Ibexa DXP",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"(?:\bez\s*publish\b|\bez\s*platform\b|\bibexa\b)"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"(?:\bez\s*publish\b|\bez\s*platform\b|\bibexa\b)"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/bundles/(?:ibexa|ezplatform)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/bundles/(?:ibexa|ezplatform)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/var/site/storage/images/"
            }
        ]
    },
    {
        "name": "Ektron CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "EktGUID",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/WorkArea/java/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/WorkArea/FrameworkUI/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"EktronClientManager"
            }
        ]
    },
    {
        "name": "Crownpeak",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.crownpeak\.net"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.crownpeak\.net"
            }
        ]
    },
    {
        "name": "FirstSpirit",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bfirstspirit\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"powered by\s+firstspirit"
            }
        ]
    },
    {
        "name": "Blogger",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"^blogger$"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"www\.blogger\.com/static/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"resources\.blogblog\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"www\.blogger\.com/static/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"www\.blogger\.com/feeds/\d+/posts/"
            }
        ]
    },
    {
        "name": "Medium",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "al:ios:app_name",
                "pattern": r"^medium$"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn-client\.medium\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn-client\.medium\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"miro\.medium\.com"
            }
        ]
    },
    {
        "name": "Substack",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"substackcdn\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"substackcdn\.com/bundle/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"substack-post-media\.s3\.amazonaws\.com"
            }
        ]
    },
    {
        "name": "MediaWiki",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bmediawiki\b"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"^mediawiki\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/load\.php\?.*modules=startup"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bmediawiki\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"RLCONF\s*="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"id=[\"']mw-content-text[\"']"
            }
        ]
    },
    {
        "name": "DokuWiki",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "DokuWiki",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"^dokuwiki$"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/lib/exe/js\.php"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/lib/exe/css\.php"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"id=[\"']dokuwiki__site[\"']"
            }
        ]
    },
    {
        "name": "BookStack",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "bookstack_session",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"href=[\"']https?://www\.bookstackapp\.com"
            }
        ]
    },
    {
        "name": "Arc XP",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"arc-anglerfish-"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Fusion\.globalContent\s*="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"images\.arcpublishing\.com"
            }
        ]
    },
    {
        "name": "Brightspot",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"brightspotcdn\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"brightspotcdn\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-bsp-"
            }
        ]
    },
    {
        "name": "RebelMouse",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"assets\.rebelmouse\.io"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"assets\.rebelmouse\.io"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"rebelmouse-image"
            }
        ]
    },
    {
        "name": "NationBuilder",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "cookies",
                "key": "_nbuild_session",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"assets\.nationbuilder\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"assets\.nationbuilder\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"nationbuilder\.com/themes/"
            }
        ]
    },
    {
        "name": "Movable Type",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bmovable\s+type\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/mt-static/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/mt-static/"
            }
        ]
    },
    {
        "name": "Textpattern",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\btextpattern\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"powered by\s+textpattern"
            }
        ]
    },
    {
        "name": "CMS Made Simple",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bcms\s+made\s+simple\b"
            }
        ]
    },
    {
        "name": "REDAXO",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"index\.php\?rex_media_type="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/media/rex_"
            }
        ]
    },
    {
        "name": "Hatena Blog",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.blog\.st-hatena\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.blog\.st-hatena\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn-ak\.f\.st-hatena\.com"
            }
        ]
    },
    {
        "name": "a-blog cms",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\ba-blog\s+cms\b"
            }
        ]
    },
    {
        "name": "Weblication",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bweblication\b"
            }
        ]
    },
    {
        "name": "Sulu CMS",
        "categories": ["CMS"],
        "rules": [
            {
                "source": "headers",
                "key": "x-generator",
                "pattern": r"\bsulu\b"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bsulu\b"
            }
        ]
    }
]