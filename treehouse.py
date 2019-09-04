import requests

def get_data(username):
    """
    Retrieve Team Treehouse data (e.g. points, badges, avatar) for a user in
    JSON format
    """
    treehouse_url = "https://teamtreehouse.com/" + username + ".json"
    response = requests.get(treehouse_url).json()
    return response
