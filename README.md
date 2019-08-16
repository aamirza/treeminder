# Treeminder

Keep track of your Team Treehouse (https://teamtreehouse.com/) badges or points on Beeminder (https://beeminder.com/)

# Instructions

1. Open params.py in a text editor.
2. Fill in all the fields in between the quotation marks (")
3. Find your Beeminder auth_token here (https://www.beeminder.com/api/v1/auth_token.json)
4. If the Beeminder URL of your Team Treehouse goal is, for example, beeminder.com/username/**treebadges**, then the BEEMINDER_GOAL = "treebadges"
5. Lastly, for GOAL_TYPE, write whether you prefer to track "badges" or "points". 

Keep in mind that if you track badges, it will add a datapoint for every badge you have ever earned, including any badges you earned before you made your Beeminder goal.
