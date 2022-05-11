import os
import requests
from faker import Faker
from dotenv import load_dotenv, find_dotenv

fake = Faker()

# loads bearer token from .env
load_dotenv(find_dotenv())
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
HOST = os.environ.get("HOST")

BASE = f"http://{HOST}:8080/api"
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}


def create_branches(selected_bank_id):

    try:

        number_of_branches = int(input(
            "\n--- Create Branches ---\n"
            "Enter The Number Of Branches To Create: ")
        )

        branches_created = 0
        for _ in range(number_of_branches):

            # creates fake data
            payload = {
                       "name": fake.company(),
                       "address": fake.street_address(),
                       "city": fake.city(),
                       "state": fake.state(),
                       "zipcode": fake.zipcode(),
                       "phone": fake.phone_number(),
                       "bankID": selected_bank_id}

            # posts branch with selected bank id
            response = requests.post(BASE + "/branches", json=payload, headers=headers)

            if response.status_code == 201:
                branches_created += 1

            # parses response to display branch info
            branch_id = response.json()["id"]
            branch_name = response.json()["name"]
            branch_city = response.json()["city"]
            branch_bank_id = response.json()["bank"]["id"]

            print(f"Created Branch: ID:{branch_id} Name:{branch_name} City:{branch_city} BankID:{branch_bank_id}")


        print(f"~~~ You Successfully Created {branches_created} Branches For Bank ID:{selected_bank_id}~~~")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Creating Branches...")
