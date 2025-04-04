import os
from dotenv import load_dotenv

class ExcelConfig:
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
        load_dotenv(dotenv_path=dotenv_path)

        self.EXCEL_OUTPUT_PATH = os.getenv("EXCEL_OUTPUT_PATH", "output/results.xlsx")
        self.DEFAULT_APPLIED_STATUS = "Not Applied"
        self.FOLLOW_UP_DAYS = int(os.getenv("FOLLOW_UP_DAYS", 14))