while True:
    try:
        val1, val2 = map(int, input().split())
        operation_or = val1 ^ val2
        print(operation_or)
    except EOFError:
        break
