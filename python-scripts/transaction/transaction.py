import requests
import sys
from app import member_account_method

sys.path.append("/Users/stephenfreed/Projects/Capstone/Cirrus-Biz/aline-gateway-SF/python-scripts/transaction/")

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuZnJlZWQiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjUwMzI2NTA4LCJleHAiOjE2NTE1MzYxMDh9.BjZiqm0ozzxFizdYK94-v08QDS5DvbjEp2aS1teyCFs"}


selection = True
while selection:
    try:

        selection_number = int(input(
            "\n--- Transaction Producer ---\n"
            "Choose 0 To Skip Transaction Creation\n"
            "How Many Members and Accounts Would You Like To Choose From?: ")
        )

        if selection_number == 0:
            print("\nSkipping Transaction Creation...\n")
            selection = False  # terminates while

        elif selection_number < 0:
            print("\n(Error!) Please Select Valid Number...")

        else:
            selection = False


            # creates dict of all members on first page
            get_members = requests.get(BASE + "/members", headers=headers)
            members_dict = get_members.json()

            # gets the paginated JSON and adds to original members_dict
            number_of_pages = get_members.json()["totalPages"]
            for i in range(1, number_of_pages):
                get_page = requests.get(BASE + f"/members/?page={i}", headers=headers)
                get_page_dict = get_page.json()

                # adds dict record to original dictionary to parse later
                number_in_content = len(get_page_dict["content"])
                for i in range(number_in_content):
                    record = get_page_dict["content"][i]
                    members_dict["content"] += [record]

            # builds dict of members by id with key dict {name: and account_types:}
            number_of_members_size = len(members_dict["content"])
            members_info_dict = {}
            for i in range(number_of_members_size):
                member_id = members_dict["content"][i]["id"]
                member_firstname = members_dict["content"][i]["applicant"]["firstName"]
                member_lastname = members_dict["content"][i]["applicant"]["lastName"]

                # get member accounts by member_id
                get_member_accounts = requests.get(BASE + f"/members/{member_id}/accounts", headers=headers)
                get_member_accounts_dict = get_member_accounts.json()

                # builds list of member account types
                number_in_member_accounts_content = len(get_member_accounts_dict["content"])
                member_account_types = []
                for i in range(number_in_member_accounts_content):
                    account_type = get_member_accounts_dict["content"][i]["type"]
                    member_account_types.append(account_type)

                # adds member_id key with {name: and account_types:} dict as value to member_info_dict
                member_name = member_firstname + " " + member_lastname
                members_info_dict[member_id] = {"name": member_name, "account_types": member_account_types}

            # loops through member_info_dict to print as many members based on user input
            # builds list of id's to check valid user input
            member_id_list = []
            member_print_count = 0
            for id in members_info_dict:
                member_id_list.append(int(id))  # appends id to member_id_list
                name = members_info_dict[id]["name"]
                accounts = members_info_dict[id]["account_types"]
                print(f"Member ID: {id} ~ {name} ~ {accounts}")
                member_print_count += 1
                
                if member_print_count >= selection_number:
                    break


            # gets user input for member id / validates it is in the list of member id's
            valid_member_id = True
            selection_member_number = -1
            while valid_member_id:

                selection_member_number = int(input("\nChoose Member ID To Withdraw, Deposit, or Transfer: "))

                if selection_member_number in member_id_list:
                    valid_member_id = False 
                    continue

                print("\nThat Was Not A Valid Membership ID Try Again...\n")

            # calls member_account_method with member_id and member_name as parameters
            selection_name = members_info_dict[selection_member_number]["name"]
            member_account_method.member_account_method(selection_member_number, selection_name)        

    except IndexError:  # out of range
        print("\n(Error!) Please Select Numbers 0 or Greater...")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")
