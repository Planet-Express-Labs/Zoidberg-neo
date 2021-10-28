# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.
import disnake
from disnake.ext import commands
from zoidberg.config import *
import motor.motor_asyncio

__version__ = "3.0 PRE"

# define activity, playing status
activity = disnake.Activity(name='> planetexpresslabs.io', type=disnake.ActivityType.playing)
# define gateway intents
intents = disnake.Intents.default()
intents.members = True
print(TEST_GUILDS)
bot = commands.Bot(command_prefix='-=',
                   activity=activity,
                   intents=intents,
                   test_guilds=[842987183588507670])

disabled_cogs = DISABLED_COGS
logging.basicConfig(level=logging.INFO)
for filename in os.listdir("cogs"):
    if filename.endswith(".py") and filename not in disabled_cogs:
        bot.load_extension(f"cogs.{filename[:-3]}")
if DB_LOCALHOST:
    mongo_client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
else:
    mongo_client = motor.motor_asyncio.AsyncIOMotorClient(CONNURL)


@bot.event
async def on_ready():
    print(f"Bot is ready: logged in as {bot.user.name} ({bot.user.id})")
    await bot.wait_until_ready()


@bot.slash_command(name='foo', brief='Tests if the bot is dead or not')
async def cmd_foo(ctx):
    await ctx.response.send_message(f"Bar!\nLatency: {bot.latency} ms")


bot.run(BOT_TOKEN)
