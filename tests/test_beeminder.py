import time
import unittest

import beeminder


class MyTestCase(unittest.TestCase):
    def test_datapoint_json(self):
        timestamp = time.time()
        datapoint = beeminder.Datapoint(value=100, timestamp=timestamp)
        expected_json = {"value": 100, "timestamp": timestamp, "comment": "",
                         "request_id": ""}
        self.assertEqual(datapoint.json, expected_json)

    def test_correct_beeminder_url(self):
        self.assertEqual("https://www.beeminder.com/api/v1/users/dee/goals/badges/",
                         beeminder.Beeminder("dee", "badges", api_key="none").goal_url)




if __name__ == '__main__':
    unittest.main()
