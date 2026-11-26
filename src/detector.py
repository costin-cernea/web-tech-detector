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
                source_data = getattr(response, source)
                if isinstance(source_data, dict):
                    value = source_data.get(key)
                    if isinstance(value, list):
                        for item in value:
                            match = re.search(pattern, item)
                            if match:
                                proofs.append(Proof(
                                    source=source,
                                    matched_value=item,
                                    pattern=pattern,
                                    key=key
                                ))
        
                    elif value is not None:
                        match = re.search(pattern, value)
                        if match:
                            proofs.append(Proof(
                                source=source,
                                matched_value=value,
                                pattern=pattern,
                                key=key
                            ))
                elif isinstance(source_data, list):
                    for value in source_data:
                        match = re.search(pattern, value)
                        if match:
                            proofs.append(Proof(
                                source=source,
                                matched_value=value,
                                pattern=pattern,
                            ))

                elif isinstance(source_data, str):
                    match= re.search(pattern, source_data)
                    if match:
                         proofs.append(Proof(
                            source=source,
                            matched_value=match.group(),
                            pattern=pattern,
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


