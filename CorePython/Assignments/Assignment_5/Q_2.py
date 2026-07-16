# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.


n = int(input("Enter the number of students : "))

student = 1
max = 500
total_of_percentage = 0

while student<=n:
    print(f"enter student{student} marks :")

    sub1=int(input("enter the marks of sub1 :"))
    sub2=int(input("enter the marks of sub2 :"))
    sub3=int(input("enter the marks of sub3 :"))
    sub4=int(input("enter the marks of sub4 :"))
    sub5=int(input("enter the marks of sub5 :"))

    total = sub1 + sub2 +sub3 + sub4 + sub5
    print(f"total of {student} student :  marks {total}")

    percentage = (total/max)*100
    print(f"percentage of {student} student :  percentage : {percentage:.2f}%")

    total_of_percentage =total_of_percentage+percentage
    print(f"total percentage of {student} student : {total_of_percentage::.2f}%")

    avg = total_of_percentage/n
    print(f"average of {student} student : {avg }")

    student = student + 1 
   
    


# n = int(input("Enter number of students: "))

# total_percentage = 0

# for i in range(1, n + 1):
#     print(f"\nStudent {i}")

#     total = 0
#     for j in range(1, 6):
#         marks = int(input(f"Enter marks of Subject {j}: "))
#         total += marks

#     percentage = (total / 500) * 100
#     print(f"Percentage = {percentage:.2f}%")

#     total_percentage += percentage

# average = total_percentage / n
# print(f"\nAverage Percentage = {average:.2f}%")

 
