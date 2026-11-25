import re
from src.models import ProcessedResponse, Proof, DetectedTech, DomainResult
from src.tech_rules import TECH_RULES


def detect_tech(signals: ProcessedResponse) -> DomainResult:
    detected_techs = []
    for tech in TECH_RULES:
        proofs = []
        for rule in tech["rules"]:
            source = rule["source"]
            key = rule["key"]
            pattern = rule["pattern"]
            value = getattr(signals, source).get(key)
            if value is not None:
                match = re.search(pattern, value)
                if match:
                    print("Technology detected!")
                    proofs.append(Proof(source=source,
                                        matched_value=value,
                                        pattern=pattern,
                                        key=key))
        if proofs:
            detected_techs.append(DetectedTech(name=tech["name"], categories=tech["categories"], proofs=proofs))

    return DomainResult(domain=signals.domain, detected_techs=detected_techs)


mock_signals = ProcessedResponse(domain="example.com",
                           headers={"server": "nginx/1.24.0"},
                           cookies={},
                           script_srcs=[],
                           meta_tags={},
                           html="")

result = detect_tech(mock_signals)
print(result)

