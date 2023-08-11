'''
Contains UI of the Employee management system and function calls of different modules

    EmpId | Name | Age | Gender | Designation | Salary | Email | Phno
    _________________________________________________________________
          |      |     |        |             |        |       |

'''

# import custom_modules
import os
import time
from custom_modules import newentry as NE
from custom_modules import printdata as PD
from custom_modules import update as UP
from custom_modules import password as PW
from custom_modules import deleteData as DD




def main():
    while 1 :

        print("<<"*50 + "\n\n")
        print("1. Enter new employee data")
        print("2. Update exisitng data")
        print("3. View data")
        print("4. Delete data")
        print("5. Exit")
        print("\n\n" + ">>"*50)

        inp = input("Enter choice : ")

        # ***************************** Insert record ***************************** 
        if inp == "1":
            # call the function in dataentry.py
            NE.add_new_data()
        # ***************************** Update record ***************************** 
        elif inp == "2":
            # call the function in update.py
            UP.update_data()
        # ***************************** Viewing data ***************************** 
        elif inp == "3":
            print("Search by category :-")
            print("1. EmpId") # generates unique output(only 1)
            print("2. Name") # may generate 1 or more based on pattern matching
            print("3. Age")
            print("4. Gender")
            print("5. Designation")
            print("6. Salary")
            # no searching on email or phone

            # ========================== Criteria selection for Viewing data ==========================
            inp = None
            allowedval = ["1","2","3","4","5","6"]
            while inp not in allowedval:
                inp = input("Select criteria to search data : ")
                if inp not in allowedval:
                    print("Incorrect Selection!!!Try again.")


                else:
                    PD.printData(inp)

            print("\n\n")
            # ========================== Admin privilege for viewing personal data ==========================
            adminprivilege = None
            allowedval = ['y','n','Y','N']
            while adminprivilege not in allowedval :
                adminprivilege = input("View Employee mail and phone(y/n) : ")
                if adminprivilege not in allowedval:
                    print("Incorrect Input!!! Please try again.")

            if adminprivilege == 'y':
                # call the secret passcode and catcha functions
                if PW.demand_password():
                    print("\n\nAdmin Privileges granted!!!\n\n")
                    
                    PD.adminPrint(inp)

                else:
                    adminprivilege = 'n'
                    print("\n\nSorry!!! Cannot grant admin privileges\n\n")

            time.sleep(2)

        # ***************************** Delete data code **********************

        elif inp=="4":
            # pass
            DD.admin()

        # ***************************** Exit code *****************************
        elif inp=="5":
            break
        # ***************************** Incorrect selection *****************************
        else:
            print("Invalid Choice!!!\n\n Refreshing Page")

        # ~~~~~~~~~~~ REFRESH PAGE ~~~~~~~~~~~~~
        os.system("cls")
    
    # if someone exits loop breaks then function returns to caller
    return





if __name__ == "__main__":
    main()
    # End of session
    time.sleep(2)
    print("\n"*5 + "~"*50 + "\nProgram Terminated. Changes Saved!\n"+ "~"*50)
