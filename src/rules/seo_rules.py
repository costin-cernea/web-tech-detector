TECH_RULES = [
    {
        "name": "Google Search Console",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "google-site-verification",
                "pattern": r"^[a-z0-9_-]{20,}$"
            }
        ]
    },
    {
        "name": "Bing Webmaster Tools",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "msvalidate.01",
                "pattern": r"^[a-f0-9]{32}$"
            }
        ]
    },
    {
        "name": "Yandex Webmaster",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "yandex-verification",
                "pattern": r"^[a-f0-9]{16,}$"
            }
        ]
    },
    {
        "name": "Ahrefs",
        "categories": ["SEO", "Analytics"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "ahrefs-site-verification",
                "pattern": r"^[a-f0-9]{64}$"
            },
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
        "name": "Yoast SEO",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"<!--\s*This site is optimized with the Yoast SEO"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"']yoast-schema-graph[\"']"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/wordpress-seo(?:-premium)?/"
            }
        ]
    },
    {
        "name": "Rank Math",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"<!--\s*Search Engine Optimization by Rank Math"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"']rank-math-schema[\"']"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/seo-by-rank-math/"
            }
        ]
    },
    {
        "name": "All in One SEO",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bAll in One SEO\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<!--\s*All in One SEO"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"']aioseo-schema[\"']"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/all-in-one-seo-pack(?:-pro)?/"
            }
        ]
    },
    {
        "name": "SEOPress",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/wp-seopress(?:-pro)?/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/wp-content/plugins/wp-seopress(?:-pro)?/|seopress-breadcrumbs"
            }
        ]
    },
    {
        "name": "The SEO Framework",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"<!--\s*The SEO Framework by Sybre Waaijer"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/autodescription/"
            }
        ]
    },
    {
        "name": "SmartCrawl",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/(?:smartcrawl-seo|wpmu-dev-seo)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"']wds-schema-graph[\"']|<!--\s*SmartCrawl"
            }
        ]
    },
    {
        "name": "Schema Pro",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/wp-schema-pro/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"aiosrs-schema|wp-schema-pro"
            }
        ]
    },
    {
        "name": "Schema App",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.schemaapp\.com/javascript/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.schemaapp\.com/javascript/|window\.schema_highlighter"
            }
        ]
    },
    {
        "name": "SEOmatic",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bSEOmatic\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<!--\s*Generated by SEOmatic"
            }
        ]
    },
    {
        "name": "Schema.org (JSON-LD)",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"<script\b[^>]*type=[\"']application/ld\+json[\"'][^>]*>"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"\"@context\"\s*:\s*\"https?://schema\.org/?\""
            }
        ]
    },
    {
        "name": "Open Graph",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "og:title",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<meta\b[^>]*property=[\"']og:(?:title|type|url|image)[\"']"
            }
        ]
    },
    {
        "name": "Twitter Cards",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "twitter:card",
                "pattern": r"^(?:summary|summary_large_image|app|player)$"
            },
            {
                "source": "meta_tags",
                "key": "twitter:site",
                "pattern": r"^@?[a-z0-9_]+$"
            }
        ]
    },
    {
        "name": "AMP",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.ampproject\.org/v0\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<link\b[^>]*rel=[\"']amphtml[\"']"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<html\b[^>]*\s(?:amp|⚡)(?:\s|>)"
            }
        ]
    },
    {
        "name": "Prerender.io",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "headers",
                "key": "x-prerender-requestid",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-prerender-cache",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-prerender",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Rendertron",
        "categories": ["SEO"],
        "rules": [
            {
                "source": "headers",
                "key": "x-renderer",
                "pattern": r"\brendertron\b"
            },
            {
                "source": "headers",
                "key": "x-rendertron-cached",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Siteimprove",
        "categories": ["SEO", "Analytics"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"siteimproveanalytics\.com/js/siteanalyze_"
            },
            {
                "source": "cookies",
                "key": "nmstat",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"siteimproveanalytics\.com/js/siteanalyze_"
            }
        ]
    }
]