number = int(input())

square_list = (f"{n}^2 = {n **2}" for n in range(1, number+1) if n % 2 == 0)

print(*square_list, sep="\n")

