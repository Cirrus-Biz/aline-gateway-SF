from os import wait
import create_banks
import create_branches
# todo
# ask how many banks to create
# post that many random banks to banks
# ask would you like to add branches to a banks
# get request for list of banks
# choose bank from list
# choose how many branches
# post that to brances of bank


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

        # runs bank creation
        else:

            selection = False
            number_of_banks = selection_number

            create_banks.create_banks(number_of_banks)


    except IndexError:  # out of range
        # logging.error("Selected File Number Was Out Of Range Of Choices")
        print("\n(Error!) Please Select Numbers 0 or 1...")

    except Exception as e:
        # logging.error("There Was A Problem Running The Application")
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")






selection = True
while selection:
    try:

        selection_number = int(input(
            "\n--- Create Branches ---\n"
            "Choose 0 To Skip Branch Creation\n"
            "You Will Choose Which Bank To Add Them To Next\n"
            "Enter Number of Branches: ")
        )

        if selection_number == 0:
            print("\nSkipping Branch Creation...\n")
            selection = False  # terminates while

        elif selection_number < 0:
            print("\n(Error!) Please Select Greater than 0...")

        # runs branch creation
        else:

            selection = False
            number_of_branches = selection_number

            bank_id = create_branches.list_banks()
            create_branches.create_branches(bank_id, selection_number)

    except IndexError:  # out of range
        # logging.error("Selected File Number Was Out Of Range Of Choices")
        print("\n(Error!) Please Select Numbers 0 or 1...")

    except Exception as e:
        # logging.error("There Was A Problem Running The Application")
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")
