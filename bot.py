import discord
import time

import settings

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    try:
        if not 'github' in message.embeds[0].author.url: return
        if not settings.should_activate(message): return
        time.tzset()
        print(time.strftime('%b %d %Y at %I:%M %p: Bot triggered by ', time.localtime()) + settings.user_github)
        await message.channel.send('@' + settings.user_discord_tag + '! Stop committing during work!')
    except:
        pass

client.run(settings.token)