iterations = int(input())

for _ in range(iterations):
    radius_1, radius_2 = map(int, input().split())

    extern_radius = radius_1 + radius_2
    print(extern_radius)