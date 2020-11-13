while True:
    value = int(input())

    if value == 0:
        break

    values_array = [[0]*value for _ in range(value)]
    ceils = value//2 if value % 2 == 0 else value//2 + 1

    for ceil in range(ceils):
        negative_ceil = -(ceil + 1)
        for index_range in range(ceil, value - ceil):
            values_array[ceil][index_range] = ceil + 1
            values_array[index_range][ceil] = ceil + 1
            values_array[index_range][negative_ceil] = ceil + 1
            values_array[negative_ceil][index_range] = ceil + 1

    for line in values_array:
        for index, column in enumerate(line):
            if index:
                print(f"{column:>4d}", end='')
            else:
                print(f"{column:>3d}", end='')
        print("")
    print("")
