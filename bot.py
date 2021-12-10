import discord
from settings import token, work_start, work_end

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(message.embeds)

client.run(token)