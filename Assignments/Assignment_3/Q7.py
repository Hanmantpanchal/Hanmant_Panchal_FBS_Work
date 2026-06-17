#7. Write a program to check if user has entered correct userid and password.

userid = input("Enter your userid: ")
password = input("Enter your password: ")

if((userid == "admin") and (password == "admin123")):
    print("Login Successful")
else:
    print("Invalid Credentials")