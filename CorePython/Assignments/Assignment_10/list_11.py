#11. Write a program to print all numbers which are divisible by m and n in the list.

def divisible_by_m_n(list1, m, n):
    for i in list1:
        if i % m == 0 and i % n == 0:
            print(i)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = 2
n = 3
divisible_by_m_n(list1, m, n)