import os
import pandas as pd
from datetime import datetime
from job_scraper.utils.todoist.todoist_integration import TodoistIntegration
from job_scraper.Config.excel_config import ExcelConfig

class FollowUpChecker:
    def __init__(self, excel_path=None):
        config = ExcelConfig()
        self.excel_path = excel_path or config.EXCEL_OUTPUT_PATH
        self.todoist = TodoistIntegration()

    def ensure_excel_file_exists(self):
        """Ensure the Excel file exists, create an empty one if not."""
        if not os.path.exists(self.excel_path):
            print(f"No follow-up file found at {self.excel_path}. Creating an empty file.")
            pd.DataFrame().to_excel(self.excel_path, index=False)

    def read_excel_file(self):
        """Read the Excel file and return a DataFrame."""
        try:
            return pd.read_excel(self.excel_path, engine="openpyxl")
        except Exception as e:
            print(f"Error reading the Excel file: {e}")
            return pd.DataFrame()

    def check_for_followups(self):
        """Check for follow-ups and create Todoist tasks if needed."""
        self.ensure_excel_file_exists()
        df = self.read_excel_file()

        if df.empty:
            print("No data found in the Excel file.")
            return

        today = datetime.today().date()

        for _, row in df.iterrows():
            applied_status = row.get("applied_status", "")
            applied_date = row.get("applied_date")
            follow_up_date = row.get("follow_up_date")

            if applied_status == "Applied" and pd.notna(applied_date) and pd.notna(follow_up_date):
                follow_up_date = pd.to_datetime(follow_up_date).date()
                if follow_up_date <= today:
                    task_content = f"Follow up with {row['company']} for {row['title']}"
                    self.todoist.create_task(task_content)

        print("Follow-up check completed.")