cases = int(input())

for case in range(cases):
    current = 0
    n, m = map(int, input().split())
    soldiers = list(range(n))

    def next_soldier(current_soldier):
        pass


    for time in (range(n - 1)):
        print(f"current:{current}, index:{soldiers.index(current)} value:{soldiers[soldiers.index(current)]} list:{soldiers}")
        killed_soldier = soldiers[soldiers.index(current) + 1]
        soldiers.remove(killed_soldier)
        print(f"killed: {killed_soldier}, list:{soldiers}")
        current = soldiers[soldiers.index(current) + m]
