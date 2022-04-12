import requests
from faker import Faker
from random import randint

fake = Faker()

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}


def create_applications(number_of_applications: int):

    selection = True
    while selection:
        try:
            
            selection_number = int(input(
                "\n--- Type of Account For Applications ---\n"
                "Choose 1 For Checking Account\n"
                "Choose 2 For Savings Account\n"
                "Choose 3 For Checking and Savings Account\n"
                "Enter Number: ")
            )

            if selection_number < 1 or selection_number > 3:
                print("\n(Error!) Please Select Valid Number(1,2,3)")

            else:

                selection = False

                # sets account type based on user input
                account_type = ""
                if selection_number == 1:
                    account_type = "CHECKING"
                elif selection_number == 2:
                    account_type = "SAVINGS"
                elif selection_number == 3:
                    account_type = "CHECKING_AND_SAVINGS"

                applications_created = 0
                for _ in range(number_of_applications):

                    # creates data outside of payload to avoid JSON object errors
                    fake_date = str(fake.date_of_birth(minimum_age=25))
                    fake_phone_number = str(randint(100,999)) + "-" + str(randint(100,999)) + "-" + str(randint(1000,9999))

                    payload =  {
                                  "applicationType": account_type,
                                  "applicants": [
                                    {
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
                                  ]
                                }

                    # posts data to endpointresponse
                    response = requests.post(BASE + "/applications", json=payload, headers=headers)

                    if response.status_code == 201:
                        applications_created += 1

                    # parses data from return JSON
                    applicants_firstname = response.json()["applicants"][0]["firstName"]
                    applicants_lastname = response.json()["applicants"][0]["lastName"]
                    applicants_account_type = response.json()["type"]
                    applicants_social = response.json()["applicants"][0]["socialSecurity"]
                    
                    print(f"\nCreated Applicant: ~ {applicants_firstname} {applicants_lastname} ~ Type:{applicants_account_type} ~ Social-Security:{applicants_social} |")

                print(f"~~~ You Successfully Created {applications_created} Applications ~~~")

        except Exception as e:
            print(e)
            print("\n(Error!) There Was A Problem Creating Applications...")
