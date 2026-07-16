#swap two number without using third variable

a= int(input("Enter a number : "))
b= int(input("Enter b number: "))
#perform operation  

a = a+b
b = a-b
a = a-b

#Diplay the result
print("After swapping: ")
print(f'a = {a} , b = {b}')