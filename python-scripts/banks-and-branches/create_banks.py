import requests
from faker import Faker

fake = Faker()

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}

def create_banks(number_of_banks: int) -> list[int]:

    banks_created_id_array = []
    
    banks_created = 0
    for _ in range(number_of_banks):

        payload = {"routingNumber": fake.aba(),
                   "address": fake.street_address(),
                   "city": fake.city(),
                   "state": fake.state(),
                   "zipcode": fake.zipcode()}

        response = requests.post(BASE + "/banks", json=payload, headers=headers)

        if response.status_code == 201:
            banks_created += 1
            bank_returned_dict = response.json()
            banks_created_id_array.append(bank_returned_dict["id"])

        bank_id = response.json()["id"]
        bank_city = response.json()["city"]
        bank_state = response.json()["state"]
        bank_zipcode = response.json()["zipcode"]

        print(f"Created Bank: ID:{bank_id} City:{bank_city} State:{bank_state} ZIP:{bank_zipcode}")

    print(f"~~~ You Successfully Created {banks_created} Banks ~~~")
    return banks_created_id_array
