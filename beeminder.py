import time
from dataclasses import dataclass
from typing import Optional, Union, List

import requests


@dataclass
class Datapoint():
    value: int
    timestamp: Union[int, float] = time.time()
    comment: Optional[str] = ""
    request_id: Optional[str] = ""

    @property
    def json(self):
        return self.__dict__


class Beeminder():
    def __init__(self, username, goal, api_key):
        self._username = username
        self._goal = goal
        self._apikey = api_key

    @property
    def goal_url(self):
        return f"https://www.beeminder.com/api/v1/users/" \
               f"{self._username}/goals/{self._goal}/"

    @property
    def single_datapoint_url(self):
        return self.goal_url + "/datapoints.json"

    @property
    def multiple_datapoints_url(self):
        return self.goal_url + "datapoints/create_all.json"
    
    def send_datapoint(self, datapoint: Datapoint):
        values = dict(auth_token = self._apikey, **datapoint.json)
        return self._send_data(self.single_datapoint_url, values)

    def send_datapoints(self, datapoints: List[Datapoint]):
        values = dict(auth_token = self._apikey)
        values["datapoints"] = [datapoint.json for datapoint in datapoints]
        return self._send_data(self.multiple_datapoints_url, values)

    def _send_data(self, url, data):
        return requests.post(url, json=data)
