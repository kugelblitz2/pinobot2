import time

# Replace 'None' with your bot's token
token = None

# Configurations
times_active = [[9,5]]
user_github = 'MrPicklePinosaur'
user_discord_id = '485120501807579144'

# Predicate
def should_activate(message):
    try:
        if not user_github in message.embeds[0].author.name: return False
        time.tzset()
        if (time.localtime()[6] == 6 or time.localtime()[6] == 5):
            return False
        for i in times_active:
            if (time.localtime()[3] >= i[0] and time.localtime()[3] < i[1]):
                return True
        
        return False
    except:
        return False

# Bot Trigger Action
async def trigger_action(message):
    await message.channel.send('<@' + user_discord_id + '>! Stop committing during work!')