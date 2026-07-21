#8. Print 1 to 100 in snakes and ladder pattern.

def snakesLadder():

    start = 1
    end = 10

    for i in range(1, 11):

        if i % 2 != 0:
            for j in range(start, end + 1):
                print(j, end=" ")
        else:
            for j in range(end, start - 1, -1):
                print(j, end=" ")

        print()

        start = start + 10
        end = end + 10

snakesLadder()

