while True:
    try:
        size = int(input())
    except EOFError:
        break
    else:
        values_array = [[0]*size for _ in range(size)]

        ceil = size // 3
        ones_range = range(ceil, size - ceil)

        for line in range(size):
            for column in range(size):
                if column + line + 1 == size:
                    values_array[line][column] = 3
                elif line == column:
                    values_array[line][column] = 2
                if line in ones_range and column in ones_range:
                    values_array[line][column] = 1
                if size % 2:
                    index = size // 2
                    values_array[index][index] = 4
        for line in values_array:
            print(*line, sep="")
        print("")
