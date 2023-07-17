# Python 3.7.8
# regex==2023.6.3
'''Python Project on Email Authentication System using File Handling. 
In this project there will be a menu consist of 3 functions Signup function, Login function,  Forgot Password function. 
To store the Email address and Password permanently we will use a Data.txt file.

pattern1=  ^([a-z\d][a-z\d\.\-_]+[a-z\d]){1,30}@[a-z\d\-]{1,20}\.[a-z]{1,10}(\.[a-z]{1,10})?
pattern2=  ^([a-z\d][a-z\d\.]+[a-z\d]){1,30}@(gmail|yahoo|hotmail){1,20}\.[a-z]{1,10}(\.[a-z]{1,10})?$
pattern3=  ^([a-z]+\.?[a-z\d]+){1,30}@(gmail|yahoo|hotmail){1,20}\.[a-z]{1,10}(\.[a-z]{1,10})?$
pattern4= ^([a-z]+\.?[a-z\d]+){1,30}@[a-z]{1,20}\.[a-z]{1,10}(\.[a-z]{1,10})?$'''

import re

# create a dictionary to store email and password data
d = {}
pattern = r"^([a-z\d]+\.?[a-z\d]+){3,10}@[a-z]{1,20}\.[a-z]{1,10}(\.[a-z]{1,10})?$"

def email_validation( email ):
    if re.search( pattern, email) != None :
        return True
    else:
        return False
    
def password_validation( password ):
    if len(password)<8:
        return False
    elif re.search(r"[a-z]", password) == None:
        return False
    elif re.search( r"[A-Z]", password) == None:
        return False
    elif re.search( r"[0-9]", password) == None:
        return False
    elif re.search( r"[@!#%&_\$,<>\'\"\^\*\-\.\?\|\(\)\\\+]", password) == None:
        return False
    else:
        return True
    
def signup( ):
    email = input("Enter email: ")
    if email_validation(email):
        password = input("(Use 8 or more characters with a mix of letters(upper case and lower case), numbers & symbols)\nEnter password: ")
        if  password_validation(password):
            conform_pass = input("Enter conform password: ")
            if password == conform_pass:
                d[email] = password         # dict[key] = value
                print("Signup successful.")
                with open("Data.txt","w") as file:
                    for keys,values in d.items():
                        file.write("{E}:{Pass}\n".format( E = keys, Pass = values))
            else:
                print("Password and Conform Password does not match.")
                print("Try again.")
        else:
            print("Entered password doesn't met the requirements, please enter a valid password.")
            print("Try again.")
    else:
        print("Entered email address doesn't met the requirements, please enter a valid email.")
        print("Try again.")

def login():
    Email = input("Enter email: ")
    if email_validation(Email):
        if Email in d:
            Password = input("Enter Password: ")
            if Password == d[Email]:
                print("Login Successful.")
            else:
                print("Incorrect Password.")
        else:
            print("Email not found.")
            print("If new user, please signup.")
    else:
        print("Invalid Email.")
        print("Please enter correct email address.")
        


        
def forgot_password():
    email = input("Enter email: ")
    if email_validation(email):
        if email in d:
            #print("Please check your email for instructions to reset your password.")
            print("Email found.")
            n = int(input("Press 1 to set new password: "))
            if(n == 1):
                new_pass = input("Enter new password: ")
                if new_pass == d[email]:
                    print("Old Password and New Password are same")
                    print("Please enter a different Password")
                    return
                if password_validation(new_pass):
                    conform_pass = input("Enter conform password: ")
                    if new_pass == conform_pass:
                        d[email] = new_pass    #dict is updated with new password
                        print("New Password changed successfully")
                        with open("Data.txt","w") as file:
                            for keys,values in d.items():
                                file.write("{E}:{Pass}\n".format( E = keys, Pass = values))
                    else:
                        print("Password and Conform Password does not match.")
                        print("Try again.")
                else:
                    print("Entered password doesn't met the requirements, please enter a valid password.")
                    print("Try again.")
        else:
            print("Email not found.")
    else:
        print("Invalid Email.")
        print("Please enter correct email address.")

#Load data from file.
# main program
with open('Data.txt') as f:
    for line in f:
        (key, val) = line.strip().split(':')
        d[key] = val

while True:
    choice = input("Enter \n1 to signup \n2 to login \n3 to forgot password \n4 to exit: ")
    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        forgot_password()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
