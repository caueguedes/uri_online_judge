while True:
    try:
        size = int(input())
    except EOFError:
        break
    else:
        values_array = [[0]*size for _ in range(size)]

        for line in range(size):
            for column in range(size):
                if column + line + 1 == size:
                    values_array[line][column] = 2
                elif line == column:
                    values_array[line][column] = 1
                else:
                    values_array[line][column] = 3

        for line in values_array:
            print(*line, sep="")
