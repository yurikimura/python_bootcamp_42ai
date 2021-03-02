import datetime
t = (3, 30, 2019, 9, 25)

year = t[2]
month = t[3]
day = t[4]
hour = t[0]
minute = t[1]

date = datetime.datetime(year, month, day, hour, minute)
date_str = date.strftime("%m/%d/%Y %H:%M")

print(date_str)
