# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.




user_id = "hanmantpanchal"
password = "Pass@1531"

for i in range(3):
    user = input("Enter the userid: ")
    pin = input("Enter the password: ")

    if user == user_id and pin == password:
        print("Login successfully")
        break
    else:
        print("Invalid userid or password")

else:
    print("Try after few minutes... BYE")



# user_id = "parmeshwarpanchal"
# password = "Pass@1234"

# user = input("enter the userid :")
# pin = input("enter the password :")

# if(user==user_id and pin==password):
#         print("login successfully")
# elif(user!=user_id and pin!=password):
#     for i in range(1,3):
#         print("enter valid :")
#         user = input("enter the userid :")
#         pin = input("enter the password :")
#         if user==user_id and pin==password:
#             print("login successfully")
#             break
#     else:
#         print("Try after few minutes  .... BYE ")            
# else:
#     for i in range(3):
#         print("enter valid :")
#         user = input("enter the userid :")
#         pin = input("enter the password :")
#         if user==user_id and pin==password:
#             print("login successfully")
#             break
#     else:
#         print("Try after few minutes  .... BYE ")




# Enter the userid: hanmantpanchal
# Enter the password: Pass@1531
# Login successfully


# Enter the userid: abc
# Enter the password: 123
# Invalid userid or password

# Enter the userid: xyz
# Enter the password: 456
# Invalid userid or password

# Enter the userid: test
# Enter the password: test
# Invalid userid or password

# Try after few minutes... BYE