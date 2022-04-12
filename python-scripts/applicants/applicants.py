import sys
sys.path.append("/Users/stephenfreed/Projects/Capstone/Cirrus-Biz/aline-gateway-SF/python-scripts//Users/stephenfreed/Projects/Capstone/Cirrus-Biz/aline-gateway-SF/python-scripts/applicants/")

from app import create_applicants

# asks how many applicants you would like to create
# calls create_applicants
selection = True
while selection:
    try:

        selection_number = int(input(
            "\n--- Create Applicants ---\n"
            "Choose 0 To Skip Applicants Creation\n"
            "Enter Number of Applicants To Create: ")
        )

        if selection_number == 0:
            print("\nSkipping Applicants Creation...\n")
            selection = False  # terminates while

        elif selection_number < 0:
            print("\n(Error!) Please Select Greater than 0...")

        else:
            selection = False
            number_of_applicants = selection_number

            create_applicants.create_applicants(number_of_applicants)

    except IndexError:  # out of range
        print("\n(Error!) Please Select Numbers 0 or Greater...")

    except Exception as e:
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")

