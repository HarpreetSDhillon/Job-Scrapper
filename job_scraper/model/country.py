from enum import Enum

class Country(Enum):
    AUSTRALIA = ("australia", "au", "com.au")
    CANADA = ("canada", "ca", "ca")
    USA = ("usa,us,united states", "www:us", "com")
    INDIA = ("india", "in", "co.in")
    UK = ("uk,united kingdom", "uk:gb", "co.uk")
    NORTH_AMERICA = ("usa/ca", "www")
    WORLDWIDE = ("worldwide", "www")
    # Add other countries here...

    @property
    def indeed_domain_value(self):
        subdomain, _, api_country_code = self.value[1].partition(":")
        return (subdomain, api_country_code.upper()) if api_country_code else (self.value[1], self.value[1].upper())

    @property
    def glassdoor_domain_value(self):
        if len(self.value) == 3:
            subdomain, _, domain = self.value[2].partition(":")
            return f"{subdomain}.glassdoor.{domain}" if domain else f"www.glassdoor.{self.value[2]}"
        raise Exception(f"Glassdoor is not available for {self.name}")

    def get_glassdoor_url(self):
        return f"https://{self.glassdoor_domain_value}/"

    @classmethod
    def from_string(cls, country_str: str):
        country_str = country_str.strip().lower()
        for country in cls:
            if country_str in country.value[0].split(","):
                return country
        raise ValueError(f"Invalid country string: '{country_str}'.")