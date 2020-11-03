nota_1, nota_2, nota_3, nota_4 = map(float, input().split())

average = nota_1 * 2 + nota_2 * 3 + nota_3 * 4 + nota_4 * 1
average /= 10

print("Media: {:.1f}".format(average))

if average >= 7:
    print("Aluno aprovado.")
elif average < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    nota_exam = float(input())
    print("Nota do exame: {:.1f}".format(nota_exam))

    average += nota_exam
    average /= 2

    if average >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(average))
