'''
All the updation functions for code 
'''

import csv

def update(id,a):

    f=open("emp_details.csv",'r')
    found=0


    csvr=csv.reader(f)

    ml=[]
    for r in csvr:
        if(r[0]==id):
            if a==1:
                r[1]=input("Enter the new name of the Employee  :")
            if a==2:
                r[2]=input("Enter the new designation of the Employee  :")
            if a==3:
                r[3]=input("Enter the new salary of the Employee  :")
            if a==4:
                r[4]=input("Enter the new age of the Employee  :")
            if a==5:
                r[6]=input("Enter the new Email id of the Employee  :")
            if a==6:
                r[7]=input("Enter the new Phone no. of the Employee  :")

            found=1

        ml.append(r)


    if found==0:
        print("No data Found!!!!")

    else:
        f=open("emp_details.csv","w",newline="")
        csvr=csv.writer(f)
        csvr.writerows(ml)
        f.close()
               
def update_data():

    id=input("Enter the ID of the Employee : ")

    

    while 1:

        print("1. Update Name ")
        print("2. Update Designation")
        print("3. Update Salary")
        print("4. Update Age")
        print("5. Update Email")
        print("6. Update Phone No. ")

        a=int(input("Enter your choice :  "))

        update(id,a)

        x=input("Do you want update anything (y/n) : ")

        if x=='y':
            pass
            # continue

        # b=b+1

        if x=='n':
            break

