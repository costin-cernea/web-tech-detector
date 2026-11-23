from src.models import RawResponse
from src.extractor import extract_signals

html = """
<html>
<head>
    <meta name="generator" content="WordPress 6.5">
    <meta name="generator" content="Elementor 3.20">
    <meta name="description" content="My test website">
    <meta property="og:site_name" content="Test Website">

    <script src="/js/app.js"></script>
    <script src="/js/vendor.js"></script>
    <script></script>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
"""

response = RawResponse(
    domain="example.com",
    final_url="https://example.com",
    status_code=200,
    headers={"Content-Type": "text/html"},
    cookies={},
    html=html
)

failed_response = RawResponse(
    domain="failed-example.com",
    error="Connection timed out"
)

results = extract_signals([response])
results_failed = extract_signals([failed_response])

print("Results:", results)
print("Type:", type(results))


print(results[0])

print("Results Failed:", results_failed)