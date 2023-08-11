'''
Simple password & captcha implementation

functions present :-
    user_entry()
    generate_captcha_img()
    captcha() --> returns a boolean value confirming if user passed the test or not
    ============
    demand_password() --> returns a boolean value

***Only 3 tries given to user for captcha and unlimited refresh given to user else  user FAILS test.
***Only 3 tries allowed and at the same time must pass the captcha test

TODO
====

* Hide the user entered password if possible later
'''

import random


# ========================= Generate captcha image ==========================

def generate_captcha_img():
    # generate a random 4 digit number
    r = random.randint(1000, 9999)
    print("\nEnter the captcha carefully(for security reasons) :-\n")

    #three unit space for each element in list(adjust space accordingly)
    numdict={
        '1':['   ', ' | ', ' | '],
        '2':[' _ ', ' _|', '|_ '],
        '3':['__ ', '__|', '__|'],
        '4':['   ', '|_|', '  |'],
        '5':[' _ ', '|_ ', ' _|'],
        '6':[' _ ', '|_ ', '|_|'],
        '7':['__ ', '  |', '  |'],
        '8':[' _ ', '|_|', '|_|'],
        '9':[' _ ', '|_|', '  |'],
        '0':[' _ ', '| |', '|_|']
    }

    # print the 4 digit number in 7 segmented display format like clock time
    for i in range(3):
        for j in str(r):
            print(numdict[j][i], end=" ")
        print()

    # return the random number generated 
    return r


# ========================= User entry function for visible captcha =========================
def user_entry(num):
    actual_ans = num
    # max three tries allowed for each refresh(unlimited refresh)
    tries_left = 3
    while tries_left :
        ch = input("\nEnter captcha shown above (to refresh captcha press 'r' or 'R')\nAny other input will be considered invalid : ")
        if ch in ['r', 'R']:
            # call captcha again for new number and update the number of tries
            actual_ans = generate_captcha_img()
            tries_left = 3

        elif ch.isdigit():
            # if valid entry
            if int(ch) == actual_ans:
                return True

            # if not valid entry
            print("\nPlease enter a valid input !\n ")
            tries_left -= 1
            print("Tries left : ", tries_left)

        else:
            print("\nPlease enter a valid input !\n ")
            tries_left -= 1
            print("Tries left : ", tries_left)

    # no more tries left
    return False


#======================== MAIN CAPTCHA FUNCTION =======================

def captcha():
    # generate the image
    ans_to_captcha = generate_captcha_img()

    # ask user to enter the dislayed value and return at end if he suceeds in 3 tries
    return user_entry(ans_to_captcha)











PASSWORD = "admin"

# ***************************** DEMAND PASSWORD FROM USER *******************************
def demand_password():
    tries_left = 3
    while tries_left:
        password = input("Enter the password : ")
        if password == PASSWORD:
            return captcha()
        tries_left -=1
        print("Tries left : ", tries_left)
    return False
