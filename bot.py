import discord
from discord.ext import tasks
import time

import functions

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    try:
        if not 'github' in message.embeds[0].author.url: return
        functions.should_update(message)
        time.tzset()
        print(time.strftime('%b %d %Y at %I:%M %p: Bot triggered by ', time.localtime()) + functions.user_github)
    except:
        pass

@tasks.loop(minutes=1)
async def check_time():
    if functions.should_trigger():
        functions.last_commit = int(time.time())
        await functions.trigger_action()
        print(time.strftime('%b %d %Y at %I:%M %p: ', time.localtime()) + functions.user_github + " was pinged!")

check_time.start()
client.run(functions.token)
