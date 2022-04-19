import os
import requests
import sys
import unittest

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(dir_path)

BASE = "http://127.0.0.1"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuZnJlZWQiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjUwMzI2NTA4LCJleHAiOjE2NTE1MzYxMDh9.BjZiqm0ozzxFizdYK94-v08QDS5DvbjEp2aS1teyCFs"}

class Tests(unittest.TestCase):

# ~~~~~ Tests Functionality of Transaction ~~~~~

    # checks transactions endpoint is healthy
    def test_check_connection_health_transaction(self):
        health_response = requests.get(BASE + ":8073/health", headers=headers)
        statuscode = health_response.status_code
        self.assertEqual(statuscode, 200)

    # checks members endpoint is healthy
    def test_check_connection_health_member(self):
        health_response = requests.get(BASE + ":8074/health", headers=headers)
        statuscode = health_response.status_code
        self.assertEqual(statuscode, 200)

    # add more unit tests



