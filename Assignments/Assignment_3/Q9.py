#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = int(input("Enter marks of first subject: "))
sub2 = int(input("Enter marks of second subject: "))
sub3 = int(input("Enter marks of third subject: "))
sub4 = int(input("Enter marks of fourth subject: "))
sub5 = int(input("Enter marks of fifth subject: "))

total = sub1 + sub2 + sub3 + sub4 + sub5

if (total >= 90):
    print("First class")
elif (total >= 80):
    print("Second class")
elif total >= 70:
    print("Third class")
elif total >= 60:
    print("Fourth class")
else:
    print("Fail")