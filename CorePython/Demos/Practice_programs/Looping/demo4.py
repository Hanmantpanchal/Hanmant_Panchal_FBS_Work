#check armstrong number 



# Check Armstrong Number

number = int(input("Enter the number: "))

# Step 1: Count the digits
temp = number
count = 0

while temp > 0:
    count = count + 1
    temp = temp // 10

# Step 2: Calculate the sum
temp = number
sum = 0

while temp > 0:
    d = temp % 10
    sum = sum + d ** count
    temp = temp // 10

# Step 3: Check
if sum == number:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

