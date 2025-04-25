import asyncio
from mbot import Mbot
from os import path, mkdir

if __name__ == "__main__":
    if not path.exists("cache"):
        mkdir("cache")

    bot = Mbot()

    loop = asyncio.get_event_loop()

    # Create task to start the bot
    loop.create_task(bot.start())

    # Keep the loop running forever
    try:
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        loop.run_until_complete(bot.stop())

## from os import sys,mkdir,path
