import requests

BASE = "http://127.0.0.1:8080/api"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdGVwaGVuIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY0OTY4NTcxNCwiZXhwIjoxNjUwODk1MzE0fQ.Xn8swsXW4P8kEbrJQWDwqGwFQ0SdO6_d1_WM8kmaUxQ"}
 

# returns bank ID selected by user
def select_bank():

    selection = True
    while selection:
        try:

            # gets banks in JSON format / converts to python dict
            get_banks = requests.get(BASE + "/banks", headers=headers)
            get_banks_dict = get_banks.json()

            print(
                "\n--- Select Bank ---\n"
                "Select the Bank ID To Add Branches\n"
                  )

            # prints parsed info from get_banks_dict for each bank to display to user
            for bank_info in get_banks_dict["content"]:
                bank_id = bank_info["id"]
                bank_address = bank_info["address"]
                bank_city = bank_info["city"]
                bank_state = bank_info["state"]
                print(f"Select {bank_id}: {bank_address}, {bank_city}, {bank_state}")

            selection_number = int(input(
                "Enter Bank ID: ")
            )


            # sends get request to check if user input is valid bank ID
            check_bank_id = requests.get(BASE + f"/banks/id/{selection_number}", headers=headers)
            if check_bank_id.status_code != 200:
                print("\n(Error!) Please Select Valid Bank ID...")
            else:
                selection = False
                return selection_number

        except Exception as e:
            print(e)
            print("\n(Error!) There Was A Problem Quarrying Banks...")
