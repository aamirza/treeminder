import calendar
import time

import beeminder
from goaltype import GoalType
from params import GOAL_TYPE
from treehouse import Treehouse


class InvalidGoalType(Exception):
    pass


def validate_goal_type():
    if GOAL_TYPE.upper() not in GoalType:
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


def send_badges_to_beeminder(badges, bmndr):
    datapoints = [badge_to_datapoint(badge) for badge in badges]
    return bmndr.send_datapoints(datapoints)


def send_points_to_beeminder(points, bmndr):
    datapoint = beeminder.Datapoint(value=points)
    return bmndr.send_datapoint(datapoint)


def main():
    validate_goal_type()

    treehouse = Treehouse()
    bee = beeminder.Beeminder()

    if GOAL_TYPE.lower() == GoalType["BADGES"]:
        response = send_badges_to_beeminder(treehouse.badges, bee)
    elif GOAL_TYPE.lower() == GoalType["POINTS"]:
        response = send_points_to_beeminder(treehouse.total_points, bee)
    return response


if __name__ == "__main__":
    print(main())
