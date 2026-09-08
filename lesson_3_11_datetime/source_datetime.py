from datetime import (
    datetime,
    timedelta,
    timezone
)

its_day = datetime.today()
print(its_day)


mydatetime = datetime.fromtimestamp(1706551390)
print(mydatetime, type(mydatetime))

ordinal_day = 365 # Порядковий номер дня
dt = datetime.fromordinal(ordinal_day)
print(dt)
day_number = datetime.today().toordinal()
print(f'Порядковий номер сьогоднішнього дня: {day_number}')

tz = timezone.utc
current_datetime = datetime.now(tz)
print("Поточна дата і час:", current_datetime)
# tz_kyiv = timedelta(hours=3)tz_kyiv
current_datetime = datetime.now()
print("Поточна дата і час:", current_datetime)
its_day = datetime.today()
print("today дата і час:", its_day)

incoming_date = "Aug 24, 1991"
dt_incoming_date = datetime.strptime(incoming_date, '%b %d, %Y')
print(dt_incoming_date)
dt_incoming_time_out = datetime.strftime(dt_incoming_date, "%H:%M:%S and %Y and month %m and day is %d")
print(dt_incoming_time_out)

dt_01 = "19:45:23"  # Germany
dt_02 = "20:00:22"
dt_03 = "20:00:27"
dt_04 = "20:45:23"  # Kyiv

def to_hour(time_in_hour:str):
    return datetime.strptime(time_in_hour, "%H:%M:%S")

new_dt = map(to_hour, [dt_01, dt_02, dt_03, dt_04])

dt_01_alex, dt_02_nata, dt_03_jena, dt_04_rost = new_dt
print(dt_01_alex, dt_02_nata, dt_03_jena)

diff_time = dt_02_nata - dt_01_alex
print("Diff", diff_time, type(diff_time))

if dt_02_nata - dt_01_alex >= timedelta(minutes=15):
    print("FAIL")
else:
    print("pass")

some_delta = timedelta(days=999999)
print(current_datetime + some_delta)

minus_td = dt_01_alex - dt_02_nata
print(minus_td, type(minus_td), timedelta(minutes=-15))

print("*"*88)
d = datetime.today()
print(d)
print(d.isocalendar())
print(d.isoformat())
print(d.isoweekday())
print(d.timetuple())
print(d.weekday())
dd = d.replace(year=2021, day=12)
print(dd)


td = timedelta(days=5, hours=3, minutes=30)
print(td)

total_seconds = td.total_seconds()
print(total_seconds)

big_td = timedelta(seconds=1_000_000)
print(big_td)
print(big_td.days/365)

big_td = timedelta(seconds=1_000_000_000)
print(big_td)
print(11574/365)
