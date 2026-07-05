from telethon.sync import TelegramClient
import asyncio
import os
from urllib.parse import urlparse

async def export_channels(api_id, api_hash, phone, export_file):
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
        print('Process Started.')

        # Fetch all the channels and groups
        async for dialog in client.iter_dialogs():
            if dialog.is_channel or dialog.is_group:
                with open(export_file, 'a', encoding='utf-8') as f:
                    f.write(f"{dialog.name}\n")


if __name__ == '__main__':
    api_id = input('YOUR_API_ID: ')
    api_hash = input('YOUR_API_HASH: ')
    phone = input('YOUR_PHONE_NUMBER: ')  # Replace with your phone number
    export_file = 'channels.txt'  # Output file

    asyncio.run(export_channels(api_id, api_hash, phone, export_file))
    print('Process Complete.')
