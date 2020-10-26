a, b, c, d = map(int, input().split())


def selection():
    # if not b <= c:  # or
    if not b > c:
        return False
    if not d > a:
        return False
    if not c + d > a + b:
        return False
    if not c > 0:
        return False
    if not d > 0:
        return False
    if a % 2 != 0:
        return False
    return True


if selection():
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
