iterator = 0

while iterator <= 2:
    for j in range(3):
        if iterator % 1 == 0:
            print('I={0:.0f} J={1:.0f}'.format(iterator, j + 1 + iterator))
        else:
            print('I={0:.1f} J={1:.1f}'.format(iterator, j + 1 + iterator))
    iterator = round(iterator + 0.2, 1)
