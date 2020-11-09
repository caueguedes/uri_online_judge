iterations = int(input())


while iterations > 0:
    iterations -= 1

    city_a, city_b, rate_a, rate_b = input().split()
    city_a, city_b = int(city_a), int(city_b)

    rate_a = float(rate_a)/100
    rate_b = float(rate_b)/100

    times = 0
    while city_a <= city_b:
        times += 1
        city_a += city_a * rate_a//1
        city_b += city_b * rate_b//1

    if times > 100:
        print("Mais de 1 seculo.")
    else:
        print("{} anos.".format(times))
