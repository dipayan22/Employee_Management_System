'''
We will first search for data using different search methods for different categories then view or print it on console 
'''


import csv
import pandas as pd


# print("Search by category :-")
#             print("1. EmpId") # generates unique output(only 1)
#             print("2. Name") # may generate 1 or more based on pattern matching
#             print("3. Age")
#             print("4. Gender")
#             print("5. Designation")
#             print("6. Salary")

def printData(opt):

    user=input("Enter the "+Dict[opt]+" of the Employee : ")

    df=pd.read_csv('emp_details.csv')
    data=df.loc[:,~df.columns.isin(['Email','Phno'])]

    print(data[data[Dict[opt]]==user])

def adminPrint(opt):
    user=input("Enter the "+Dict[opt]+" of the Employee : ")

    df=pd.read_csv('emp_details.csv')

    print(df[df[Dict[opt]]==user])


Dict={
    '1':'Emp_Id',
    '2':'Name',
    '3':'Age',
    '4':'Gender',
    '5':'Designation',
    '6':'salary'}

# printData(2)
# opt=2
# print(Dict['1'])