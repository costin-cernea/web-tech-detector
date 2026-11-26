from src.models import ProcessedResponse
from src.detector import detect_tech
from src.reporter import convert_results_to_dict, save_results_to_json
import json

good_response = ProcessedResponse(
    domain="example.com",
    headers={"server": "nginx"},
    cookies={},
    script_srcs=[],
    meta_tags={},
    html="",
    error=None
)

broken_response = ProcessedResponse(
    domain="broken-domain.com",
    headers={},
    cookies={},
    script_srcs=[],
    meta_tags={},
    html="",
    error="Connection timed out"
)

responses = [good_response, broken_response]

results = detect_tech(responses)

for result in results:
    print(result)

print("------------------------------------------")

dict_results = convert_results_to_dict(results)
print(dict_results)

print("------------------------------------------")

save_results_to_json(results, "results.json")