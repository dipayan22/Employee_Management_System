import csv
import pandas as pd
import time


USERID="BCREC"
PASSWORD='admin'

def admin():
    tries_left=3

    while tries_left:

        userid=input("Enter the UserID : ")
        user=input("Enter the password : ")
        if user==PASSWORD and userid==USERID:
            print("Permission Granted!!!!!")
            time.sleep(1)
            delete_data()
            time.sleep(2)
            break

        if user!=PASSWORD and userid==USERID:
            print("Wrong Password !!!!!")

        if user==PASSWORD and userid!=USERID:
            print("Wrong userID !!!!!")

        if user!=PASSWORD and userid!=USERID:
            print("Wrong userID and wrong Password  !!!!!")
        
        tries_left-=1
        print("Tries left : ",tries_left)


def delete_data():
    
    df=pd.read_csv('emp_details.csv')
    while 1:
        id=input("Enter the ID of the Employee : ")

        if(df[df.Emp_Id==id].shape[0]==0):
            print("NO DATA FOUND !!!! Please enetr valid Employee ID .")

        else:
            df=df.drop(df[df.Emp_Id==id].index)
            df.to_csv('emp_details.csv',index=False)

            print("Delete Employee ID no. "+id+" Sucessfully.   ")
            break


