import datetime
import portion as P

start_date = datetime.datetime(2023, 1, 1, 10, 0, 0)
end_date = datetime.datetime(2023, 1, 5, 10, 0, 0)
main_interval = P.closed(start_date, end_date)

night_interval_start = datetime.time(0, 0, 0)
night_interval_end = datetime.time(6, 0, 0)

night_intervals_list = []
current_date = start_date.date() + datetime.timedelta(days=1) 

while current_date <= end_date.date():
    interval_start = datetime.datetime.combine(current_date, night_interval_start)
    interval_end = datetime.datetime.combine(current_date, night_interval_end)
    current_night_interval = P.closed(interval_start, interval_end)
    night_intervals_list.append(current_night_interval)
    current_date += datetime.timedelta(days=1)

for interval in night_intervals_list:
    main_interval -= interval
total_hours = datetime.timedelta(seconds=0)

for interval in main_interval:
    total_hours += interval.upper - interval.lower

total_hours = total_hours.total_seconds() / 3600
print(f"Total hours: {total_hours} hours")
