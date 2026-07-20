#12 . Write a program to create three lists of numbers, their squares and cubes

def list_of_squares_and_cubes(list1):
    squares =[]
    cubes = []
    for i in list1:

        cubes.append(i**3)
        squares.append(i**2)
    return squares,cubes

list1 = [1,2,3,4,5,6,7,8,9,10]

print(list_of_squares_and_cubes(list1))
