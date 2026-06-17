#8. Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)

import random

u_id = 'Hanmant'
u_pass = 'Pass@1234'

username = input('Enter the username: ')
password = input('Enter the password: ')

if (u_id == username and u_pass == password):
    captcha = random.randint(1000, 9999)
    print(captcha)

    OTP = int(input('Enter the OTP: '))

    if (captcha == OTP):
        print('Successfully login')
    else:
        print('Failed')

else:
    print('Enter valid username and password')