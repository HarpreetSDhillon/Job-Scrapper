from typing import Optional, List
from datetime import date
from pydantic import BaseModel
from .location import Location
from .job_type import JobType
from .compensation import Compensation

class JobPost(BaseModel):
    id: str | None = None
    title: str
    company_name: str | None
    job_url: str
    job_url_direct: str | None = None
    location: Optional[Location]

    description: str | None = None
    company_url: str | None = None
    company_url_direct: str | None = None

    job_type: List[JobType] | None = None
    compensation: Compensation | None = None
    date_posted: date | None = None
    emails: List[str] | None = None
    is_remote: bool | None = None
    listing_type: str | None = None

    job_level: str | None = None
    company_industry: str | None = None
    job_function: str | None = None

    company_addresses: str | None = None
    company_num_employees: str | None = None
    company_revenue: str | None = None
    company_description: str | None = None
    company_logo: str | None = None
    banner_photo_url: str | None = None

    skills: list[str] | None = None  
    experience_range: str | None = None  
    company_rating: float | None = None 
    company_reviews_count: int | None = None 
    vacancy_count: int | None = None 
    work_from_home_type: str | None = None 