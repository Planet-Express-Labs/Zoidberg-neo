# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.
import disnake
from disnake.ext import commands
from utils.amputator_utils import check_if_amp
from modules.amputator.basic_funcs import get_reply


class Amputator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if check_if_amp(message.content):
            reply=get_reply(message.content)
            if reply:
                embed=disnake.Embed(color=1015649)
                embed.description = reply
                embed.set_footer(text="Zoidberg-Neo")
                embed.set_author(name="Amputator",
                                 icon_url="https://raw.githubusercontent.com/KilledMufasa/AmputatorBot/master/img"
                                          "/amputatorbot_logo.png",
                                 url="https://github.com/KilledMufasa/AmputatorBot/")
                await message.reply(embed=embed)


def setup(bot):
    bot.add_cog(Amputator(bot))
