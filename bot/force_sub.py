from telethon import TelegramClient, events, functions, types
from config import API_HASH,YOUR_CHANNEL_USERNAME,API_ID
# Your bot credentials
API_ID = API_ID
API_HASH = 'API_HASH'
BOT_TOKEN = 'BOT_TOKEN'

# Your channel username
channel_username = 'YOUR_CHANNEL_USERNAME'

# Create a Telethon client
client = TelegramClient('my_bot', API_ID, API_HASH).start(BOT_TOKEN=BOT_TOKEN)

# Define a handler for incoming messages
@client.on(events.NewMessage(func=lambda event: not event.is_private))
async def my_handler(event):
    # Get the user ID
    user_id = event.message.from_id

    # Check if the user is already subscribed to the channel
    result = await client(functions.channels.GetFullChannelRequest(channel=channel_username))
    if user_id not in [user.user_id for user in result.full_chat.participants]:
        # Force the user to subscribe to the channel
        try:
            await client(functions.channels.JoinChannelRequest(channel=channel_username))
            await client.send_message(user_id, 'You have been subscribed to the channel.')
        except Exception as e:
            print(e)
            await client.send_message(user_id, 'An error occurred while subscribing to the channel.')

# Start the event loop
client.run_until_disconnected()
