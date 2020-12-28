import calendar
import requests
import time

from params import *
import treehouse

def main():
    treehouse_data = treehouse.get_data(TREEHOUSE_USERNAME)

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
