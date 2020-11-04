start_day = int(input().split()[-1])
start_hour, start_min, start_second = map(int, input().split(" : "))

end_day = int(input().split()[-1])
end_hour, end_min, end_second = map(int, input().split(" : "))


seconds_started = start_second + start_min * 60 + start_hour * 3600 + start_day * 3600 * 24
seconds_ended = end_second + end_min * 60 + end_hour * 3600 + end_day * 3600 * 24
difference = seconds_ended - seconds_started

days = difference // (3600 * 24)
hours = difference % (3600 * 24) // 3600
minutes = difference % (3600 * 24) % 3600 // 60
seconds = difference % (3600 * 24) % 3600 % 60

print(f"""{days} dia(s)
{hours} hora(s)
{minutes} minuto(s)
{seconds} segundo(s)""")

# OR
import datetime
date_started = datetime.date(day=start_day, hours=start_hour, minutes=start_min, seconds=start_second)
date_ended = datetime.date(day=end_day, hours=end_hour, minutes=end_min, seconds=end_second)

difference = date_ended - date_started
formatted_string = """%d dia(s)
%H hora(s)
%M minuto(s)
%S segundo(s)"""
print(difference.strftime(formatted_string))
