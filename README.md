# pinobot2
A bot to remind Daniel to be more productive with his time

## How To Use
Configure `settings.py`, cd into the directory and run

    pip3 install -r requirements

to install dependencies. Then,

    python3 bot.py

to start pinobot.

## Running as a service
Change the path in `pinobot.service` to the location of your `bot.py` file

    sudo pip3 install -r requirements
    sudo cp ./pinobot2.service /etc/systemd/system
    sudo systemctl daemon-reload
    sudo systemctl enable pinobot2
    sudo systemctl start pinobot2


**Compatibility Notice: Runs on all real (UNIX) operating systems. May or may not work on Windows**
