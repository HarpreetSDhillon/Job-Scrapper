import os
from dotenv import load_dotenv

class LinkedInConfig:
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
        load_dotenv(dotenv_path=dotenv_path)

        self.LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
        self.LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")