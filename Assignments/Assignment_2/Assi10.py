#revers three digit number 
num= int(input("enter the number :"))

#perform operation 

a = num//100
b = (num%100)//10
c = (num%100)%10

#Display result

print(f'{c}{b}{a}')
