import requests
from random import randint
from faker import Faker

fake = Faker()

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}


def create_members():

    selection = True
    while selection:
        try:
            
            show_this_many_members = int(input(
                f"\n--- Create Member Users ---\n"
                f"We Will Only Show You Members That Are Not Currently Users\n"
                f"How Many Valid Members Would You Like To Choose From?: ")
            )

            if show_this_many_members < 0:
                print("\n(Error!) Please Select Valid Number...")

            else:

                selection = False

                # creates dict of all users on first page
                get_users = requests.get(BASE + "/users", headers=headers)
                users_dict = get_users.json()

                # gets the paginated JSON and adds to original dict
                number_of_pages = get_users.json()["totalPages"]
                for i in range(1, number_of_pages):
                    get_page = requests.get(BASE + f"/users/?page={i}", headers=headers)
                    get_page_dict = get_page.json()

                    # adds dict record to original dictionary to parse later
                    number_in_content = len(get_page_dict["content"])
                    for i in range(number_in_content):
                        record = get_page_dict["content"][i]
                        users_dict["content"] += [record]

                # builds list of member id's from users dict to check later
                number_of_users_size = len(users_dict["content"])
                user_member_id_list = []
                for i in range(number_of_users_size):
                    role = users_dict["content"][i]["role"]

                    # checks since admins don't have memberships
                    if role == "MEMBER":
                        current_user_member_id = users_dict["content"][i]["memberId"] 
                        user_member_id_list.append(current_user_member_id)

                # creates dict of all available members
                get_members = requests.get(BASE + "/members", headers=headers)
                members_dict = get_members.json()

                # builds list of valid member id's not in users
                member_id_list = []
                member_counter = 0
                for member in members_dict["content"]:

                    membership_id = member["id"]
                    membership_member_id = member["membershipId"]
                    membership_social = member["applicant"]["socialSecurity"]
                    membership_firstname = member["applicant"]["firstName"]
                    membership_lastname = member["applicant"]["lastName"]

                    if membership_id not in user_member_id_list:

                        member_id_list.append(membership_member_id)

                        print(f"\nMember: Member_ID:{membership_member_id} ~ {membership_firstname} {membership_lastname} ~")

                        member_counter += 1

                    # caps number of members to show based on used input
                    if member_counter == show_this_many_members:
                        break

                valid_member_id = True
                selection_membership_id = ""
                while valid_member_id:

                    selection_membership_id = input(f"Enter Membership ID Of Member To Create User: ")

                    if selection_membership_id in member_id_list:
                        valid_member_id = False 
                        continue

                    print("\nThat Was Not A Valid Membership ID Try Again...\n")

                get_members = requests.get(BASE + f"/members/{selection_membership_id}", headers=headers)
                member_info_dict = get_members.json()

                user_membership_id = member_info_dict["membershipId"]
                # user_firstname = member_info_dict["applicant"]["firstName"]
                # user_lastname = member_info_dict["applicant"]["lastName"]
                # user_email = member_info_dict["applicant"]["email"]
                user_social = member_info_dict["applicant"]["socialSecurity"]
                last_4_of_social = user_social[-4:]

                # creates data outside of payload to avoid JSON object errors
                fake_username =  str(fake.first_name()) + str(randint(100,999))
                fake_password = str(randint(100000000000,199999999999)) + "a3!A"

                payload =  {
                            "username": fake_username,
                            "password": fake_password,
                            # "email": user_email,
                            # "firstname": user_firstname,
                            # "lastname": user_lastname,
                            "role": "member",
                            "membershipId": user_membership_id,
                            "lastFourOfSSN": last_4_of_social
                            }                       

                # posts data to endpoint
                response = requests.post(BASE + "/users/registration", json=payload, headers=headers)

                # parses data from return JSON
                users_id = response.json()["id"]
                users_firstname = response.json()["firstName"]
                users_lastname = response.json()["lastName"]
                users_role = response.json()["role"]

                print(f"\nCreated User: ID:{users_id} Role:{users_role} ~ {users_firstname} {users_lastname} ~")

            print(f"~~~ You Successfully Created A Member User ~~~")

        except Exception as e:
            print(e)
            print("\n(Error!) There Was A Problem Creating Users...")

