import re
from src.models import ProcessedResponse, Proof, DetectedTech, DomainResult
from src.tech_rules import TECH_RULES


def detect_tech(responses: list[ProcessedResponse]) -> list[DomainResult]:
    results = []
    for response in responses:
        if response.error is not None:
            results.append(DomainResult(domain=response.domain,
                                        status="failed",
                                        error=response.error))
            continue
        detected_techs = []
        for tech in TECH_RULES:
            proofs = []
            for rule in tech["rules"]:
                source = rule["source"]
                key = rule["key"]
                pattern = rule["pattern"]

                value = getattr(response, source).get(key)

                if value is not None:
                    match = re.search(pattern, value)
                    if match:
                        proofs.append(Proof(
                            source=source,
                            matched_value=value,
                            pattern=pattern,
                            key=key
                        ))

            if proofs:
                detected_techs.append(DetectedTech(
                    name=tech["name"],
                    categories=tech["categories"],
                    proofs=proofs
                ))

        results.append(DomainResult(domain=response.domain,
                                    status="success",
                                    technologies=detected_techs,
                                    error=None))

    return results


