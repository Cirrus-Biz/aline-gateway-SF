import sys
sys.path.append("/Users/stephenfreed/Projects/Capstone/Cirrus-Biz/aline-gateway-SF/python-scripts/users/")

from app import create_admins, create_members

selection = True
while selection:
    try:

        selection_number = int(input(
            "\n--- Create Users ---\n"
            "Choose 0 To Skip Users Creation\n"
            "Choose 1 To Create Admin Users\n"
            "Choose 2 To Create Member User\n"
            "Enter Type of User: ")
        )

        if selection_number == 0:
            print("\nSkipping User Creation...\n")
            selection = False  # terminates while

        elif selection_number < 0 or selection_number > 2:
            print("\n(Error!) Please Select Valid Number...")

        else:
            selection = False

            if selection_number == 1:
                create_admins.create_admins()
            elif selection_number == 2:
                create_members.create_members()
            else:
                print("\n(Error!) Please Restart and Try Again...")

    except IndexError:  # out of range
        print("\n(Error!) Please Select Numbers 0 or Greater...")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")

