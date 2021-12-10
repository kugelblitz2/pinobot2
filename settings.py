import time
from typing import final

# Replace 'None' with your bot's token
token = 'OTE4NzMwNjUxNTU2MDE2MTU4.YbLgmA.tCv7hfvU7g9XldpKLL5bxwyV_VE'

# Configurations
times_active = [[0,24]]
user_github = 'kugelblitz2'
user_discord_tag = 'tokyoneko#1777'

# Predicate
def should_activate(message):
    try:
        if not user_github in message.embeds[0].author.name: return False
        time.tzset()
        for i in times_active:
            if (time.localtime()[3] >= i[0] and time.localtime()[3] < i[1]):
                return True
        
        return False
    except:
        return False