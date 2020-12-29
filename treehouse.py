import requests

from params import TREEHOUSE_USERNAME


class Treehouse():
    def __init__(self, username=TREEHOUSE_USERNAME):
        self._username = username
        self.data = self.get_data()

    @property
    def username(self):
        return self._username

    @property
    def user_data_url(self):
        return "https://teamtreehouse.com/" + self.username + ".json"

    def get_data(self):
        response = requests.get(self.user_data_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise SystemExit(f"Error retrieving Treehouse data: "
                             f"Response {response.status_code}")

    @property
    def badges(self):
        return self.data["badges"]

    @property
    def total_points(self):
        return self.data["points"]["total"]
