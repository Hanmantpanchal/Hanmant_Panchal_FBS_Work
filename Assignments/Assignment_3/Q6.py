#6. Write a program to calculate profit or loss.

p=int(input("Enter the profit:"))
l=int(input("Enter the loss:"))

if(p>l):
    print("Profit")
elif(l>p):
    print("Loss")
else:
    print("Neither profit nor loss")