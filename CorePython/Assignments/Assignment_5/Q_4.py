# 4. WAP to print Armstrong number within a given range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):

    # Count digits
    count = 0
    temp = n

    while temp > 0:
        count += 1
        temp = temp // 10

    # Calculate Armstrong sum
    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp = temp // 10

    if total == n:
        print(n)
