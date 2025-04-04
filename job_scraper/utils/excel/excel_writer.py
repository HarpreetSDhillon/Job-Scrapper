import os
import pandas as pd
from datetime import datetime, timedelta
from job_scraper.config import FOLLOW_UP_DAYS

class ExcelWriter:
    def __init__(self, output_path, headers):
        self.output_path = output_path
        self.headers = headers

    def write_jobs_to_excel(self, jobs):
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

        # Check if the file already exists
        if os.path.exists(self.output_path):
            # Read the existing data
            existing_data = pd.read_excel(self.output_path, engine="openpyxl")
            # Ensure the headers match
            if list(existing_data.columns) != self.headers:
                print("Headers in the existing file do not match the expected headers. Updating headers.")
                existing_data = existing_data.reindex(columns=self.headers, fill_value="")
            # Convert the new jobs to a DataFrame
            new_data = pd.DataFrame(jobs, columns=self.headers)
            # Append the new jobs to the existing data
            combined_data = pd.concat([existing_data, new_data], ignore_index=True)
        else:
            # If the file doesn't exist, create a new DataFrame with headers
            combined_data = pd.DataFrame(jobs, columns=self.headers)

        # Update follow-up dates for all jobs
        combined_data = combined_data.apply(self.update_follow_up_dates, axis=1)

        # Write the combined data back to the Excel file
        combined_data.to_excel(self.output_path, index=False, engine="openpyxl")
        print(f"Data successfully written to {self.output_path}")

    @staticmethod
    def update_follow_up_dates(job):
        """Update follow-up dates for a single job."""
        if job["Applied_Status"].lower() == "applied" and job["Applied_Date"]:
            applied_date = datetime.strptime(job["Applied_Date"], "%Y-%m-%d")
            job["Follow_Up_Date"] = (applied_date + timedelta(days=FOLLOW_UP_DAYS)).strftime("%Y-%m-%d")
        elif not job.get("Follow_Up_Date"):
            job["Follow_Up_Date"] = ""
        return job