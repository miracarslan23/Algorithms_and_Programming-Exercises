# Your Student ID:210543008
# Your Name and Surname:mustafa miraç arslan
from datetime import datetime
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")
current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date: {current_date}")
print(f"Current time: {current_time}")
print(f"Current date and time: {current_datetime}")

