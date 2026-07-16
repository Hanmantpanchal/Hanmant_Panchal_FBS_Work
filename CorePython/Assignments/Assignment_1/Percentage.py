#write a program to calculate the percentage of student based on marks of any 5 subjects 

sub1= int(input("enter the marks of sub1 :"))
sub2= int(input("enter the marks of sub2 :"))
sub3= int(input("enter the marks of sub3 :"))
sub4= int(input("enter the marks of sub4 :"))
sub5= int(input("enter the marks of sub5 :"))

Totalmarks =500

#Perform operation 

ObtainedMarks = sub1 + sub2 + sub3 + sub4 + sub5

Percentage = ObtainedMarks/Totalmarks * 100

#Display output 

print(f'percentage of 5 subject is {Percentage} %')


