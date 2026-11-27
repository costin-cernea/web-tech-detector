TECH_RULES = [
    {
        "name": "Cloudflare",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"^cloudflare$"
            },
            {
                "source": "headers",
                "key": "cf-ray",
                "pattern": r"^[0-9a-f]+-[a-z]{3}$"
            },
            {
                "source": "cookies",
                "key": "__cf_bm",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/cdn-cgi/(?:scripts|rum|challenge-platform)/"
            }
        ]
    },
    {
        "name": "Fastly",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "x-served-by",
                "pattern": r"\bcache-[a-z]{3,4}\d+"
            },
            {
                "source": "headers",
                "key": "x-fastly-request-id",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-timer",
                "pattern": r"^S\d+\.\d+,VS\d+,VE\d+"
            }
        ]
    },
    {
        "name": "Akamai",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"\bAkamaiGHost\b|\bAkamaiNetStorage\b"
            },
            {
                "source": "headers",
                "key": "x-akamai-transformed",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "ak_bmsc",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"\.akamaized\.net/|\.akamaihd\.net/"
            }
        ]
    },
    {
        "name": "Amazon CloudFront",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "via",
                "pattern": r"\bcloudfront\.net\b"
            },
            {
                "source": "headers",
                "key": "x-amz-cf-id",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-amz-cf-pop",
                "pattern": r"^[A-Z]{3}\d+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"\.cloudfront\.net/"
            }
        ]
    },
    {
        "name": "Bunny CDN",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"\bBunnyCDN\b"
            },
            {
                "source": "headers",
                "key": "cdn-pullzone",
                "pattern": r"^\d+$"
            },
            {
                "source": "headers",
                "key": "cdn-uid",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"\.b-cdn\.net/"
            }
        ]
    },
    {
        "name": "Varnish",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "x-varnish",
                "pattern": r"^\d+(?:\s+\d+)?$"
            },
            {
                "source": "headers",
                "key": "via",
                "pattern": r"\bvarnish\b"
            },
            {
                "source": "headers",
                "key": "x-varnish-cache",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Vercel",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"^Vercel$"
            },
            {
                "source": "headers",
                "key": "x-vercel-id",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-vercel-cache",
                "pattern": r"^(?:HIT|MISS|STALE|PRERENDER|BYPASS|REVALIDATED)$"
            }
        ]
    },
    {
        "name": "Netlify",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"^Netlify$"
            },
            {
                "source": "headers",
                "key": "x-nf-request-id",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "AWS",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"\bAmazonS3\b|\bawselb(?:/[\d.]+)?\b"
            },
            {
                "source": "headers",
                "key": "x-amz-request-id",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "AWSALB",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"\.s3(?:[.-][a-z0-9-]+)?\.amazonaws\.com/"
            }
        ]
    },
    {
        "name": "Google Cloud Platform",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"^Google Frontend$"
            },
            {
                "source": "headers",
                "key": "via",
                "pattern": r"\b1\.1 google\b"
            },
            {
                "source": "headers",
                "key": "x-goog-generation",
                "pattern": r"^\d+$"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"storage\.googleapis\.com/"
            }
        ]
    },
    {
        "name": "Microsoft Azure",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "x-azure-ref",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "ARRAffinity",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"\.(?:azureedge\.net|blob\.core\.windows\.net)/"
            }
        ]
    },
    {
        "name": "Heroku",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "via",
                "pattern": r"\bvegur\b"
            },
            {
                "source": "headers",
                "key": "nel",
                "pattern": r"heroku-nel"
            }
        ]
    },
    {
        "name": "Nginx",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"\bnginx(?:/[\d.]+)?\b"
            }
        ]
    },
    {
        "name": "Apache",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"\bApache(?!-Coyote)(?:/[\d.]+)?\b"
            },
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bApache(?!-Coyote)(?:/[\d.]+)?\b"
            }
        ]
    },
    {
        "name": "LiteSpeed",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"\bLiteSpeed\b"
            },
            {
                "source": "headers",
                "key": "x-litespeed-cache",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-litespeed-tag",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Caddy",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "server",
                "pattern": r"\bCaddy\b"
            },
            {
                "source": "headers",
                "key": "via",
                "pattern": r"\bCaddy\b"
            }
        ]
    },
    {
        "name": "WP Rocket",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "x-rocket-nginx-serving-static",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/wp-rocket/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<!--\s*This website is like a Rocket|rocketlazyloadscript|id=[\"']wpr-usedcss[\"']"
            }
        ]
    },
    {
        "name": "NitroPack",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "x-nitro-cache",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn-[a-z0-9]+\.nitrocdn\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"nitro-telemetry-meta|nitro-lazy-src|data-nitro-marker-id"
            }
        ]
    },
    {
        "name": "Cloudflare Zaraz",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/cdn-cgi/zaraz/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/cdn-cgi/zaraz/s\.js|zaraz\.track\("
            }
        ]
    },
    {
        "name": "Google PageSpeed",
        "categories": ["Performance / Infrastructure"],
        "rules": [
            {
                "source": "headers",
                "key": "x-mod-pagespeed",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-page-speed",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"pagespeed\.ic\.|data-pagespeed-(?:url-hash|no-defer|lazy-src)"
            }
        ]
    }
]