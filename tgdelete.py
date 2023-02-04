import logging
from telethon import TelegramClient, events

API_ID = 23760181  # your API ID here
API_HASH = "cd952e08ae2b4552fe0dfce5d778afe8"  # your API hash here
# BOT_TOKEN = "6058614028:AAEQdS2ApdKSpxx3wVhhM8yc5EcojBaydPU"

blacklist = ["@Thesqd", "@thesqd"]

client = TelegramClient('theDeleter', API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True))
async def delete_message(event):
    for word in blacklist:
        if word in event.message.message.lower():
            await event.message.delete()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    client.start()
    client.run_until_disconnected()
