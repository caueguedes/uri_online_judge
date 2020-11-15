while True:
    try:
        complains = int(input())
    except EOFError:
        break
    else:
        if complains > 0:
            print("vai ter duas!")
        else:
            print("vai ter copa!")
