import os
from discord.ext import commands

client = commands.Bot(command_prefix="//")
TOKEN = os.getenv("TOKEN")

print(TOKEN)

@client.event
async def on_ready():
	print(f"Logged on as {client.user}")

client.run(TOKEN)