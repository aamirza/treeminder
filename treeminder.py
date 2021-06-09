import calendar
import os
import time

import yaml

import beeminder
from goaltype import GoalType
from treehouse import Treehouse


PARAMS_FILE = os.path.join(os.path.dirname(__file__), "params.yaml")


class InvalidGoalType(Exception):
    pass


def validate_goal_type(goal_type):
    if goal_type not in GoalType:
        raise InvalidGoalType("Goal type must be one of 'badges' or 'points'")
    return GoalType[goal_type.upper()]


def get_yaml_data():
    with open(PARAMS_FILE, 'r') as params:
        user_data = yaml.safe_load(params)
    return user_data


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
    user = get_yaml_data()
    goal_type = validate_goal_type(user['GOAL_TYPE'])

    treehouse = Treehouse(username=user['TREEHOUSE_USERNAME'])
    bee = beeminder.Beeminder(username=user['BEEMINDER_USERNAME'],
                              goal=user['BEEMINDER_GOAL_SLUG'],
                              api_key=user['BEEMINDER_AUTH_TOKEN'])

    if goal_type == GoalType.BADGES:
        response = send_badges_to_beeminder(treehouse.badges, bee)
    elif goal_type == GoalType.POINTS:
        response = send_points_to_beeminder(treehouse.total_points, bee)
    return response


if __name__ == "__main__":
    print(main())
