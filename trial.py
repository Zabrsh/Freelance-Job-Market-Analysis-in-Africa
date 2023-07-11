from telethon import TelegramClient, sync
from datetime import datetime
import pytz 
from datetime import datetime
api_id = ""
api_hash = ""
phone_number = ''

client = TelegramClient('session_name', api_id, api_hash)
client.start()

channel_username = 'https://t.me/freelance_ethio'
channel_entity = client.get_entity(channel_username)

# Create a timezone object
tz = pytz.timezone('Africa/Nairobi')

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 6, 29)

# Convert start_date and end_date to timezone-aware datetime objects
start_date_aware = tz.localize(start_date)
end_date_aware = tz.localize(end_date)

messages = client.get_messages(channel_entity, limit=None)

# with open('messages.txt', 'a', encoding='utf-8') as file:
#     for message in messages:
#         if start_date <= message.date <= end_date:
#             file.write(message.text + '\n')

# Loop through messages and write to file
with open('messages.txt', 'a', encoding='utf-8') as file:
    for message in messages:
        # Convert message date to timezone-aware datetime object
        message_date_naive = message.date.replace(tzinfo=None)
        message_date_aware = tz.localize(message_date_naive)

        # Check if message date is between start_date and end_date
        # if start_date_aware <= message_date_aware <= end_date_aware:
        #     file.write(message.text + '\n')
        if start_date_aware <= message_date_aware <= end_date_aware:
             if type(message.text) == str:
                 file.write(message.text + '\n')
        