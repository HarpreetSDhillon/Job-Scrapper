import os
import pandas as pd

class ExcelReader:
    def __init__(self, output_path):
        self.output_path = output_path

    def read_jobs_from_excel(self):
        """Read jobs from the Excel file."""
        if os.path.exists(self.output_path):
            return pd.read_excel(self.output_path, engine="openpyxl")
        else:
            print(f"No file found at {self.output_path}. Returning an empty DataFrame.")
            return pd.DataFrame()