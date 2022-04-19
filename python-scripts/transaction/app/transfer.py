import requests

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuZnJlZWQiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjUwMzI2NTA4LCJleHAiOjE2NTE1MzYxMDh9.BjZiqm0ozzxFizdYK94-v08QDS5DvbjEp2aS1teyCFs"}

# returns 1 or 0 to member_account_method to continue or cancel more transactions
def transfer(member_name, member_id):

    selection = True
    while selection:
        try:
            
            print("\nWhat Account To Withdrawal From?\n")

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

            # builds dict of {account_number: account_type} / prints account info
            account_number_dict = {}
            for account_type in accounts_dict:
                account_balance = accounts_dict[account_type]["account_balance"]
                account_number = accounts_dict[account_type]["account_number"]
                print(f"{account_type} ~ Balance: {account_balance} ~ Account Number: {account_number}")
                account_number_dict[account_number] = account_type

            account_to_withdraw = input(f"\nEnter The Account Number To Withdraw From: ")

            amount_to_transfer = int(input(f"\nEnter The Amount To Transfer: "))

            account_to_deposit= input(f"\nEnter The Account Number To Deposit: ")
                
            if account_to_withdraw not in account_number_dict or account_to_deposit not in account_number_dict:
                print("\n(Error!) Please Select Valid Account Numbers...")

            elif amount_to_transfer > accounts_dict[account_number_dict[account_to_withdraw]]["account_balance"]:
                print(f"\n(Error!) There Is Not Enough Funds To Withdrawal {amount_to_transfer}")

            else:
                selection = False

                payload = {
                           "fromAccountNumber": account_to_withdraw,
                           "toAccountNumber": account_to_deposit,
                           "amount": amount_to_transfer,
                           "memo": "Transfering"}  

                # posts transfer
                post_response = requests.post(BASE + "/transactions/transfer", json=payload, headers=headers)

                # parses response
                transfer_status_0 = post_response.json()[0]["status"]
                transfer_status_1 = post_response.json()[1]["status"]
                if transfer_status_0 == "APPROVED" and transfer_status_1 == "APPROVED":
                    print(f"\n{amount_to_transfer} Was Transfered Between {member_name}'s Accounts")
                else:
                    print("\n(Error!) Something Went Wrong Transfering...")

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
            print("\n(Error!) There Was A Problem With Transfer...")
