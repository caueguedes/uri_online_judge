while True:
    try:
        _ = int(input())
    except EOFError:
        break
    else:
        slugs_list = map(int, input().split())
        faster_slug = max(slugs_list)

        if faster_slug < 10:
            print(1)
        elif faster_slug < 20:
            print(2)
        else:
            print(3)