import time

current_time = time.localtime()
print(current_time)
print("current_time", time.asctime(current_time))

get_me_time = time.asctime((2026, 2, 2, 18, 22, 22, 6, 32, 0))
print("some date:", get_me_time)


unix_time = time.time()
print(unix_time)

timestamp = 1777777777
unix_a_time = time.ctime(timestamp)
print("unix_a_time", unix_a_time)

unix_time_zero = 0
unix_z_time = time.ctime(unix_time_zero)
print("unix zero", unix_z_time)

timestamp = 17222707821 #2515
unix_timestamp = time.ctime(timestamp)
print("ex1",unix_timestamp)
#timestamp = 19999999999 #2603
timestamp = 20000000000
unix_timestamp = time.ctime(timestamp)
print("ex2", unix_timestamp)

print(time.time())
time.sleep(1)
print(time.time())

some_day_1 = "Sep 20, 2022"
some_day_1_1 = "Dec 21, 2022"
some_day_2 = "Dec 21 2022"

pattern = "%b %d, %Y"
my_datetime = time.strptime(some_day_1, pattern)
print(my_datetime)
# Рядок з часом
time_string = '2023/12/31 23:59:59'
# Формат рядка
format_string = '%Y/%m/%d %H:%M:%S'
# Перетворення рядка у структуру часу
time_obj = time.strptime(time_string, format_string)
print(time_obj)
try:
    time_obj_1 = time.strptime(time_string, pattern)
    print(time_obj_1)
except ValueError:
    print(f"wrong time format: {time_string}, expect {pattern}")

good_time_output = time.strftime("Now year %Y %m month and day is %d time is: %H:%M",
                     time.localtime())
print(good_time_output)
