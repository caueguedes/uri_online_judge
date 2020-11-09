scores = []


def play_again():
    print("novo calculo (1-sim 2-nao)")
    play = int(input())

    if play == 1:
        return True
    elif play == 2:
        return False
    else:
        return play_again()


while True:
    grade = float(input())

    if 0 <= grade <= 10:
        scores.append(grade)
    else:
        print("nota invalida")

    if len(scores) == 2:
        average = sum(scores) / 2
        print("media = {:.2f}".format(average))

        if not play_again():
            break
        else:
            scores = []
