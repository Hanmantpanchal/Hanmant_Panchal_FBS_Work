#11. WAP to check if a given number is Armstrong number or not. For
#each task create separate functions

def count(num):
    temp=num
    count=0
    while(temp>0):
        temp=temp//10
        count+=1
    return count

def armstrong(num):
    power = count(num)
    temp=num
    
    total = 0
    while(temp>0):
        digit=temp%10
        total +=digit**power
        temp=temp//10
    return total == num
x = int(input("Enter a number : "))
if(armstrong(x)):
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

    