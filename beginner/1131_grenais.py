def play_again():
    print("Novo grenal (1-sim 2-nao)")
    play = int(input())
    if play == 1:
        return True
    else:
        return False


result = []

while True:
    inter_goals, gremio_goals = map(int, input().split())

    if inter_goals == gremio_goals:
        result.append('tied')
    elif inter_goals > gremio_goals:
        result.append('inter')
    else:
        result.append('gremio')

    if play_again():
        continue

    games = len(result)
    inter_wins = result.count('inter')
    gremio_wins = result.count('gremio')
    tieds = result.count('tied')
    winner = 'Inter' if inter_wins > gremio_wins else 'Gremio'

    print("""{} grenais
Inter:{}
Gremio:{}
Empates:{}
{} venceu mais""".format(games, inter_wins, gremio_wins, tieds, winner))
    break
