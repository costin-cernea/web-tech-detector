TECH_RULES = [
    {
        "name": "Stripe",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.stripe\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"checkout\.stripe\.com/"
            },
            {
                "source": "cookies",
                "key": "__stripe_mid",
                "pattern": r".+"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"pk_(?:live|test)_[0-9a-zA-Z]{20,}"
            }
        ]
    },
    {
        "name": "PayPal",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"paypal\.com/sdk/js"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"paypalobjects\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"data-paypal-(?:button|uid|checkout)"
            }
        ]
    },
    {
        "name": "Braintree",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.braintreegateway\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"assets\.braintreegateway\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"braintree\.(?:dropin|client)\.create"
            }
        ]
    },
    {
        "name": "Adyen",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"checkoutshopper-(?:live|test)(?:-[a-z]+)?\.adyen\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"adyen\.com/checkoutshopper/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"AdyenCheckout\(|adyen-checkout__"
            }
        ]
    },
    {
        "name": "Square",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:sandbox\.)?web\.squarecdn\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.squareup(?:sandbox)?\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"SqPaymentForm|Square\.payments\("
            }
        ]
    },
    {
        "name": "Checkout.com",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.checkout\.com/js/(?:framesv2|checkout\.js)"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"checkout-web-components\.checkout\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Frames\.init\(|CheckoutWebComponents\("
            }
        ]
    },
    {
        "name": "Authorize.Net",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js(?:test)?\.authorize\.net/v[123]/Accept"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Accept\.dispatchData\(|data-apiLoginID"
            }
        ]
    },
    {
        "name": "Worldpay",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.worldpay\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"payments\.worldpay\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Worldpay\.(?:useTemplateForm|setClientKey)\("
            }
        ]
    },
    {
        "name": "Mollie",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.mollie\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"mollie-component|Mollie\(['\"]pfl_"
            }
        ]
    },
    {
        "name": "Razorpay",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"checkout\.razorpay\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"new\s+Razorpay\(|data-razorpay-"
            }
        ]
    },
    {
        "name": "PayU",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:secure|static|checkout)\.payu\.(?:com|in|pl|ro|co|lat)/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"https?://(?:secure|checkout)\.payu\.(?:com|in|pl|ro|co|lat)/"
            }
        ]
    },
    {
        "name": "Shopify Payments",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:checkout|card-fields)\.shopifycs\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"pay\.shopify\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"shopify-payment-button|shop-pay-payment-request"
            }
        ]
    },
    {
        "name": "Amazon Pay",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static-(?:na|eu|fe)\.payments-amazon\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"payments\.amazon\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"amazon\.Pay\.renderButton|OffAmazonPayments"
            }
        ]
    },
    {
        "name": "Klarna",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"x\.klarnacdn\.net/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.klarna\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<klarna-placement\b|data-klarna-"
            }
        ]
    },
    {
        "name": "Paddle",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.paddle\.com/paddle/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Paddle\.(?:Initialize|Setup|Checkout\.open)\("
            }
        ]
    },
    {
        "name": "Affirm",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn1(?:-sandbox)?\.affirm\.com/js/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"affirm-as-low-as|affirm\.ui\.refresh\("
            }
        ]
    },
    {
        "name": "Afterpay / Clearpay",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"js\.(?:afterpay|clearpay)\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.(?:afterpay|clearpay)\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<(?:afterpay|clearpay)-placement\b|data-(?:afterpay|clearpay)-"
            }
        ]
    },
    {
        "name": "Sezzle",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:widget|checkout-sdk)\.sezzle\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"sezzle-widget|document\.sezzleConfig"
            }
        ]
    },
    {
        "name": "Zip",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"static\.zipmoney\.com\.au/|js\.quadpay\.com/|cdn\.us\.zip\.co/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"<(?:quadpay|zip)-widget\b|data-zm-merchant"
            }
        ]
    },
    {
        "name": "Alma",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"cdn\.jsdelivr\.net/npm/@alma/widgets|widgets\.getalma\.eu/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"Alma\.Widgets\.initialize|alma-payment-plans"
            }
        ]
    },
    {
        "name": "Apple Pay",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"applepay\.cdn-apple\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"ApplePaySession\.(?:canMakePayments|supportsVersion)|<apple-pay-button\b"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"-apple-pay-button-style"
            }
        ]
    },
    {
        "name": "Google Pay",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"pay\.google\.com/gp/p/js/pay\.js"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"google\.payments\.api\.PaymentsClient"
            }
        ]
    },
    {
        "name": "Samsung Pay",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"img\.mpay\.samsung\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"SamsungPay\.PaymentClient|samsungpay-button"
            }
        ]
    },
    {
        "name": "Mercado Pago",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"sdk\.mercadopago\.com/"
            },
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"secure\.mlstatic\.com/sdk/javascript/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"new\s+MercadoPago\(|Mercadopago\.setPublishableKey"
            }
        ]
    },
    {
        "name": "Alipay",
        "categories": ["Payment"],
        "rules": [
            {
                "source": "script_srcs",
                "key": None,
                "pattern": r"(?:gw|as)\.alipayobjects\.com/"
            },
            {
                "source": "html",
                "key": None,
                "pattern": r"alipay\.com/gateway\.do|AlipayJSBridge"
            }
        ]
    }
]