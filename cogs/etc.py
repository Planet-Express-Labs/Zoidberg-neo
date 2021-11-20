# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.
import disnake
from disnake.ext import commands
import art


class Etc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="big-text", brief="Makes the text a big boy!.")
    async def cmd_big_text(self, inter, text: str = commands.Param(),
                           font: str = commands.Param(desc='Python Art text2art supported fonts.', default='ascii')):
        """
        big boy textifer
        :Context inter:
        :string text:
        """
        try:
            await inter.response.send_message(f"```{art.text2art(text, font=font)}```")
        except art.artError:
            await inter.response.send_message(f":exclamation: Something went wrong! Are you sure {font} exists within text2art?")


def setup(bot):
    bot.add_cog(Etc(bot))
