import os
from dotenv import load_dotenv

class GeneralConfig:
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
        load_dotenv(dotenv_path=dotenv_path)

        self.KEYWORDS = os.getenv("KEYWORDS", "").split(",")
        self.EXCLUDE = os.getenv("EXCLUDE", "").split(",")
        self.RESUMES_FOLDER = os.getenv("RESUMES_FOLDER", "resumes")
        self.TODOIST_API_TOKEN = os.getenv("TODOIST_API_TOKEN", "")