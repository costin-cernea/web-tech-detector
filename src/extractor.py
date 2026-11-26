from bs4 import BeautifulSoup
from src.models import RawResponse, ProcessedResponse


def extract_signals(responses: list[RawResponse]) -> list[ProcessedResponse]:
    results = []
    for response in responses:
        if response.error is not None:
            results.append(ProcessedResponse(domain=response.domain,
                                             headers={},
                                             cookies={},
                                             script_srcs=[],
                                             meta_tags={},
                                             html="",
                                             error=response.error))
            continue
        soup = BeautifulSoup(response.html, "html.parser")
        scripts = soup.find_all("script")
        metas = soup.find_all("meta")
        meta_tags = {}

        for meta in metas:
            name = meta.get("name") or meta.get("property")
            content = meta.get("content")

            if name and content:
                key = name.strip().lower()
                value = content.strip()
                meta_tags.setdefault(key, []).append(value)

        results.append(ProcessedResponse(domain=response.domain, 
                                   headers={key.lower(): value for key, value in response.headers.items()}, 
                                   cookies=response.cookies,
                                   script_srcs=[script.get("src") for script in scripts if script.get("src")],
                                   meta_tags=meta_tags,
                                   html=response.html,
                                   error=None))
    return results
