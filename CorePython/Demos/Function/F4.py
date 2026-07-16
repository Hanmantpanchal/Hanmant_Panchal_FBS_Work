#4.with passing parameter with returning value 

def addition(num1 , num2):
    #sum = num1 + num2
    #return sum

    return num1 + num2

x = int(input("enter the num1 :"))
y = int(input("enter the num2 :"))

res = addition(x , y)
print('addition ', res)