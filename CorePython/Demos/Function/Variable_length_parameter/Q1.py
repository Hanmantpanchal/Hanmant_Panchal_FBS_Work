def add(*num):
    total = 0
    for val in num:
        total = total + val
    return total

res = add(10, 20, 30, 40, 50)
print("Addition is:", res)