from twilio.rest import Client
from datetime import datetime
import time

# Twilio credentials
acc_SID = "Your Twilio Account SID"
auth_token = "Your Twilio auth token"

client = Client(acc_SID, auth_token)


def send_message(recipient_num, message_body):
    try:
        message = client.messages.create(
            from_="whatsapp: Your Twilio Number",
            body=message_body,
            to=f"whatsapp:{recipient_num}",
        )
        print(f"Message Sent Successfully! Message SID: {message.sid}")
    except Exception as e:
        print("Error:", e)


# Get user input
name = input("Enter the recipient name: ")
recipient_num = input("Enter the recipient WhatsApp number with country code: ")
message_body = input(f"Enter the message that you want to send to {name}: ")

# Get scheduled date and time
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (in 24-hour format, HH:MM): ")

# Combine date and time
schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The time is in the past. Please enter a future time and date.")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}")
    time.sleep(delay_seconds)
    send_message(recipient_num, message_body)
