TECH_RULES = [
    {
        "name": "Shopify",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-shopid",
                "pattern": r"^\d+$"
            },
            {
                "source": "headers",
                "key": "x-sorting-hat-shopid",
                "pattern": r"^\d+$"
            },
            {
                "source": "headers",
                "key": "x-shopify-stage",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "powered-by",
                "pattern": r"shopify"
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
                "source": "cookies",
                "key": "shopify_pay_redirect",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "shopify-checkout-api-token",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "shopify-digital-wallet",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.shopify\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/shopifycloud/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Shopify\.theme\s*="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.Shopify\s*="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"id=[\"']shopify-section-"
            }
        ]
    },
    {
        "name": "WooCommerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "cookies",
                "key": "woocommerce_cart_hash",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "woocommerce_items_in_cart",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "woocommerce_recently_viewed",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bwoocommerce\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/woocommerce/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"woocommerce(?:\.min)?\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/wp-content/plugins/woocommerce/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"wc_add_to_cart_params"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bwoocommerce-no-js\b"
            }
        ]
    },
    {
        "name": "Magento",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-magento-vary",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-magento-cache-debug",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-magento-tags",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-magento-cache-control",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "mage-cache-sessid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "mage-messages",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "mage-translation-storage",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/static/version\d+/frontend/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/mage/requirejs/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/js/mage/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"text/x-magento-init"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-mage-init="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Mage\.Cookies\.path"
            }
        ]
    },
    {
        "name": "Adobe Commerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"Magento_(?:B2b|Reward|CustomerBalance|GiftCardAccount|Banner|QuickOrder|RequisitionList|Company|GiftRegistry)/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"storefront-events-collector"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Magento_(?:B2b|Reward|CustomerBalance|GiftCardAccount|Banner|QuickOrder|RequisitionList|Company|GiftRegistry)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Magento_LiveSearch/"
            }
        ]
    },
    {
        "name": "BigCommerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-bc-storefront-type",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-bc-edge-cache-status",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-bc-cache-status",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "SHOP_SESSION_TOKEN",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "fornax_anonymousId",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "STORE_VISITOR",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "SHOP_TOKEN",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\d+\.bigcommerce\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"microapps\.bigcommerce\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"checkout-sdk\.bigcommerce\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\d+\.bigcommerce\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.BCData\s*="
            }
        ]
    },
    {
        "name": "PrestaShop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "powered-by",
                "pattern": r"prestashop"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bprestashop\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/modules/ps_"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"var\s+prestashop\s*="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/modules/ps_shoppingcart/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"prestashop\.emit\("
            }
        ]
    },
    {
        "name": "OpenCart",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "cookies",
                "key": "OCSESSID",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"catalog/view/javascript/common\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"catalog/view/javascript/opencart"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"catalog/view/theme/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"index\.php\?route=(?:product|checkout/cart|common/home)"
            }
        ]
    },
    {
        "name": "Wix eCommerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.parastorage\.com/services/(?:wix-ecommerce|ecom-|stores-)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"static\.parastorage\.com/services/(?:wix-ecommerce|ecom-|stores-)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"\"appDefinitionName\"\s*:\s*\"Wix Stores\""
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-hook=[\"']product-page-root[\"']"
            }
        ]
    },
    {
        "name": "Squarespace Commerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"assets\.squarespace\.com/universal/scripts-compressed/commerce-"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Squarespace\.Commerce"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bsqs-add-to-cart-button\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"\"commerceSettings\"\s*:"
            }
        ]
    },
    {
        "name": "Webflow Ecommerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"data-wf-commerce-"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"w-commerce-commercecartwrapper"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"w-commerce-commerceaddtocartbutton"
            }
        ]
    },
    {
        "name": "Square Online",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\d*\.editmysite\.com/js/site/commerce"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bwsite-com-(?:product|store)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\d*\.editmysite\.com/js/site/commerce"
            }
        ]
    },
    {
        "name": "Salesforce Commerce Cloud",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-dw-request-base-id",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "dwsid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "cqcid",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "dw_dnt",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/on/demandware\.static/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"demandware\.edgesuite\.net"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cquotient\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/on/demandware\.(?:store|static)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"demandware\.edgesuite\.net"
            }
        ]
    },
    {
        "name": "Shopware",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "sw-context-token",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-shopware-cache-id",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "sw-states",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "sw-currency",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "sw-cache-hash",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bshopware\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/bundles/storefront/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/bundles/storefront/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bsw-cms-"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"frontend\.checkout\.cart"
            }
        ]
    },
    {
        "name": "commercetools",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"commercetools\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"frontastic\.(?:io|cloud)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:api|auth)\.[a-z0-9-]+\.commercetools\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"frontastic\.(?:io|cloud)"
            }
        ]
    },
    {
        "name": "Ecwid",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"app\.ecwid\.com/script\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"app\.shopsettings\.com/script\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"xProductBrowser\("
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Ecwid\.init\("
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"app\.ecwid\.com/script\.js"
            }
        ]
    },
    {
        "name": "Lightspeed eCom",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\blightspeed\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.webshopapp\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.shoplightspeed\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"assets\.webshopapp\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.(?:webshopapp|shoplightspeed)\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"webshopapp\.com/shops/"
            }
        ]
    },
    {
        "name": "VTEX",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-vtex-janus-router-backend-app",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-vtex-io-cluster-id",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "powered-by",
                "pattern": r"\bvtex\b"
            },
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bvtex\b"
            },
            {
                "source": "cookies",
                "key": "vtex_segment",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "vtex_session",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "VtexWorkspace",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"vtexassets\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"vteximg\.com\.br"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"io\.vtex\.com\.br"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"vtexassets\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"vteximg\.com\.br"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"vtex-store-components"
            }
        ]
    },
    {
        "name": "SAP Commerce Cloud",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "cookies",
                "key": "acceleratorSecureGUID",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/_ui/(?:responsive|desktop)/common/js/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"acc\.(?:minicart|product|checkout)\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/_ui/(?:responsive|desktop)/common/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/_ui/addons/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"ACC\.config\s*="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<cx-storefront\b"
            }
        ]
    },
    {
        "name": "Oracle Commerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/ccstoreui/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/ccstore/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/occ-static/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/ccstore(?:ui)?/v1/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"atg/commerce/"
            }
        ]
    },
    {
        "name": "HCL Commerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "cookies",
                "key": "WC_SESSION_ESTABLISHED",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "WC_PERSISTENT",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "WC_ACTIVEPOINTER",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wcsstore/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/wcsstore/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/webapp/wcs/stores/servlet/"
            }
        ]
    },
    {
        "name": "Drupal Commerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/modules/contrib/commerce/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/sites/all/modules/commerce/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"commerce_(?:cart|checkout)\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/modules/contrib/commerce/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"commerce-order-item-add-to-cart-form"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"commerce-cart-block"
            }
        ]
    },
    {
        "name": "Ubercart",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/modules/(?:contrib/)?ubercart/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"uc_cart\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"uc-product-add-to-cart"
            }
        ]
    },
    {
        "name": "Shift4Shop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"(?:3dcart|shift4shop)"
            },
            {
                "source": "cookies",
                "key": "3dvisit",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/assets/templates/common-(?:core|html5)/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:3dcart|shift4shop)\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/assets/templates/common-(?:core|html5)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"3dcartstores\.com"
            }
        ]
    },
    {
        "name": "Volusion",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/a/j/javascripts\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/v/vspfiles/templates/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/v/vspfiles/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"productdetails\.asp\?productcode="
            }
        ]
    },
    {
        "name": "X-Cart",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"x-cart"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bx-cart\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"powered by\s+x-cart"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"xcart_catalog"
            }
        ]
    },
    {
        "name": "CS-Cart",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bcs-cart\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/js/tygh/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/js/tygh/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"tygh_main_container"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bty-cart-content\b"
            }
        ]
    },
    {
        "name": "Zen Cart",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "cookies",
                "key": "zenid",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bzen\s*cart\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"index\.php\?main_page=(?:product_info|shopping_cart)"
            }
        ]
    },
    {
        "name": "osCommerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "cookies",
                "key": "osCsid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"osCsid=[a-z0-9]+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"product_info\.php\?products_id="
            }
        ]
    },
    {
        "name": "nopCommerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"nopcommerce"
            },
            {
                "source": "cookies",
                "key": ".Nop.Customer",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": ".Nop.Antiforgery",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": ".Nop.Session",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bnopcommerce\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"public\.ajaxcart\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"powered by\s+nopcommerce"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"AjaxCart\.init\("
            }
        ]
    },
    {
        "name": "Odoo eCommerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/website_sale/static/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/website_sale/static/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\boe_website_sale\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bjs_add_cart_json\b"
            }
        ]
    },
    {
        "name": "Shopline",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-shopline-request-id",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:cdn|static|img)\.shoplineapp\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.myshopline\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.(?:shoplineapp|myshopline)\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.SL_State\s*="
            }
        ]
    },
    {
        "name": "Shoplazza",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:cdn|assets|static)\.shoplazza\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.shoplazza\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.SHOPLAZZA"
            }
        ]
    },
    {
        "name": "ShopBase",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.shopbase\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.shopbase\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.__SHOPBASE__"
            }
        ]
    },
    {
        "name": "Shoper",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"dcsaas\.net"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"shoper\.pl"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/skins/user/rwd_shoper_"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"dcsaas\.net"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/skins/user/rwd_shoper_"
            }
        ]
    },
    {
        "name": "Shoptet",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-shoptet-cache",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"shoptet"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.myshoptet\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.myshoptet\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.shoptet\s*="
            }
        ]
    },
    {
        "name": "IdoSell",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"idosell"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:idosell|iai-shop)\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"iai_product"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.idosell\.com"
            }
        ]
    },
    {
        "name": "Cafe24",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "cookies",
                "key": "ECSESSID",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "EC_ASYNC_CACHE",
                "pattern": r".+"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:ec-img|m-img|img\.echosting)\.cafe24\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cafe24\.com/ind-script/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"echosting\.cafe24\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"EC_FRONT_EXTERNAL_SCRIPT"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"xans-element-\s+xans-product"
            }
        ]
    },
    {
        "name": "Imweb",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.imweb\.me"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.imweb\.me"
            }
        ]
    },
    {
        "name": "Gomag",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"gomagcdn\.ro"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"gomag\.ro"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"gomagcdn\.ro"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"__gomag"
            }
        ]
    },
    {
        "name": "MerchantPro",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"s\d*\.cdnmpro\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"merchantpro\.(?:ro|com)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"s\d*\.cdnmpro\.com"
            }
        ]
    },
    {
        "name": "CloudCart",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"cloudcart"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdncloudcart\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdncloudcart\.com"
            }
        ]
    },
    {
        "name": "Shoprenter",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.shoprenter\.hu"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"shoprenter\.hu"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.shoprenter\.hu"
            }
        ]
    },
    {
        "name": "UNAS",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"unas\.hu"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"shop\.unas\.hu/shop_ordered/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"unas_page"
            }
        ]
    },
    {
        "name": "Tiendanube / Nuvemshop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:acdn|dcdn)\.mitiendanube\.com"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"d26lpennugtm8s\.cloudfront\.net"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:tiendanube\.com|nuvemshop\.com\.br)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:acdn|dcdn)\.mitiendanube\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"LS\.store\s*="
            }
        ]
    },
    {
        "name": "Mercado Shops",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"http2\.mlstatic\.com/frontend-assets/mshops-"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"mercadoshops\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"http2\.mlstatic\.com/frontend-assets/mshops-"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"mshops-frontend"
            }
        ]
    },
    {
        "name": "Tray",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"images\.tcdn\.com\.br"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"images\.tcdn\.com\.br"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-tray-tst="
            }
        ]
    },
    {
        "name": "Loja Integrada",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.awsli\.com\.br"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.awsli\.com\.br"
            }
        ]
    },
    {
        "name": "Salla",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-salla-theme",
                "pattern": r".+"
            },
            {
                "source": "headers",
                "key": "x-powered-by",
                "pattern": r"\bsalla\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.(?:assets\.)?salla\.(?:network|sa)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.(?:assets\.)?salla\.(?:network|sa)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<salla-products-list\b"
            }
        ]
    },
    {
        "name": "Zid",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:media|assets)\.zid\.store"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:media|assets)\.zid\.store"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"window\.zid\s*="
            }
        ]
    },
    {
        "name": "EasyStore",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.easystore\.co"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.easystore\.co"
            }
        ]
    },
    {
        "name": "Haravan",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:theme|product|file)\.hstatic\.net"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:theme|product)\.hstatic\.net"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Haravan\.shop"
            }
        ]
    },
    {
        "name": "Sapo",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"bizweb\.dktcdn\.net"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"bizweb\.dktcdn\.net"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Bizweb\.store"
            }
        ]
    },
    {
        "name": "BASE",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"baseec-img-mng\.akamaized\.net"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"thebase\.in"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"baseec-img-mng\.akamaized\.net"
            }
        ]
    },
    {
        "name": "MakeShop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"makeshop\.(?:jp|co\.kr)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"shop\d+\.makeshop\.jp"
            }
        ]
    },
    {
        "name": "Color Me Shop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"img\d+\.shop-pro\.jp"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"img\d+\.shop-pro\.jp"
            }
        ]
    },
    {
        "name": "Big Cartel",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:assets|cache)\.bigcartel\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"(?:assets|cache)\.bigcartel\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"bigcartel\.com/api/"
            }
        ]
    },
    {
        "name": "OXID eShop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\boxid\s+eshop\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/out/(?:flow|wave|apex)/src/js/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/out/(?:flow|wave|apex)/src/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cl=details&(?:amp;)?anid="
            }
        ]
    },
    {
        "name": "JTL-Shop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "cookies",
                "key": "JTLSHOP",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bjtl-shop\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"jtl\.evo\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/templates/(?:NOVA|Evo)/js/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"name=[\"']jtl_token[\"']"
            }
        ]
    },
    {
        "name": "Gambio",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/GXModules/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/templates/(?:Honeygrid|Malibu)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/GXModules/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-gx-widget="
            }
        ]
    },
    {
        "name": "xt:Commerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\bxt:commerce\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"powered by\s+xt:commerce"
            }
        ]
    },
    {
        "name": "Spryker",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "headers",
                "key": "x-spryker-version",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"js-spryker-"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"spryker-shop"
            }
        ]
    },
    {
        "name": "Miva Merchant",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/mm5/clientside\.mvc"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/mm5/merchant\.mvc"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/mm5/graphics/"
            }
        ]
    },
    {
        "name": "NetSuite SuiteCommerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"netsuite\.com/core/media/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/sca-dev-[^/]+/javascript/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"SC\.ENVIRONMENT\s*="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/scs/extensions/"
            }
        ]
    },
    {
        "name": "Intershop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/INTERSHOP/static/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/INTERSHOP/(?:web|static)/"
            }
        ]
    },
    {
        "name": "Optimizely Configured Commerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"insite\.(?:core|cart)\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bisc-(?:add-to-cart|product-)"
            }
        ]
    },
    {
        "name": "Spree Commerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"spree/frontend/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Spree\.routes\s*="
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-hook=[\"'](?:product_show|cart_container)[\"']"
            }
        ]
    },
    {
        "name": "Medusa",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "cookies",
                "key": "_medusa_cart_id",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_medusa_jwt",
                "pattern": r".+"
            },
            {
                "source": "cookies",
                "key": "_medusa_cache_id",
                "pattern": r".+"
            }
        ]
    },
    {
        "name": "Sylius",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/bundles/syliusshop/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/bundles/syliusshop/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"id=[\"']sylius-cart-button[\"']"
            }
        ]
    },
    {
        "name": "Saleor",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"saleor\.cloud/graphql"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"saleor-storefront"
            }
        ]
    },
    {
        "name": "Craft Commerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "html",
                "key": None,
                "pattern": r"name=[\"']action[\"'][^>]*value=[\"']commerce/cart/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"value=[\"']commerce/cart/update-cart[\"']"
            }
        ]
    },
    {
        "name": "OroCommerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/bundles/oro(?:commerce|shoppinglist)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/bundles/oro(?:commerce|shoppinglist)/"
            }
        ]
    },
    {
        "name": "Kibo Commerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:mozu|kibocommerce)\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-mz-(?:product|cart|action)="
            }
        ]
    },
    {
        "name": "Maropost Commerce Cloud",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"netostatic\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"netostatic\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-neto-"
            }
        ]
    },
    {
        "name": "Centra",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"centracdn\.net"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"centracdn\.net"
            }
        ]
    },
    {
        "name": "Abicart",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"shop\.textalk\.se"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"shop\.textalk\.se"
            }
        ]
    },
    {
        "name": "CCV Shop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"ccvshop\.(?:nl|com)"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-ccvshop"
            }
        ]
    },
    {
        "name": "Mijnwebwinkel",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.myonlinestore\.eu"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.myonlinestore\.eu"
            }
        ]
    },
    {
        "name": "VirtueMart",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/components/com_virtuemart/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"vm(?:prices|site)\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/components/com_virtuemart/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"virtuemart_product_id"
            }
        ]
    },
    {
        "name": "HikaShop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/media/com_hikashop/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"hikashop\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/media/com_hikashop/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"hikashop_(?:product|cart)"
            }
        ]
    },
    {
        "name": "Easy Digital Downloads",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "cookies",
                "key": "edd_items_in_cart",
                "pattern": r".+"
            },
            {
                "source": "meta_tags",
                "key": "generator",
                "pattern": r"\beasy\s+digital\s+downloads\b"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/easy-digital-downloads/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"edd-ajax(?:\.min)?\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/wp-content/plugins/easy-digital-downloads/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bedd-add-to-cart\b"
            }
        ]
    },
    {
        "name": "SureCart",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wp-content/plugins/surecart/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jsdelivr\.net/npm/@surecart/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/wp-content/plugins/surecart/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<sc-cart-icon\b"
            }
        ]
    },
    {
        "name": "Snipcart",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.snipcart\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.snipcart\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bsnipcart-add-item\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"id=[\"']snipcart[\"']"
            }
        ]
    },
    {
        "name": "Foxy.io",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.foxycart\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.foxycart\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"foxycart\.com/cart"
            }
        ]
    },
    {
        "name": "Swell",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.swell\.store"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.swell\.store"
            }
        ]
    },
    {
        "name": "Gumroad",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"gumroad\.com/js/gumroad(?:-embed)?\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"gumroad\.com/js/gumroad(?:-embed)?\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bgumroad-button\b"
            }
        ]
    },
    {
        "name": "Sellfy",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sellfy\.com/js/api_buttons\.js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.sellfy\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.sellfy\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bsellfy-buy-button\b"
            }
        ]
    },
    {
        "name": "Payhip",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"payhip\.com/(?:payhip|embed-page)\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"payhip\.com/(?:payhip|embed-page)\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"class=[\"'][^\"']*\bpayhip-buy-button\b"
            }
        ]
    },
    {
        "name": "Fourthwall",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.fourthwall\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"cdn\.fourthwall\.com"
            }
        ]
    },
    {
        "name": "EKM",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"ekmpowershop"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"ekmpowershop"
            }
        ]
    },
    {
        "name": "Shop-Script",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/wa-apps/shop/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/wa-(?:apps|data/public)/shop/"
            }
        ]
    },
    {
        "name": "InSales",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.insales-cdn\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"static\.insales-cdn\.com"
            }
        ]
    },
    {
        "name": "AmeriCommerce",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"/store/inc/clientapi/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"/store/inc/clientapi/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"AC\.cart\b"
            }
        ]
    },
    {
        "name": "Ueeshop",
        "categories": ["Ecommerce"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"ueeshop\.com"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"ueeshop_config"
            }
        ]
    }
]

