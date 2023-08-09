from datetime import datetime, timedelta
import portion as P
start_time_str = input("Enter the start time (YYYY-MM-DD HH:mm:ss): ")
end_time_str = input("Enter the end time (YYYY-MM-DD HH:mm:ss): ")
start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
interval = P.closed(start_time,end_time)
night_interval = P.closed(datetime(2023, 1, 2, 0,00,1),datetime(2023, 1, 2,6,00,00))
time_diff = datetime(2023, 1, 2,10,00,00)-datetime(2023, 1, 1, 10,00,00)
date_list = [interval.lower]  # Start with the lower bound
current_date = interval.lower 
# to track the hours
count = 0
for i in range(int(time_diff.total_seconds()/3600)): # divided by 3600 to convert minutes to hours
    current_date += timedelta(hours=1)
    if current_date not in night_interval:
        count += 1
        date_list.append(current_date)
print(f"The difference between the start time - {start_time} and end time - {end_time} is {count} Hours")