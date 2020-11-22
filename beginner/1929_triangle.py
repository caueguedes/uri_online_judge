a, b, c, d = map(int, input().split())


def make_triangle(side1, side2, side3):
    if side1 + side2 < side3:
        return False
    if side1 + side3 < side2:
        return False
    if side2 + side3 < side1:
        return False
    return True


if make_triangle(a, b, c) or make_triangle(a, c, d) or \
        make_triangle(b, c, d) or make_triangle(a, b, d):
    print("S")
else:
    print("N")

