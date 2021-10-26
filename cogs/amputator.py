# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.
import disnake
from disnake.ext import commands
from disnake import Option, OptionType
from amputator.helpers.utils import check_if_amp
from amputator.basic_funcs import get_reply

class Amputator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if check_if_amp(message.content):
            reply=get_reply(message.content)
            if reply:
                await message.reply(reply)

def setup(bot):
    bot.add_cog(Amputator(bot))