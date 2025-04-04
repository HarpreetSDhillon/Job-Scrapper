from pydantic import BaseModel
from .job_post import JobPost

class JobResponse(BaseModel):
    jobs: list[JobPost] = []