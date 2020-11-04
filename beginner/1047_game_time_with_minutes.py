hour_start, min_start, hour_end, min_end = map(int, input().split())

if hour_start > hour_end:
    hour_end += 24
elif hour_start == hour_end and min_start >= min_end:
    hour_end += 24

total_start = hour_start * 60 + min_start
total_end = hour_end * 60 + min_end

total = total_end - total_start
total_hour = total // 60
total_min = total % 60
print(f"O JOGO DUROU {total_hour} HORA(S) E {total_min} MINUTO(S)")
