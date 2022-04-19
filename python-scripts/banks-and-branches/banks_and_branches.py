import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(dir_path)

from app import create_banks, query_banks, create_branches


# select number of banks to create
# runs create_banks module with input number
selection = True
while selection:
    try:

        selection_number = int(input(
            "\n--- Create Banks ---\n"
            "Choose 0 To Skip Bank Creation\n"
            "Enter Number of Banks: ")
        )

        if selection_number == 0:
            print("\nSkipping Bank Creation...\n")
            selection = False  # terminates while

        elif selection_number < 0:
            print("\n(Error!) Please Select Greater than 0...")

        else:
            selection = False
            number_of_banks = selection_number

            create_banks.create_banks(number_of_banks)

    except IndexError:  # out of range
        print("\n(Error!) Please Select Numbers 0 or Greater...")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")


# select bank to add branches too
# select how many branches to add
selection = True
while selection:
    try:

        selection_number = int(input(
            "\n--- Create Branches ---\n"
            "Choose 0 To Skip Branch Creation\n"
            "Enter Any Number > 0 To Create Branches: ")
        )

        if selection_number == 0:
            print("\nSkipping Branch Creation...\n")
            selection = False  # terminates while

        elif selection_number < 0:
            print("\n(Error!) Please Select Greater than 0...")

        else:
            selection = False

            selected_bank_id = query_banks.select_bank()

            create_branches.create_branches(selected_bank_id)

    except IndexError:  # out of range
        print("\n(Error!) Please Select Number > 0...")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")
