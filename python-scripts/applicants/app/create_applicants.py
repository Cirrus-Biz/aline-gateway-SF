import requests
from faker import Faker
from random import randint

fake = Faker()

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}


def create_applicants(number_of_applicants: int):

    try:

        applicants_created = 0
        for _ in range(number_of_applicants):

            # creates data outside of payload to avoid JSON object errors
            fake_date = str(fake.date_of_birth(minimum_age=25))
            fake_phone_number = str(randint(100,999)) + "-" + str(randint(100,999)) + "-" + str(randint(1000,9999))

            payload =  {
                           "firstName": fake.first_name(),
                           "middleName": fake.first_name(),
                           "lastName": fake.last_name(),
                           "dateOfBirth": fake_date,
                           "gender": "MALE",
                           "email": fake.first_name() + fake.last_name() + "@gmail.com",
                           "phone": fake_phone_number,
                           "socialSecurity": fake.ssn(),
                           "driversLicense": fake.license_plate(),
                           "income": 100000000,
                           "address": fake.street_address(),
                           "city": fake.city(),
                           "state": fake.state(),
                           "zipcode": fake.zipcode(),
                           "mailingAddress": fake.street_address(),
                           "mailingCity": fake.city(),
                           "mailingState": fake.state(),
                           "mailingZipcode": fake.zipcode()
                        }

            # posts data to endpointresponse
            response = requests.post(BASE + "/applicants", json=payload, headers=headers)

            if response.status_code == 201:
                applicants_created += 1

            # parses data from return JSON
            applicants_id = response.json()["id"]
            applicants_firstname = response.json()["firstName"]
            applicants_lastname = response.json()["lastName"]
            
            print(f"\nCreated Applicant: ID:{applicants_id} ~ {applicants_firstname} {applicants_lastname}")

        print(f"~~~ You Successfully Created {applicants_created} Applicants ~~~")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Creating Applicants...")

