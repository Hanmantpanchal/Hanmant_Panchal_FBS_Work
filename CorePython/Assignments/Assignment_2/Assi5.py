#calculate  selling  price  of book based  on  cost price and discount 

cp = int(input("Enter the cost price of book: "))

discount = int(input("Enter the discount on book: "))

#perform oprations 


sp = cp*(1-discount/100)

#Dsiplay the  selling  price  of  book

print(f'The selling price of book is {sp}')