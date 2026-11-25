import re
from src.models import PageSignals, Proof, DetectedTech, DomainResult
from src.tech_rules import TECH_RULES


def detect_tech(signals: PageSignals) -> DomainResult:
    for tech in TECH_RULES:
        print(tech["name"])
        for rule in tech["rules"]:
            source = rule["source"]
            key = rule["key"]
            pattern = rule["pattern"]
            value = getattr(signals, source).get(key)
            if value is not None:
                match = re.search(pattern, value)
                if match:
                    print("Technology detected!")
                    print("Matched value:", match.group())
                print(match)
                
    return


mock_signals = PageSignals(domain="example.com",
                           headers={"server": "nginx/1.24.0"},
                           cookies={},
                           script_srcs=[],
                           meta_tags={},
                           html="")

result = detect_tech(mock_signals)
print(result)

