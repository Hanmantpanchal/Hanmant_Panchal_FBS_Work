#2. Print All Palindrome Numbers from 1 to N

number = int(input("how many palindrome you want :"))

temp = number
i = 1

while(i <= temp):
    
    rev = 0 
    
    temp = i
    while(temp > 0):
        d  = temp % 10 
        temp = temp // 10
        rev = rev * 10 + d
    if rev == i:
        print(i)
        
        
    temp = number
    i = i + 1
