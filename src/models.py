from dataclasses import dataclass, field

@dataclass
class RawResponse:
    domain: str
    final_url: str
    status_code: int | None = None
    headers: dict[str, str] = field(default_factory=dict)
    cookies: dict[str, str] = field(default_factory=dict)
    html: str = ""
    fetch_method: str = "http"
    error: str | None = None


@dataclass
class PageSignals:
    domain: str
    headers: dict[str, str]
    cookies: dict[str, str]
    script_srcs: list[str]
    meta_tags: dict[str, str]
    html: str



@dataclass
class Proof:
    source: str
    matched_value: str
    pattern: str
    key: str | None = None

@dataclass
class DetectedTech:
    name: str
    categories: list[str]
    proofs: list[Proof]

@dataclass
class DomainResult:
    domain: str
    status: str
    technologies: list[DetectedTech] = field(default_factory=list)
    error: str | None = None
