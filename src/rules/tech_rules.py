from src.rules.ecommerce_rules import TECH_RULES as ECOMMERCE_RULES
from src.rules.cms_rules import TECH_RULES as CMS_RULES
from src.rules.analytics_rules import TECH_RULES as ANALYTICS_RULES
from src.rules.payment_rules import TECH_RULES as PAYMENT_RULES
from src.rules.marketing_rules import TECH_RULES as MARKETING_RULES
from src.rules.customer_support_rules import TECH_RULES as CUSTOMER_SUPPORT_RULES
from src.rules.performance_rules import TECH_RULES as PERFORMANCE_RULES
from src.rules.seo_rules import TECH_RULES as SEO_RULES


TECH_RULES = (
    ECOMMERCE_RULES
    + CMS_RULES
    + ANALYTICS_RULES
    + PAYMENT_RULES
    + MARKETING_RULES
    + CUSTOMER_SUPPORT_RULES
    + PERFORMANCE_RULES
    + SEO_RULES
)