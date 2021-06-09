# Treeminder

Keep track of your Team Treehouse (https://teamtreehouse.com/) badges or points on Beeminder (https://beeminder.com/)

# Instructions

## Filling in params.yaml

1. Open params.yaml in a text editor.
2. Fill in all the fields.
   1. Grab your Beeminder auth_token here: https://www.beeminder.com/api/v1/auth_token.json
   2. If the Beeminder URL of your Team Treehouse goal is, for example, beeminder.com/username/**treebadges**, then your slug is **treebadges**
3. Lastly, for GOAL_TYPE, enter whether you prefer to track "badges" or "points". 
   
## Run treeminder.py

Run treeminder.py with 

```python treeminder.py```

This will return a response. If all goes according to plan, it should return ```Response <[200]>```

You may need to install YAML. To install with pip,

```pip install pyyaml```

## Notes

Keep in mind that if you track badges, it will add a datapoint for every badge you have ever earned, including any badges you've earned before you made your Beeminder goal.

Happy coding!

# Developer's Notes

* treeminder.py – this is the main file, integrating both treehouse.py and beeminder.py
* treehouse.py – Treehouse class, to get points count and badge count
* beeminder.py – Beeminder class, so we can send points to Beeminder. Also contains a Datapoint dataclass.
* goaltype.py – Contains the GoalType enum class. There are only two valid goals for the time being: points and badges
* params.yaml – This is where user parameters are stored.
