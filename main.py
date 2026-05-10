import discord
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
LINK_TO_SEND = "https://cloud.timeedit.net/eeg/web/public1/ri1f7X7Q97ZZ3YQf5Q0443Y8yQY.html"
TRIGGER_WORDS = ["schema", "schemat", "har vi skola", "på plats", "lektion imorgon"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(word in message.content.lower() for word in TRIGGER_WORDS):
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
            await webhook.send(
                content = f"Någon sa det magiska ordet, här är länken: {LINK_TO_SEND}",
                username = "Helder"
            )


client.run(DISCORD_TOKEN)