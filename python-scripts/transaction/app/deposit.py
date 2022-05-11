import os
import requests
from dotenv import load_dotenv, find_dotenv

# loads bearer token from .env
load_dotenv(find_dotenv())
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
HOST = os.environ.get("HOST")

BASE = f"http://{HOST}:8080/api"
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

# returns 1 or 0 to member_account_method to continue or cancel more transactions
def deposit(member_name, member_id):

    print("\nWhat Account To Deposit Into?\n")

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

    # prints account info and builds list of valid accounts for later validations
    account_number_list = []
    for account_type in accounts_dict:
        account_balance = accounts_dict[account_type]["account_balance"]
        account_number = accounts_dict[account_type]["account_number"]
        print(f"{account_type} ~ Balance: {account_balance} ~ Account Number: {account_number}")
        account_number_list.append(account_number)

    selection = True
    while selection:
        try:
            
            account_number_selection = input(f"\nEnter The Account Number To Deposit: ")

            amount_to_deposit = int(input(f"\nEnter The Amount To Deposit: "))

            if account_number_selection not in account_number_list:
                print("\n(Error!) Please Select Valid Account Number...")

            else:
                selection = False

                payload = {
                           "type": "DEPOSIT",
                           "method": "ATM",
                           "amount": amount_to_deposit,
                           "merchantCode": "111111",
                           "merchantName": "Merchant Name",
                           "description": "Merchant Description",
                           "accountNumber": account_number_selection}

                # posts deposit transaction
                post_response = requests.post(BASE + "/transactions", json=payload, headers=headers)

                # parses response
                deposit_status = post_response.json()["status"]
                if deposit_status == "APPROVED":
                    print(f"\nDeposited {amount_to_deposit} to {member_name}'s Account: {account_number_selection}")
                else:
                    print("\n(Error!) Something Went Wrong Depositing...")

                # get account details again
                # ask if you would like to make another transaction:
                get_member_account = requests.get(BASE + f"/members/{member_id}/accounts", headers=headers)
                get_member_account_dict = get_member_account.json()

                # builds dict of member accounts and values
                # type of account is the key / value dict {account_number: and account_balance:}
                number_of_accounts = len(get_member_account_dict["content"])
                accounts_dict = {}
                for i in range(number_of_accounts):
                    account_type = get_member_account_dict["content"][i]["type"]
                    account_number = get_member_account_dict["content"][i]["accountNumber"]
                    account_balance = get_member_account_dict["content"][i]["balance"]
                    accounts_dict[account_type] = {"account_number": account_number, "account_balance": account_balance}

                # prints member account/accounts info
                print(f"\n{member_name} Accounts:")
                for account in accounts_dict:
                    account_balance = accounts_dict[account]["account_balance"]
                    print(f"{account}: {account_balance}")


                more_transactions_selection  = int(input(
                    "\n--- Would You Like Another Transaction? ---\n"
                    "Choose 0 To Skip Transaction Creation\n"
                    "Choose 1 For Another Transaction Creation\n"
                    "Enter Selection: ")
                )

                if more_transactions_selection == 1:
                    return 1
                else:
                    return 0

        except Exception as e:
            print(e)
            print("\n(Error!) There Was A Problem With Deposit...")
