# User enter current time in hours
current_time = int(input("Enter current time (millitary time): "))

# User number of hours before alarm sounds off
hours_to_wait = int(input("Enter the number of hours for alarm: "))

# Calculate before alarm sounds
alarm_time = (current_time + hours_to_wait)

# Print the result
print("The alarm will ring at {alarm_time}:00 (24-hour clock).")