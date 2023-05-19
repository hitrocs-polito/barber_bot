from datetime import datetime, time, timedelta
from pytz import timezone

# Set the time zone
from handlers.users.google_api import service

tz = timezone('Asia/Tashkent')

# Set the date
date = datetime.today() + timedelta(days=1)

# Set the start and end of the day
start_of_day = datetime.combine(date, time.min).astimezone(tz)
end_of_day = datetime.combine(date, time.max).astimezone(tz)
print(start_of_day)
print(end_of_day)

# Format the start and end of the day as RFC3339 timestamps
start_of_day_str = start_of_day.isoformat()
end_of_day_str = end_of_day.isoformat()

events_result = service.events().list(calendarId='primary',
                                      timeMin=start_of_day_str,
                                      timeMax=end_of_day_str,
                                      singleEvents=True,
                                      orderBy='startTime'
                                      ).execute()
events = events_result.get('items', [])

for event in events:
    event_title = event['description']
    start_time_str = event['start'].get('dateTime', event['start'].get('date'))
    start_time = datetime.fromisoformat(start_time_str).astimezone(tz)
    end_time_str = event['end'].get('dateTime', event['end'].get('date'))
    end_time = datetime.fromisoformat(end_time_str).astimezone(tz)

    print(f'{event_title}: {start_time} - {end_time}')



