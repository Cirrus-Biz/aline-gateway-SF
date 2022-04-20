import os
import requests
import sys
import unittest
from dotenv import load_dotenv, find_dotenv

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(dir_path)

# loads bearer token from .env
load_dotenv(find_dotenv())
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

BASE = "http://127.0.0.1"
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

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



