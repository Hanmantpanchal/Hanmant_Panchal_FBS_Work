x=10
y=10
z=20
li1=[10,20,30]
li2=[10,20,30]



#1. is

print(x is y) # int is immutable so it is not change 
print(id(x))
print(id(y))
print(li1 is li2) # list is mutable it can be change 
print(id(li1))
print(id(li2))



#2. is not 

print(li1 is not li2)
print(x is not y)