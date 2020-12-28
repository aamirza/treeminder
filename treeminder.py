import calendar
import requests
import time

import beeminder
from goaltype import GoalType
from params import GOAL_TYPE
from treehouse import Treehouse


def main():
    treehouse = Treehouse()
    bee = beeminder.Beeminder()
    if GOAL_TYPE.upper() == GoalType["BADGES"]:
        datapoints = []
        for badge in treehouse.badges:
            timestamp = calendar.timegm(time.strptime(badge["earned_date"],
                                                      "%Y-%m-%dT%H:%M:%S.000Z"))
            datapoints.append(beeminder.Datapoint(
                value = 1,
                timestamp = timestamp,
                comment = badge["name"],
                request_id = str(badge["id"])
            ))
        response = bee.send_datapoints(datapoints)
    elif GOAL_TYPE.upper() == GoalType["POINTS"]:
        datapoint = beeminder.Datapoint(value = treehouse.total_points)
        response = bee.send_datapoint(datapoint)
    return response


if __name__ == "__main__":
    print(main())
