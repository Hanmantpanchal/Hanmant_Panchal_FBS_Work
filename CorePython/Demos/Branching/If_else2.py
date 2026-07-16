#program to print username and password

U = 'Hanmant'
P = '1234'

Username = input('enter username ')
Password = input('enter password')

#perform operation 

if(Username==U and Password==P):
    print('login successfully')
else:
    print(f"{Username} and {Password} not match")