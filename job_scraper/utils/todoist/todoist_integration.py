import requests
from job_scraper.Config.general_config import GeneralConfig

class TodoistIntegration:
    def __init__(self, api_token=None):
        config = GeneralConfig()
        self.api_token = api_token or config.TODOIST_API_TOKEN
        self.base_url = "https://api.todoist.com/rest/v2/tasks"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }

    def create_task(self, content, due_date=None, project_id=None):
        """Create a task in Todoist."""
        payload = {"content": content}
        if due_date:
            payload["due_date"] = due_date
        if project_id:
            payload["project_id"] = project_id

        response = requests.post(self.base_url, json=payload, headers=self.headers)
        if response.status_code == 200 or response.status_code == 204:
            print(f"Task '{content}' created successfully.")
        else:
            print(f"Failed to create task: {response.status_code} - {response.text}")

    def get_tasks(self):
        """Retrieve all tasks from Todoist."""
        response = requests.get(self.base_url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve tasks: {response.status_code} - {response.text}")
            return []

    def delete_task(self, task_id):
        """Delete a task in Todoist."""
        url = f"{self.base_url}/{task_id}"
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"Failed to delete task: {response.status_code} - {response.text}")