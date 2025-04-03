import os
import pandas as pd
from datetime import datetime, timedelta
from job_scraper.config import EXCEL_OUTPUT_PATH, FOLLOW_UP_DAYS

# Default headers for the Excel file
DEFAULT_HEADERS = [
    "Title","Company","Link","Job_Description","Source","Applied_Status",
    "Applied_Date","Follow_Up_Date","Cold_Email_Contacts",
    "Tech_To_Study","Resume_Used","Refferal_Contact","Notes","Location",
    "Salary","Job_Level",
]

def write_to_excel(jobs, output_path=EXCEL_OUTPUT_PATH):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Get headers from the environment or use default headers
    headers = os.getenv("EXCEL_HEADERS", ",".join(DEFAULT_HEADERS)).split(",")

    # Check if the file already exists
    if os.path.exists(output_path):
        # Read the existing data
        existing_data = pd.read_excel(output_path, engine="openpyxl")
        # Ensure the headers match
        if list(existing_data.columns) != headers:
            print("Headers in the existing file do not match the expected headers. Updating headers.")
            existing_data = existing_data.reindex(columns=headers, fill_value="")
        # Convert the new jobs to a DataFrame
        new_data = pd.DataFrame(jobs, columns=headers)
        # Append the new jobs to the existing data
        combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        # If the file doesn't exist, create a new DataFrame with headers
        combined_data = pd.DataFrame(jobs, columns=headers)

    # Update follow-up dates for all jobs
    combined_data = combined_data.apply(update_follow_up_dates, axis=1)

    # Write the combined data back to the Excel file
    combined_data.to_excel(output_path, index=False, engine="openpyxl")
    print(f"Data successfully written to {output_path}")

def update_follow_up_dates(job):
    """Update follow-up dates for a single job."""
    if job["applied_status"].lower() == "applied" and job["applied_date"]:
        applied_date = datetime.strptime(job["applied_date"], "%Y-%m-%d")
        job["follow_up_date"] = (applied_date + timedelta(days=FOLLOW_UP_DAYS)).strftime("%Y-%m-%d")
    elif not job.get("follow_up_date"):
        job["follow_up_date"] = ""
    return job