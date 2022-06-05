import random
import smtplib

#Declare digits variable to store all digits.
digits = "0123456789"

#Declare a empty string variable to store OTP with random digits.
OTP = ""
for i in range(6):
    OTP += digits[random.randint(0,9)]

otp = OTP
message = "Your OTP number is "+otp



my_email = input("Please enter your email: ")
password = input("Please enter your Password: ")
print()
print("Note: Please enter google app password for gmail users as smptlib code works for only less secure apps.")
receiver_email = input("Please enter the email to send OTP: ")

#Opening the connection from  "smtp.gmail.com"  server.
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()

server.starttls()   #Securing the connection via TLS.

#Authenticating your email.
server.login(my_email, password)
print("Login success.")
print()

#Sending the email
server.sendmail(my_email, receiver_email, message)
server.quit()

print("OTP has been sent to", receiver_email)


ans = input("Please enter your OTP: ")

if ans == otp:
    print("Your email: %s is verified" %(receiver_email))
else:
    print("Incorrect OTP! \nPlease check your OTP again.")
