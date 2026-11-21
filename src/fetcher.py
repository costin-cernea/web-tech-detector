import pyarrow.parquet as pq
from urllib.parse import urlparse, urlunparse
import httpx
from models import RawResponse

def fetch_domain_response(domain: str) -> httpx.Response | str:
    domain = domain.strip().lower()
    if "://" not in domain:
        parsed = urlparse(f"//{domain}")
    else:
        parsed = urlparse(domain)
    # Now i need to verify if the domain uses https or http accesing the http request. First, verifying if its https and then http
    try:
        response = httpx.get(f"https://{parsed.hostname}", timeout=5, follow_redirects=True)
        return response
    except httpx.RequestError:
        try:
            response = httpx.get(f"http://{parsed.hostname}", timeout=5, follow_redirects=True)
            return response
        except httpx.RequestError as exc:
            return str(exc)


def process_domains(dataset_path: str) -> list[RawResponse]:
    table = pq.read_table(dataset_path)
    domains = table.column("root_domain").to_pylist()
    results = []
    for domain in domains:
        response = fetch_domain_response(domain)
        if isinstance(response, str):
            results.append(RawResponse(domain=domain, error=response))
            continue
        results.append(RawResponse(domain=domain, final_url=str(response.url), status_code=response.status_code,
                                   headers=dict(response.headers), cookies=dict(response.cookies), html=response.text))
    return results


test = process_domains("data/part-00000-66e0628d-2c7f-425a-8f5b-738bcd6bf198-c000.snappy.parquet")
print(test)