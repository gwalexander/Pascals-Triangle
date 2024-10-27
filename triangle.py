def generateTriangle():
    array = [[1]]
    for i in range(0, 100):
        add = []
        for j in range(0, len(array)+1):
            if (j-1) < 0:
                number = 1

            elif j > len(array[i])-1:
                number = 1

            else:
                number = array[i][j - 1] + array[i][j]
            add.append(number)

        array.append(add)
    return(array)

array = generateTriangle()

for i in range(0, len(array)-1):
    print(array[i])


# print(max(array[100))

