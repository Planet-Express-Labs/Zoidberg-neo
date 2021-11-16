# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.
import asyncio
from time import sleep

import disnake
import threading

from disnake import ApplicationCommandInteraction
from disnake.enums import *
from disnake.ext import commands

from database import databases
from main import __version__
from main import bot


async def wait_for_text_input(inter: ApplicationCommandInteraction):

    @disnake.ui.button(label="Skip", style=ButtonStyle.red)
    async def skip_button():
        return

    def check(m):
        # check if the message is from the correct person and channel
        if m.channel.id == inter.channel.id and m.author.id == inter.author.id:
            return m.content

    # await inter.response.defer()
    message = await inter.channel.send("Waiting for response...")
    try:
        resp = await bot.wait_for('message', check=check)
    except asyncio.TimeoutError:
        await inter.response.send_message("Timeout reached. Try again. ")


async def image_filtering_menu(inter: ApplicationCommandInteraction):

    @disnake.ui.button(label="Skip", style=ButtonStyle.red)
    async def skip_button():
        return

    def check(m):
        # check if the message is from the correct person and channel
        if m.channel.id == inter.channel.id and m.author.id == inter.author.id:
            return m.content

    # await inter.response.defer()
    message = await inter.channel.send("Waiting for response...")
    try:
        resp = await bot.wait_for('message', check=check)
    except asyncio.TimeoutError:
        await inter.response.send_message("Timeout reached. Try again. ")


async def first_time(inter):
    # TODO: FORCE to read from a JSON file.
    embed = disnake.Embed(title="Zoidberg server setup")
    embed.description = """
        Welcome to Zoidberg! I am your new moderation assistant.
        I can automatically delete images that I detect as NSFW, detect spam, and more.
        This wizard will help you configure all of Zoidberg's options.
        I'll update you if we add anything new in your community updates channel.
        
        Each option will have either a button or a text option that I will listen for.
        If you don't want to specify an option, click the skip button.
        
        Send the message "next" to progress onto the next screen.
        1/4
        """
    resp = await inter.response.send_message(embed=embed)
    await wait_for_text_input(inter)
    embed.description = """
        Would you like to enable image filtering? We use state of the art AI models to detect NSFW images.

        Commonly found NSFW images are stored in a database to reduce load.
        We do not store copies of images that are detected, only a hash that can't be turned back into an image.

        AI Filtering uses advanced AI to detect NSFW images. This includes images containing gore.
            This feature will send a copy of any new image, in enabled channels, to our image processing partners.

        Hash filtering uses our database to detect common images that may not be detected by AI.
        These images usually don't contain nudity, but are still extremely suggestive

        You can configure which channels will use this filter on the next page.
        2/4"""
    await resp.edit(embed=embed)


class Configuration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='setup', brief="Helps you set up Zoidberg to your needs. ")
    async def cmd_setup(self, inter):
        pass

    @cmd_setup.sub_command(name='general-server', brief='Configures options for your server')
    async def sub_server(self, inter):
        # document = await databases.Server.find_one({'server_id': inter.guild.id})
        if None is None:
            await first_time(inter)


def setup(bot):
    bot.add_cog(Configuration(bot))
