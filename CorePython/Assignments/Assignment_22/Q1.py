# 1. Create a class Emp (eid,ename,basic)
# 2. WAP a menu driven program to perform following operations using
# files :
# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records


import pickle


class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print("ID     :", self.eid)
        print("Name   :", self.ename)
        print("Basic  :", self.basic)


FILE_NAME = "employee.dat"


# 1. Add Record
def add_record():
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    emp = Emp(eid, ename, basic)

    try:
        f = open(FILE_NAME, "rb")
        employees = pickle.load(f)
        f.close()
    except:
        employees = []

    # Check duplicate ID
    for e in employees:
        if e.eid == eid:
            print("Employee ID already exists!")
            return

    employees.append(emp)

    f = open(FILE_NAME, "wb")
    pickle.dump(employees, f)
    f.close()

    print("Record added successfully.")


# 2. Search Record
def search_record():
    eid = int(input("Enter Employee ID to search: "))

    try:
        f = open(FILE_NAME, "rb")
        employees = pickle.load(f)
        f.close()
    except:
        print("No records found.")
        return

    for e in employees:
        if e.eid == eid:
            print("\nRecord Found")
            e.display()
            return

    print("Employee not found.")


# 3. Delete Record
def delete_record():
    eid = int(input("Enter Employee ID to delete: "))

    try:
        f = open(FILE_NAME, "rb")
        employees = pickle.load(f)
        f.close()
    except:
        print("No records found.")
        return

    for e in employees:
        if e.eid == eid:
            employees.remove(e)

            f = open(FILE_NAME, "wb")
            pickle.dump(employees, f)
            f.close()

            print("Record deleted successfully.")
            return

    print("Employee not found.")


# 4. Edit Record
def edit_record():
    eid = int(input("Enter Employee ID to edit: "))

    try:
        f = open(FILE_NAME, "rb")
        employees = pickle.load(f)
        f.close()
    except:
        print("No records found.")
        return

    for e in employees:
        if e.eid == eid:

            print("\nCurrent Record:")
            e.display()

            e.ename = input("Enter New Name: ")
            e.basic = float(input("Enter New Basic Salary: "))

            f = open(FILE_NAME, "wb")
            pickle.dump(employees, f)
            f.close()

            print("Record updated successfully.")
            return

    print("Employee not found.")


# 5. Display All Records
def display_all():
    try:
        f = open(FILE_NAME, "rb")
        employees = pickle.load(f)
        f.close()
    except:
        print("No records found.")
        return
    print()

    for e in employees:
        e.display()


# Menu Driven Program
while True:

    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    print()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_record()

    elif choice == 2:
        search_record()

    elif choice == 3:
        delete_record()

    elif choice == 4:
        edit_record()

    elif choice == 5:
        display_all()

    elif choice == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid choice!")