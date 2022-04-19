import os
import requests
import sys
import unittest
from faker import Faker
# from app import create_banks
# from app import create_branches

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(dir_path)

fake = Faker()

BASE = "http://127.0.0.1"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}

class Tests(unittest.TestCase):

# ~~~~~ Tests Functionality of Banks and Branches ~~~~~

    # checks banks and branches endpoint is healthy
    def test_check_connection_health(self):
        health_response = requests.get(BASE + ":8072/health", headers=headers)
        statuscode = health_response.status_code
        self.assertEqual(statuscode, 200)

    def test_faker(self):
        zipcode = fake.zipcode()
        self.assertEqual(len(zipcode), 5)

    def test_banks(self):
        get_banks = requests.get(BASE + ":8080/api/banks", headers=headers)
        get_banks_status_code = get_banks.status_code
        self.assertEqual(get_banks_status_code, 200)


    def test_branches(self):
        get_branches = requests.get(BASE + ":8080/api/branches", headers=headers)
        get_branches_status_code = get_branches.status_code
        self.assertEqual(get_branches_status_code, 200)

