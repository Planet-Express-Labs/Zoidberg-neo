# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.

from disnake.ext import commands
from frontman.config import *

bot = commands.Bot(command_prefix='-=')

disabled_cogs = []
logging.basicConfig(level=logging.INFO)

for filename in os.listdir("cogs"):
    if filename.endswith(".py") and filename not in disabled_cogs:
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    print(f"Bot is ready: logged in as {bot.user.name} ({bot.user.id})")
    await bot.wait_until_ready()


@bot.slash_command(name='foo', brief='Tests if the bot is dead or not')
async def cmd_foo(ctx):
    await ctx.response.send_message(f"Bar!\nLatency: {bot.latency} ms")

bot.run(BOT_TOKEN)
