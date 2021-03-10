from datetime import datetime
now = datetime.now()
today = datetime.today()

print(today)
print(today.year)
print(today.month)

print(now.hour)

print(datetime.strftime(today,'%d/%m/%y'))
print(today.strftime('%d/%m/%y'))


