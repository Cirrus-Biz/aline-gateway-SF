import requests
import sys
import unittest
from faker import Faker

sys.path.append("/Users/stephenfreed/Projects/Capstone/Cirrus-Biz/aline-gateway-SF/python-scripts/applicants/")

fake = Faker()

BASE = "http://127.0.0.1"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}

class Tests(unittest.TestCase):

# ~~~~~ Tests Functionality of Applicants ~~~~~

    # checks underwriter endpoint is healthy
    def test_check_connection_health(self):
        health_response = requests.get(BASE + ":8071/health", headers=headers)
        statuscode = health_response.status_code
        self.assertEqual(statuscode, 200)

    def test_faker(self):
        zipcode = fake.zipcode()
        self.assertEqual(len(zipcode), 5)

    def test_applications(self):
        get_banks = requests.get(BASE + ":8080/api/applications", headers=headers)
        get_banks_status_code = get_banks.status_code
        self.assertEqual(get_banks_status_code, 200)

    def test_applicants(self):
        get_banks = requests.get(BASE + ":8080/api/applicants", headers=headers)
        get_banks_status_code = get_banks.status_code
        self.assertEqual(get_banks_status_code, 200)

