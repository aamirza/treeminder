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
        return requests.get(self.user_data_url).json()

    @property
    def badges(self):
        return self.data["badges"]

    @property
    def total_points(self):
        return self.data["points"]["total"]
