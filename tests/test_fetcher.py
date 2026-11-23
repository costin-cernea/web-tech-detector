from src.fetcher import fetch_domain_response, process_domains

response = fetch_domain_response("google.com")
response2 = fetch_domain_response("example.com")

print(response)
print(type(response))
print(response2)
print(type(response2))

results = process_domains("data/part-00000-66e0628d-2c7f-425a-8f5b-738bcd6bf198-c000.snappy.parquet")
print(f"Number of results: {len(results)}")

for result in results:
    if result.error is not None:
        print(f"FAILED: {result.domain} | {result.error}")
    else:
        print(f"SUCCESS: {result.domain} | Full url: {result.final_url} | Status: {result.status_code}")