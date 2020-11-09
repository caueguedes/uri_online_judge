while True:
    coordinate_x, coordinate_y = map(int, input().split())

    if coordinate_x == 0 or coordinate_y == 0:
        break

    if coordinate_x > 0:
        if coordinate_y > 0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if coordinate_y > 0:
            print('segundo')
        else:
            print('terceiro')
