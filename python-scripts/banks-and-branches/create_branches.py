# get list of banks
import requests
import time
from faker import Faker

fake = Faker()

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}

# def list_banks():
#
#     selection = True
#     while selection:
#         try:
#
#             get_banks = requests.get(BASE + "/banks", headers=headers)
#             banks_dict = get_banks.json()
#
#             banks_list = "\n~~~ Select Bank To Add Branches To By Bank ID ~~~\n"
#
#             for i in range(len(banks_dict["content"])):
#
#                 bank_info_dict = banks_dict["content"][i]
#                 bank_id = bank_info_dict["id"]
#                 bank_address = bank_info_dict["address"]
#                 bank_city = bank_info_dict["city"]
#                 bank_state = bank_info_dict["state"]
#
#                 banks_list += f"ID:{bank_id} {bank_address}, {bank_city}, {bank_state}\n"
#
#             print(banks_list)
#
#             bank_id_number = int(input("Select ID: "))
#
#             verify_bank = requests.get(BASE + f"/banks/id/{bank_id_number}", headers=headers)
#             if verify_bank.status_code != 200:
#                 print("\n(Error!) Please Select Valid ID...")
#             
#             else:
#                 return bank_id_number
#
#         except Exception as e:
#             # logging.error("There Was A Problem Running The Application")
#             print(e)
#             print("\n(Error!) There Was A Problem Running The Application...")


def create_branches(banks_created_id_array):
    try:
        print(banks_created_id_array)    
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
        print("\n(Error!) There Was A Problem Running The Application...")
