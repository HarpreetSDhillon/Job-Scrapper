import requests
from job_scraper.config import TODOIST_API_TOKEN

def create_todoist_task(content):
    if not TODOIST_API_TOKEN:
        print("No Todoist API token provided.")
        return

    url = "https://api.todoist.com/rest/v2/tasks"
    headers = {
        "Authorization": f"Bearer {TODOIST_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "content": content
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200 or response.status_code == 204:
        print(f"Task created: {content}")
    else:
        print(f"Failed to create task: {response.status_code} - {response.text}")
