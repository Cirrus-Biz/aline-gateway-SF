import requests
import time
from faker import Faker

fake = Faker()

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}

def create_branches(banks_created_id_array):

    try:
        branches_created = 0
        for bank_id in banks_created_id_array:

            payload = {
                       "name": fake.company(),
                       "address": fake.street_address(),
                       "city": fake.city(),
                       "state": fake.state(),
                       "zipcode": fake.zipcode(),
                       "phone": fake.phone_number(),
                       "bankID": bank_id}

            response = requests.post(BASE + "/branches", json=payload, headers=headers)

            if response.status_code == 201:
                branches_created += 1

            branch_id = response.json()["id"]
            branch_name = response.json()["name"]
            branch_city = response.json()["city"]
            branch_bank_id = response.json()["bank"]["id"]

            print(f"Created Branch: ID:{branch_id} Name:{branch_name} City:{branch_city} BankID:{branch_bank_id}")


        print(f"~~~ You Successfully Created {branches_created} Branches For {len(banks_created_id_array)} Banks ~~~")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Creating Branches...")
