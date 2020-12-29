import calendar
import requests
import time

import beeminder
from goaltype import GoalType
from params import GOAL_TYPE
from treehouse import Treehouse


class InvalidGoalType(Exception):
    pass


def validate_goal_type():
    if GOAL_TYPE not in GoalType:
        raise InvalidGoalType("Goal type must be one of 'badges' or 'points'")
    pass


def time_to_timestamp(time_str):
    return calendar.timegm(time.strptime(time_str, "%Y-%m-%dT%H:%M:%S.000Z"))


def badge_to_datapoint(badge):
    return beeminder.Datapoint(
        value = 1,
        timestamp = time_to_timestamp(badge["earned_date"]),
        comment = badge["name"],
        request_id = str(badge["id"])
    )


def main():
    validate_goal_type()
    treehouse = Treehouse()
    bee = beeminder.Beeminder()

    if GOAL_TYPE.lower() == GoalType["BADGES"]:
        datapoints = [badge_to_datapoint(badge) for badge in treehouse.badges]
        response = bee.send_datapoints(datapoints)
    elif GOAL_TYPE.lower() == GoalType["POINTS"]:
        datapoint = beeminder.Datapoint(value = treehouse.total_points)
        response = bee.send_datapoint(datapoint)
    else:
        raise InvalidGoalType("Goal type must be one of 'badges' or 'points'")

    return response


if __name__ == "__main__":
    print(main())
