
from datetime import datetime, time, timedelta, date


now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
print(f'{month}/{day}/{year} {hour}:{minute}:{second}')

print(now.strftime("%m/%d/%Y %H:%M:%S"))

today_date = "22 April 2023"
new_date = datetime.strptime(today_date, "%d %B %Y")
print(new_date)

next_new_year = date(now.year+1, month=1, day=1)
now = date.today()
diff = next_new_year - now
print("Time to the next new year: ", diff)

an_old_date = date(year=1903, day=17, month=12)
diff = now-an_old_date
print("Time since an old date: ", diff)


