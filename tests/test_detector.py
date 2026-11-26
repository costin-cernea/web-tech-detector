from src.models import ProcessedResponse
from src.detector import detect_tech

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