import requests
from random import randint
from faker import Faker

fake = Faker()

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}


def create_admins():

    selection = True
    while selection:
        try:
            
            selection_number = int(input(
                f"\n--- Create Admin Users ---\n"
                f"How Many Admin Users To Create?\n"
                f"Enter Number of Admin Users: ")
            )

            if selection_number < 0:
                print("\n(Error!) Please Select Valid Number...")

            else:

                selection = False

                users_created = 0
                for _ in range(selection_number):

                    # creates data outside of payload to avoid JSON object errors
                    fake_phone_number = str(randint(100,999)) + "-" + str(randint(100,999)) + "-" + str(randint(1000,9999))
                    fake_username =  str(fake.first_name()) + str(randint(100,999))
                    fake_password = str(randint(100000000000,199999999999)) + "a3!A"

                    payload =  {
                                  "username": fake_username,
                                  "password": fake_password,
                                  "role": "admin",
                                  "firstName": fake.first_name(),
                                  "lastName": fake.last_name(),
                                  "email": fake.first_name() + fake.last_name() + "@gmail.com",
                                  "phone": fake_phone_number,
                            }

                    # posts data to endpointresponse
                    response = requests.post(BASE + "/users/registration", json=payload, headers=headers)

                    if response.status_code == 201:
                        users_created += 1

                    # parses data from return JSON
                    users_id = response.json()["id"]
                    users_firstname = response.json()["firstName"]
                    users_lastname = response.json()["lastName"]
                    users_role = response.json()["role"]

                    print(f"\nCreated User: ID:{users_id} Role:{users_role} ~ {users_firstname} {users_lastname} ~")

                print(f"~~~ You Successfully Created {users_created} Admin Users ~~~")

        except Exception as e:
            print(e)
            print("\n(Error!) There Was A Problem Creating Users...")


