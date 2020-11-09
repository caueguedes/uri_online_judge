while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break

    if m > n :
        m, n = n, m

    values = [value for value in range(m, n+1)]
    print(*values, end=' ')
    print(f"Sum={sum(values)}")


