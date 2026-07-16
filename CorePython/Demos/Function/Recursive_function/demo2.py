#WAP to saprate the digit and print it 
def print_digit(n):
    if n>0:
        print_digit(n//10)
        print(n%10)
             
n=int(input("Enter a number: "))
print_digit(n)