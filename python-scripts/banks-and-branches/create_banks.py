import requests
from faker import Faker

fake = Faker()

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTYzNzUxOCwiZXhwIjoxNjUwODQ3MTE4fQ.dziM9LxVRA9vBWg7Q9elGjnEkaXiDk-xr3vLlNHIYIs"}

def create_banks(number_of_banks: int):

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

        print(f"Status Code: {response.json()}")

    print(f"~~~ You Successfully Created {banks_created} Banks ~~~")
