li = [34,57,83,42,23,53,65]
max = li[0]

for i in range(1, len(li)):
    if max<li[i]:
        max=li[i]
print("maximum number is :",max)