from params import BEEMINDER_GOAL, BEEMINDER_USERNAME, BEEMINDER_APIKEY


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


