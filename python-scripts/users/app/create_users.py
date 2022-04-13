import requests
from random import randint
from faker import Faker
from random import randint

fake = Faker()

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}


def create_users(user_role):

    selection = True
    while selection:
        try:
            
            if user_role == "admin":
                selection_number = int(input(
                    f"\n--- Create {user_role.capitalize()} Users ---\n"
                    f"How Many {user_role.capitalize()} Users To Create?\n"
                    f"Enter Number of {user_role.capitalize()} Users: ")
                )

            if selection_number < 0:
                print("\n(Error!) Please Select Valid Number...")

            else:

                selection = False

                if user_role == "admin":
                    users_created = 0
                    for _ in range(selection_number):

                        # creates data outside of payload to avoid JSON object errors
                        fake_phone_number = str(randint(100,999)) + "-" + str(randint(100,999)) + "-" + str(randint(1000,9999))
                        fake_username =  str(fake.first_name()) + str(randint(100,999))
                        fake_password = str(randint(100000000000,199999999999)) + "a3!A"

                        if user_role == "admin":
                            payload =  {
                                          "username": fake_username,
                                          "password": fake_password,
                                          "role": user_role,
                                          "firstName": fake.first_name(),
                                          "lastName": fake.last_name(),
                                          "email": fake.first_name() + fake.last_name() + "@gmail.com",
                                          "phone": fake_phone_number,
                                    }
                elif user_role == "member":

                    selection_show_this_many_members = int(input(
                        f"\n--- Create Member Users ---\n"
                        f"We Will Only Show You Members That Are Not Currently Users\n"
                        f"How Many Valid Members Would You Like To Choose From?: ")
                    )

                    get_members = requests.get(BASE + "/api/members", headers=headers)
                    members_dict = get_members.json()

                    get_users = requests.get(BASE + "/api/users", headers=headers)
                    users_dict = get_users.json()
                    membership_id_list = []
                    for user in users_dict:
                        membership_id_list.append(user["content"]["membershipId"])

                    member_counter = 0
                    for member in members_dict:

                        # membership_applicant_id = response.json()["id"]
                        membership_member_id = response.json()["membershipId"]
                        membership_4_last_social = response.json()["applicant"]["socialSecurity"]
                        membership_firstname = response.json()["applicant"]["firstName"]
                        membership_lastname = response.json()["applicant"]["lastName"]

                        if membership_id_list.contains(membership_member_id):
                            continue

                        print(f"\nMember: Member_ID:{membership_member_id} ~ {membership_firstname} {membership_lastname} ~")

                        member_counter += 1
                        if member_counter == selection_show_this_many_members:
                            break

                    selection_membership_id = int(input(
                        f"Enter Membership ID Of Member To Create User: ")
                    )

                    payload =  {
                                "username": fake_username,
                                "password": fake_password,
                                "role": "member",
                                "membershipId": selection_membership_id,
                                "lastFourOfSSN": membership_4_last_social
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

                print(f"~~~ You Successfully Created {users_created} {user_role.capitalize()} Users ~~~")

        except Exception as e:
            print(e)
            print("\n(Error!) There Was A Problem Creating Users...")

