# once member choosen, need to get member name, accounts and numbers for users
# show account values
# choose deposit, withdraw, transfer between accounts
# have checks to make sure no overdrafts, or can transfer
# complete function and show results

import requests

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}

def member_account_method(member_id, member_name):

    # get member accounts JSON
    get_member_accounts = requests.get(BASE + f"/members/{member_id}/accounts", headers=headers)
    member_accounts_dict = get_member_accounts.json()

    # builds dict of member accounts and values
    # type of account is the key / value dict {account_number: and account_balance:}
    number_of_accounts = len(member_accounts_dict["content"])
    accounts_dict = {}
    for i in range(number_of_accounts):
        account_type = member_accounts_dict["content"][i]["type"]
        account_number = member_accounts_dict["content"][i]["accountNumber"]
        account_balance = member_accounts_dict["content"][i]["balance"]
        accounts_dict[account_type] = {"account_number": account_number, "account_balance": account_balance}

    # prints member account/accounts info
    print(f"\n{member_name} Accounts:")
    for account in accounts_dict:
        account_balance = accounts_dict[account]["account_balance"]
        print(f"{account}: {account_balance}")



    selection = True
    while selection:
        try:
            
            show_this_many_members = int(input(
                f"\n--- Withdraw, Deposit, or Transfer ---\n"
                f"We Will Only Show You Members That Are Not Currently Users\n"
                f"How Many Valid Members Would You Like To Choose From?: ")
            )

            if show_this_many_members < 0:
                print("\n(Error!) Please Select Valid Number...")

            else:

        except Exception as e:
            print(e)
            print("\n(Error!) There Was A Problem In Member Account Functions...")
