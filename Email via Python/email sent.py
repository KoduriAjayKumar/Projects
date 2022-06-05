import smtplib
sender_email =  input(str("Please enter your email: "))
print("Note: please enter App password only (less secure apps) for gmail users")
password = input(str("Please enter your password: "))
receiver_email = input(str("Please enter recipient email: "))
subject = "Super offer for especially you only, important message"
body = "Hey, greetings from AJ learning academy"
message = input("please enter the message to send: ")

try:
    
    #Opening the connection from  "smtp.gmail.com"  server and  port 587    
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    # Another way of securing the connection via TLS  by  ".starttls()"  method  TLS/SSL.
    #server.starttls()
    # SSL connection  "smtplib.SMTP_SSL("smpt.gmail.com",465) and use  465 port"

    #Authenticating with Gmail.
    server.login(sender_email, password)
    print("Login success")
    #Sending the gmail.
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
    print("Email has been sent to", receiver_email)

except():
    print("""Something went wrong.....
 
             may be incorrect password or emails
             please try again.""")

input("please press enter to exit")
