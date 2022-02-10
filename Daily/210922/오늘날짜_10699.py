import datetime

today = datetime.date.today()
dif = datetime.timedelta(hours=9)
today = today+dif
print(f'{today.year}-{today.month:02}-{today.day:02}')