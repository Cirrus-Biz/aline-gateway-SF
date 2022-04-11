import requests
import sys
sys.path.append("/Users/stephenfreed/Projects/Capstone/Cirrus-Biz/aline-gateway-SF/python-scripts/banks-and-branches/")

from app import create_banks, create_branches
import unittest

BASE = "http://127.0.0.1"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}

class Test_CreateBanks(unittest.TestCase):

# ~~~~~ Tests Functionality of Createing Banks ~~~~~

    def test_check_connection_health(self):
        health_response = requests.get(BASE + ":8072/health", headers=headers)
        statuscode = health_response.status_code
        self.assertEqual(statuscode, 200)

