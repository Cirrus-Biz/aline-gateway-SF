import os
import requests
import sys
import unittest
from faker import Faker
from dotenv import load_dotenv, find_dotenv

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(dir_path)

fake = Faker()

# loads bearer token from .env
load_dotenv(find_dotenv())
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

BASE = "http://127.0.0.1"
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

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

