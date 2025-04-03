import os
import pandas as pd
from datetime import datetime
from job_scraper.todoist_integration import create_todoist_task
from job_scraper.config import EXCEL_OUTPUT_PATH

def check_for_followups():
    # Check if the Excel file exists
    if not os.path.exists(EXCEL_OUTPUT_PATH):
        print(f"No follow-up file found at {EXCEL_OUTPUT_PATH}. Creating an empty file.")
        # Create an empty Excel file
        pd.DataFrame().to_excel(EXCEL_OUTPUT_PATH, index=False)
        return

    # Read the Excel file
    try:
        df = pd.read_excel(EXCEL_OUTPUT_PATH, engine="openpyxl")  # Specify the engine explicitly
        today = datetime.today().date()

        for _, row in df.iterrows():
            if (row.get("applied_status", "") == "Applied" and
                pd.notna(row.get("applied_date")) and
                pd.notna(row.get("follow_up_date"))):

                follow_up_date = pd.to_datetime(row["follow_up_date"]).date()
                if follow_up_date <= today:
                    task_content = f"Follow up with {row['company']} for {row['title']}"
                    create_todoist_task(task_content)
            print("Follow-up check completed.")
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return
    df = pd.read_excel(EXCEL_OUTPUT_PATH)
    