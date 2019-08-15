import calendar
import requests
import time

from params import *


def get_treehouse_data(username):
    treehouse_url = "https://teamtreehouse.com/" + username + ".json"
    response = requests.get(treehouse_url).json()
    return response


def main():
    treehouse_data = get_treehouse_data(TREEHOUSE_USERNAME)
    beeminder_url = "https://www.beeminder.com/api/v1/users/{}/goals/{}/".format(
        BEEMINDER_USERNAME, BEEMINDER_GOAL
    )

    if GOAL_TYPE == "badges":
        values = {"auth_token": BEEMINDER_APIKEY,
                  "datapoints": []}
        beeminder_url += "datapoints/create_all.json"
        for badge in treehouse_data["badges"]:
            timestamp = calendar.timegm(time.strptime(badge["earned_date"],
                                                      "%Y-%m-%dT%H:%M:%S.000Z"))
            values["datapoints"].append({
                "timestamp": timestamp,
                "value": 1,
                "comment": badge["name"],
                "requestid": str(badge["id"])
            })
    elif GOAL_TYPE == "points":
        values = {
            "auth_token": BEEMINDER_APIKEY,
            "timestamp": time.time(),
            "value": treehouse_data["points"]["total"],
            "comment": ""
        }
        beeminder_url += "datapoints.json"

    response = requests.post(beeminder_url, json=values)
    return response


if __name__ == "__main__":
    print(main())
