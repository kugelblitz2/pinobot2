import time

# Replace 'None' with your bot's token
token = None

# Configurations
times_active = [[9,17]]
user_github = 'MrPicklePinosaur'
user_discord_id = '485120501807579144'

last_commit = 0
commit_interval = 7200
channel = None

# Predicate
def should_trigger():
    global last_commit
    try:
        now = int(time.time())
        if (time.localtime()[6] == 6 or time.localtime()[6] == 5):
            return
        for i in times_active:
            if (time.localtime()[3] >= i[0] and time.localtime()[3] < i[1]):
                if (now - last_commit > commit_interval) and (channel):
                    return True;
        return False
    except:
        return False

# Update last commit time
def should_update(message):
    global last_commit
    global channel
    try:
        if not user_github in message.embeds[0].author.name: return
        time.tzset()
        last_commit = int(time.time())
        channel = message.channel
        return
    except:
        return

# Bot Trigger Action
async def trigger_action():
    await channel.send('<@' + user_discord_id + '>, you\'re not being productive enough! Please commit more!')
