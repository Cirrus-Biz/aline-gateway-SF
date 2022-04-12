import sys
sys.path.append("/Users/stephenfreed/Projects/Capstone/Cirrus-Biz/aline-gateway-SF/python-scripts/applications/")

from app import create_applications

# asks how many applications you would like to create
# calls create_applications where you choose account type
selection = True
while selection:
    try:

        selection_number = int(input(
            "\n--- Create Applications ---\n"
            "Choose 0 To Skip Applicatoins Creation\n"
            "Enter Number of Applications: ")
        )

        if selection_number == 0:
            print("\nSkipping Application Creation...\n")
            selection = False  # terminates while

        elif selection_number < 0:
            print("\n(Error!) Please Select Greater than 0...")

        else:
            selection = False
            number_of_applications = selection_number

            create_applications.create_applications(number_of_applications)

    except IndexError:  # out of range
        print("\n(Error!) Please Select Numbers 0 or Greater...")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")


