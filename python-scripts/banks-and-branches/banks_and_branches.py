import os
import sys
sys.path.append("/Users/stephenfreed/Projects/Capstone/Cirrus-Biz/aline-gateway-SF/python-scripts/")

from app import create_banks
from app import create_branches

banks_created_id_array = []

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

            # returns array of bank id's that were created
            banks_created_id_array = create_banks.create_banks(number_of_banks)

    except IndexError:  # out of range
        print("\n(Error!) Please Select Numbers 0 or 1...")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")


selection = True
while selection:
    try:

        selection_number = int(input(
            "\n--- Create Branches ---\n"
            "Choose 0 To Skip Branch Creation\n"
            "You Will Create A Branch For Every Bank You Just Created\n"
            "Enter Any Number > 0 To Create Branches: ")
        )

        if selection_number == 0:
            print("\nSkipping Branch Creation...\n")
            selection = False  # terminates while

        elif selection_number < 0:
            print("\n(Error!) Please Select Greater than 0...")

        else:
            selection = False

            create_branches.create_branches(banks_created_id_array)

    except IndexError:  # out of range
        print("\n(Error!) Please Select Numbers 0 or 1...")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")
