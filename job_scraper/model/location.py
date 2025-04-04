from typing import Optional
from pydantic import BaseModel
from .country import Country

class Location(BaseModel):
    country: Country | str | None = None
    city: Optional[str] = None
    state: Optional[str] = None

    def display_location(self) -> str:
        location_parts = []
        if self.city:
            location_parts.append(self.city)
        if self.state:
            location_parts.append(self.state)
        if isinstance(self.country, str):
            location_parts.append(self.country)
        elif self.country:
            country_name = self.country.value[0].split(",")[0]
            location_parts.append(country_name.title() if country_name not in ("usa", "uk") else country_name.upper())
        return ", ".join(location_parts)