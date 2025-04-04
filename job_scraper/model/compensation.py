from typing import Optional
from enum import Enum
from pydantic import BaseModel

class CompensationInterval(Enum):
    YEARLY = "yearly"
    MONTHLY = "monthly"
    WEEKLY = "weekly"
    DAILY = "daily"
    HOURLY = "hourly"

    @classmethod
    def get_interval(cls, pay_period):
        interval_mapping = {"YEAR": cls.YEARLY, "HOUR": cls.HOURLY}
        return interval_mapping.get(pay_period, cls[pay_period].value if pay_period in cls.__members__ else None)

class Compensation(BaseModel):
    interval: Optional[CompensationInterval] = None
    min_amount: float | None = None
    max_amount: float | None = None
    currency: Optional[str] = "USD"