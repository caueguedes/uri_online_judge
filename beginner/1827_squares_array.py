while True:
    try:
        size = int(input())
    except EOFError:
        break
    else:
        fours_space = 1 if size % 2 else 2

        values_array = [[0]*size for _ in range(size)]
        fours_range = range(limit_four, size - limit_four)

        for line in range(size):
            for column in range(size):
                if column + line + 1 == size:
                    values_array[line][column] = 3
                elif line == column:
                    values_array[line][column] = 2
                if line in ones_range and column in ones_range:
                    values_array[line][column] = 1
                if line in fours_range and column in fours_range:
                    values_array[line][column] = 4
        for line in values_array:
            print(*line, sep="")
