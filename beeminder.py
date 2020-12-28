import time
from dataclasses import dataclass
from typing import Optional

from params import BEEMINDER_GOAL, BEEMINDER_USERNAME, BEEMINDER_APIKEY


@dataclass
class Datapoint():
    value: int
    timestamp: int = time.time()
    comment: Optional[str] = ""
    request_id: Optional[str] = ""


class Beeminder():
    def __init__(self, username=BEEMINDER_USERNAME, goal=BEEMINDER_GOAL,
                 api_key=BEEMINDER_APIKEY):
        self._username = username
        self._goal = goal
        self._apikey = api_key

    @property
    def goal_url(self):
        return f"https://www.beeminder.com/api/v1/users/" \
               f"{self._username}/goals/{self._goal}/"
