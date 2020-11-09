scores = []
while True:
    grade = float(input())

    if 0 <= grade <= 10:
        scores.append(grade)
    else:
        print("nota invalida")

    if len(scores) == 2:
        average = sum(scores) / 2
        print("media = {:.2f}".format(average))
        break
