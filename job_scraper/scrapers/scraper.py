
from abc import ABC, abstractmethod
from ..job_response import JobResponse
from ..scraper_input import ScraperInput

class Scraper(ABC):
    def __init__(
        self, site: Site, proxies: list[str] | None = None, ca_cert: str | None = None
    ):
        self.site = site
        self.proxies = proxies
        self.ca_cert = ca_cert

    @abstractmethod
    def scrape(self, scraper_input: ScraperInput) -> JobResponse: ...
