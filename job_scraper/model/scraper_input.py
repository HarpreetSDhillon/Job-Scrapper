from typing import Optional, List
from pydantic import BaseModel
from .country import Country
from .job_type import JobType
from .job_post import JobPost
from .compensation import CompensationInterval

class ScraperInput(BaseModel):
    site_type: List[str]
    search_term: str | None = None
    location: str | None = None
    country: Country | None = Country.USA
    distance: int | None = None
    is_remote: bool = False
    job_type: JobType | None = None
    results_wanted: int = 15