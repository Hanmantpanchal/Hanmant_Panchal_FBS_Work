#remove duplicates from a list 
def remove_duplicates(lst):
    result = []

    for i in lst:
        if i not in result:
            result.append(i)

    return result

lst = [1,2,3,4,5,1,2,3,4,5]
print(remove_duplicates(lst))
