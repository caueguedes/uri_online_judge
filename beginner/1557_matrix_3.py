while True:
    size = int(input())

    if not size:
        break

    values_array = []

    for line in range(size):
        array = [2 ** (line + column) for column in range(size)]
        values_array.append(array)

    spaces = len(str(values_array[-1][-1]))
    for line in values_array:
        for index, column in enumerate(line):
            if index:
                print(f"{column:>{spaces+1}d}", end='')
            else:
                print(f"{column:>{spaces}d}", end='')
        print("")
    print("")