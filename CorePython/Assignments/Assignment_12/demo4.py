#4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged

def exchangeCharacter(s):
    if len(s) <= 1:
        return s

    new_string = s[-1] + s[1:-1] + s[0]
    return new_string


s = "python"

result = exchangeCharacter(s)

print(result)
