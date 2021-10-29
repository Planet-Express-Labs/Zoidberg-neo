import disnake
from disnake import *
from disnake.ext import commands
from utils.regex_patterns import find_url
import ffmpeg
import os


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="tenderize", brief="Makes the image very nice, saturated and tender.",
                            options=[
                                Option("url", "the image you want to tenderize", type=OptionType.string),
                                Option("saturation-amount", "how much to tenderize the image", type=OptionType.integer)
                            ])
    async def cmd_tenderize(self, ctx, url, saturation_amount=10000):
        url = find_url(url)
        if url is not None:
            return await ctx.response.send_message("I can't find a valid URL. ")
        image = ffmpeg.input(url)
        image = ffmpeg.hue(image, s=saturation_amount)
        ffmpeg.output(image, 'temp.jpg').run()
        with open('temp.jpg', 'rb') as export:
            df = disnake.File(export)
            await ctx.response.send_message("Here's your spicy, tender image:", file=df)
        os.remove('temp.jpg')


def setup(bot):
    bot.add_cog(Images(bot))
