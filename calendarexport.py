from datetime import datetime, timedelta
from icalendar import Calendar, Event

# Set initial dates for November and December 2024
november_start = datetime(2024, 11, 1)
december_start = datetime(2024, 12, 1)

# Schedule with times for each week in November and December
schedule_november = [
    [("Monday", 10), ("Wednesday", 14), ("Thursday", 16), ("Saturday", 11)],
    [("Tuesday", 9), ("Thursday", 15), ("Friday", 17), ("Sunday", 14)],
    [("Monday", 8), ("Tuesday", 12), ("Thursday", 18), ("Friday", 9)],
    [("Wednesday", 11), ("Thursday", 13), ("Friday", 10), ("Saturday", 15), ("Sunday", 16)]
]

schedule_december = [
    [("Monday", 9), ("Wednesday", 10), ("Friday", 16), ("Saturday", 17)],
    [("Tuesday", 11), ("Thursday", 13), ("Friday", 15), ("Sunday", 9)],
    [("Monday", 14), ("Wednesday", 8), ("Thursday", 16), ("Saturday", 10), ("Sunday", 13)],
    [("Tuesday", 12), ("Wednesday", 9), ("Friday", 11), ("Saturday", 14)]
]

# Helper function to find the correct date and time based on weekday name
def find_datetime_by_weekday(start_date, weekday_name, week_offset, hour):
    weekday_map = {
        "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
        "Friday": 4, "Saturday": 5, "Sunday": 6
    }
    day_offset = (weekday_map[weekday_name] - start_date.weekday() + 7) % 7
    target_date = start_date + timedelta(days=day_offset, weeks=week_offset)
    target_datetime = target_date.replace(hour=hour, minute=0)
    return target_datetime

# Initialize calendar
cal = Calendar()

# Add events for November and December
for week_index, weekly_schedule in enumerate(schedule_november):
    for day_name, hour in weekly_schedule:
        event_start = find_datetime_by_weekday(november_start, day_name, week_index, hour)
        event = Event()
        event.add('summary', 'Data Analytics Company Work Session')
        event.add('dtstart', event_start)
        event.add('dtend', event_start + timedelta(hours=1))
        cal.add_component(event)

for week_index, weekly_schedule in enumerate(schedule_december):
    for day_name, hour in weekly_schedule:
        event_start = find_datetime_by_weekday(december_start, day_name, week_index, hour)
        event = Event()
        event.add('summary', 'Data Analytics Company Work Session')
        event.add('dtstart', event_start)
        event.add('dtend', event_start + timedelta(hours=1))
        cal.add_component(event)

# Save the calendar to a file
file_path = 'data_analytics_work_sessions.ics'
with open(file_path, 'wb') as f:
    f.write(cal.to_ical())

print(f"Calendar file created at {file_path}")
