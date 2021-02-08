#!/usr/bin/env python3
from functions import *
import getpass


identity = 0
user = ""
count = 0
print("Welcome to Quiz Portal !!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
print("***************************************************\n")
print("If you are User,Enter 'U' or if you are super_user , Enter 'S'\n")
print("Don't worry about case sensitive problem\n")

while True:
    input_from_user = input("Enter here: ").lower()
    print()
    if input_from_user == 'u':
        print("*******************************")
        print("\tWELCOME USER\t\n")
        print("*******************************")
        user = "USER"
        identity = 1
        break
    elif input_from_user == 's':
        user = "SUPERUSER"
        break
    else:
        print("Oops !!! , Enter correct parameter\n")

    
if user == 'SUPERUSER':
    while True:
        print("Enter password or secretcode below")
        secret_code = getpass.getpass()

        if decode(secret_code) == "aWFtc3VwZXJ1c2Vy":
            print("*****************************************")
            print("\tWELCOME SUPERUSER\t\n")
            print("*****************************************")
            identity = 2
            break
        else:
            print("Wrong secret code,remaining tries : {}".format(3 - count - 1,"\n"))
            count += 1
          
            if count == 3:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("\tyou have exceeded maximum tries\t")
                print("\texiting the application\t")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                break







