# 2. Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero

class Television:

    def __init__(self):
        self.modelNo = 0
        self.screenSize = 0
        self.price = 0

    def accept(self):

        try:
            # Take input
            self.modelNo = int(input("Enter Model Number: "))
            self.screenSize = float(input("Enter Screen Size: "))
            self.price = float(input("Enter Price: "))

            # Validate Model Number
            if self.modelNo < 0 or len(str(self.modelNo)) > 4:
                raise Exception("Model number should not contain more than 4 digits.")

            # Validate Screen Size
            if self.screenSize < 12 or self.screenSize > 70:
                raise Exception("Screen size must be between 12 and 70 inches.")

            # Validate Price
            if self.price < 0 or self.price > 5000:
                raise Exception("Price must be between Rs. 0 and Rs. 5000.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

            # Replace all values with zero
            self.modelNo = 0
            self.screenSize = 0
            self.price = 0

        except Exception as e:
            print("Error:", e)

            # Replace all values with zero
            self.modelNo = 0
            self.screenSize = 0
            self.price = 0

    def display(self):

        print("\n--------- Television Details ---------")
        print("Model Number :", self.modelNo)
        print("Screen Size  :", self.screenSize, "inches")
        print("Price        : Rs.", self.price)
        print("--------------------------------------")


# main()

tv = Television()

tv.accept()

tv.display()