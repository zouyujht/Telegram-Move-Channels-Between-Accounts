from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import asyncio
import os
from urllib.parse import urlparse

async def import_channels(api_id, api_hash, phone, import_file):
    proxy = None
    http_proxy = os.environ.get('HTTP_PROXY')
    if http_proxy:
        parsed = urlparse(http_proxy)
        proxy_type = parsed.scheme
        if proxy_type.startswith('http'):
            proxy_type = 'http'
        proxy = (proxy_type, parsed.hostname, parsed.port)

    async with TelegramClient('anon', api_id, api_hash, proxy=proxy) as client:
        # Ensure you're authorised
        await client.start(phone)

        # Read the channels and groups from the file with utf-8 encoding
        with open(import_file, 'r', encoding='utf-8') as f:
            channels = f.readlines()

        for channel in channels:
            channel = channel.strip()  # Remove any extra whitespace or newline characters
            try:
                await client(JoinChannelRequest(channel=channel))
                print(f"Successfully joined {channel}")
            except Exception as e:
                print(f"Could not join {channel}: {e}")

if __name__ == '__main__':
    api_id = input('YOUR_API_ID: ')  # Get user input for API ID
    api_hash = input('YOUR_API_HASH: ')  # Get user input for API hash
    phone = input('YOUR_PHONE_NUMBER: ')  # Get user input for phone number
    import_file = 'channels.txt'  # Input file

    asyncio.run(import_channels(api_id, api_hash, phone, import_file))
