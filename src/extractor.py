from bs4 import BeautifulSoup
from src.models import RawResponse, PageSignals


def extract_signals(responses: list[RawResponse]) -> list[PageSignals]:
    results = []
    for response in responses:
        if response.error is not None:
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

        results.append(PageSignals(domain=response.domain, 
                                   headers={key.lower(): value for key, value in response.headers.items()}, 
                                   cookies=response.cookies,
                                   script_srcs=[script.get("src") for script in scripts if script.get("src")],
                                   meta_tags=meta_tags,
                                   html=response.html))
    return results
