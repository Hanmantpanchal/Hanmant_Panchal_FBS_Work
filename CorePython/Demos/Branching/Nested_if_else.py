#program to find the valid age for marriage for male and female 

gender=input('enter the gender (M/F) :')
age = int(input('enter the gender :' ))

#perform operation

if(gender=='F'):
    if(age>=18):
        print(' Female Eligible for marriage ')
    else:
        print('Female not eligible ')
else:
    if(age>=21):
        print(' Male Eligible for marriage ')
    else:
        print('Male not eligible ')
        