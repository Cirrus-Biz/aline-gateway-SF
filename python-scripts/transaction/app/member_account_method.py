import os
import requests
import sys
from dotenv import load_dotenv, find_dotenv
from app import deposit, withdrawal, transfer

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(dir_path)

# loads bearer token from .env
load_dotenv(find_dotenv())
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

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
            
            method_choice = int(input(
                f"\n--- Withdraw, Deposit, or Transfer ---\n"
                f"Select 0 To Quit\n"
                f"Select 1 For Withdrawal\n"
                f"Select 2 For Deposit\n"
                f"Select 3 For Transfer\n"
                f"Enter Selection: ")
            )

            if method_choice < 0 or method_choice > 3:
                print("\n(Error!) Please Select Valid Number...")

            elif method_choice == 0:
                print("\nYou Have Quit The Application...")
                selection = False

            elif method_choice == 1:
                if number_of_accounts == 0:
                    print("\n(Error!) This Account Has No Accounts...")
                else:
                    continue_selection = withdrawal.withdrawal(member_name, member_id)
                    if continue_selection == 1:  # continue with other transactions
                        pass
                    else:
                        selection = False

            elif method_choice == 2:
                if number_of_accounts == 0:
                    print("\n(Error!) This Account Has No Accounts...")
                else:
                    continue_selection = deposit.deposit(member_name, member_id)
                    if continue_selection == 1:  # continue with other transactions
                        pass
                    else:
                        selection = False

            elif method_choice == 3:
                if number_of_accounts < 2:
                    print("\n(Error!) This Member Does Not Have More Than One Account To Transfer...")
                else:
                    continue_selection = transfer.transfer(member_name, member_id)
                    if continue_selection == 1:  # continue with other transactions
                        pass
                    else:
                        selection = False
                    
        except Exception as e:
            print(e)
            print("\n(Error!) There Was A Problem In Member Account Functions...")
