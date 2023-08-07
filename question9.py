from datetime import datetime, timedelta
start_time_str = input("Enter the start time (YYYY-MM-DD HH:mm): ")
end_time_str = input("Enter the end time (YYYY-MM-DD HH:mm): ")
# according to the requirement there was a interval that should not be added 
# input form the user to not include the specific timing
start_str_time = input("Enter the start time (HH:MM): ")
end_str_time = input("Enter the end time (HH:MM): ")
# string time to match the date and time format
start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
# string time to match the date and time format
start_time_obj = datetime.strptime(start_str_time, "%H:%M")
end_time_obj = datetime.strptime(end_str_time, "%H:%M")
# first finding the diff and then substracting the diff of the intervals which are not gonna be added
c = (end_time - start_time) - (end_time_obj - start_time_obj)
print('Difference: ', c)