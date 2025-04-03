import os
from dotenv import load_dotenv

# Explicitly load the .env file
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path=dotenv_path)

KEYWORDS = os.getenv("KEYWORDS", "").split(",")
EXCLUDE = os.getenv("EXCLUDE", "").split(",")
RESUMES_FOLDER = os.getenv("RESUMES_FOLDER", "resumes")
TODOIST_API_TOKEN = os.getenv("TODOIST_API_TOKEN", "")

EXCEL_OUTPUT_PATH = os.getenv("EXCEL_OUTPUT_PATH", "output/results.xlsx")
DEFAULT_APPLIED_STATUS = "Not Applied"
FOLLOW_UP_DAYS = int(os.getenv("FOLLOW_UP_DAYS", 14))

HEADERS = {
    "User-Agent": os.getenv(
        "USER_AGENT",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    )
}
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", 2))

# Add LinkedIn credentials
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")