import asyncio
from mbot import Mbot
from os import path, mkdir

if __name__ == "__main__":
    if not path.exists("cache"):
        mkdir("cache")
    bot = Mbot()
    asyncio.run(bot.start())
