import re
pattern = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"


def email_validation(Email):
    if re.search(pattern, Email):
        return 1
    else:
        return 0


def password_valiadtion(flag, Password):

    if not re.search('[a-z]', Password):
        flag = 0
    if not re.search('[0-9]', Password):
        flag = 0
    if not re.search('[A-Z]', Password):
        flag = 0
    if not re.search('[$@#!]', Password):
        flag = 0
    if (len(Password) < 5 or len(Password) > 16):
        flag = 0
    if flag == 1:
        return 1
    else:
        return 0


def login(email, password):
    if(email_validation(email)):
        file1 = open("Database.txt", "r")
        flag = 0
        index = 0
        temp = 0
        temp1 = 0
        for line in file1:
            index += 1
            if email in line:
                flag = 1
                temp = 1
                break
        if(temp == 0):
            print("username doesnt exists")
        if(flag == 1):
            password = password.strip()
            str = email+','+password
            for line in file1:
                index += 1
                if str in line:
                    print("Login Successfulll")
                    temp1 = 1
                    break
            if(temp1 == 0):
                print("invalid password")

    else:
        print("Entered username doesn't met the requirements,please enter a valid email")
        print('try again')
        home()
        

def registration(email, password):
    if(email_validation(email)):
        if(password_valiadtion(flag1, passwd)):
            file1 = open("Database.txt", "r")
            flag = 0
            index = 0
            for line in file1:
                index += 1
                if email in line:
                    flag = 1
                    break
            if(flag == 0):
                new_line = f"Username:{email},Password:{passwd}\n"
                with open("Database.txt", "a") as a_file:
                    # a_file.write("\n")
                    a_file.write(new_line)
                    file1.close()
                    print("Your registration is Successfull")
            else:
                print("username already exist")
                print('try again')
                home()

        else:
            print(" Entered password doesn't met the requirements, please enter a valid password")
            print("Try again")
            home()
    else:
        print("Entered username doesn't met the requirements, please enter a valid email")
        print("try again")
        home()
        

def forgot_password(email):
    if(email_validation(email)):
        file1 = open("Database.txt", "r")
        flag = 0
        index = 0
        temp = 0
        temp1 = 0
        for line in file1:
            index += 1
            if email in line:
                print(line)
                flag = 1
                temp = 1
                break
        if(temp == 0):
            print("username doesnt exists")
        if(flag == 1):
            print("The above password exist with the the entered username")
            dec = input(
                "Do you want to use the above password or want to set new password?[Y/N")
            if(dec == 'Y' or dec == "y"):
                print("Thank You")
            else:
                new_pass = input("Please enter new password")
                if(password_valiadtion(flag1, new_pass)):
                    new_line = f"Username:{email},Password:{new_pass}\n"
                    with open("Database.txt", "a") as a_file:
                        # a_file.write("\n")
                        a_file.write(new_line)
                        file1.close()
                        print("New Password Created successfully")
                else:
                    print("password doesn't met the requirements,please enter a valid password")
    else:
        print("username doesn't met the requiremets please enter a valid mail id")

def home():
 print("Welcome to dash board!")   
 if __name__ == '__main__':
    flag1 = 1
    user_input = int(
        input("Enter the number\n Press 1 for Registration \n press 2 for login \n press 3 for forgot password\n"))
    if(user_input == 1):
        email = input("Enter ur email id: \n")
        passwd = input("Create ur password: \n")
        passwd1 = input("Confrim password: \n")
        if passwd == passwd1:
            registration(email, passwd)
        else:
            print("Password and confrim password does not match, Try again!")
            home()
    elif(user_input == 2):
        email = input("Enter ur email id: \n")
        passwd = input("Enter ur password: ")
        login(email, passwd)
        
    
    elif(user_input == 3):
        email = input("please enter the mail id: ")
        forgot_password(email)
    else:
        print("invalid choice")
home()
