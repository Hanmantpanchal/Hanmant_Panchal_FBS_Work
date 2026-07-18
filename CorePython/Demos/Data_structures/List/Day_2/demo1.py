#count even and odd numbers 

def evenOdd(li):
    Even = 0
    Odd = 0
    for i in li:
        if i % 2 == 0:
            Even = Even + 1
        else:
            Odd = Odd + 1
    print("Even number in the list",Even)
    print("Odd numbers in the list " , Odd)


    
li = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ,10]

evenOdd(li)


