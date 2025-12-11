import requests
import yaml

class APIClient:
    def __init__(self):
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)
        self.base_url = config["api_url"]


    def get_users(self, page=1):
        return requests.get(f"{self.base_url}/users", params={"page": page})


    def create_user(self, name, job):
        payload = {"name": name, "job": job}
        return requests.post(f"{self.base_url}/users", json=payload)


    def delete_user(self, user_id):
        return requests.delete(f"{self.base_url}/users/{user_id}")


    def get_user_by_id(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}")
