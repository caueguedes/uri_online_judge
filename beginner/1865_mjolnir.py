iterations = int(input())

for _ in range(iterations):
    name, force = input().split()

    if name == "Thor":
        print("Y")
    else:
        print("N")
