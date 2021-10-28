# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.
import disnake
from disnake.ext import commands
from disnake import Option, OptionType
from utils.languagetool_utils import get_matches, correct
import requests

class Language_Tool(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.language_codes = [lang['longCode'].lower() for lang in requests.get("https://api.languagetoolplus.com/v2/languages").json()]
    
    @commands.slash_command(
        name="proofread",
        description="Proofreads and replies with changed text.",
        options=[
            Option("text", "The text to proofread", OptionType.string, required=True),
            Option("lang", "Language to proofread in (default: en-US)", OptionType.string)
        ]
    )
    async def proofread(self, ctx, text, lang="en-us"):
        prefix=''
        if lang != "en-us":
            lang=lang.lower()
            if not lang in self.language_codes:
                prefix=f"It seems that your selected language ({lang}) is not a valid code. Language codes should be formatted by locale (eg en-US or fr). Falling back to English.\n\n"
                lang="en-us"
        matches = await get_matches(text, lang)
        if len(matches) == 0:
            await ctx.response.send_message(prefix+"No problems were detected with your text!")
            return
        corrected = correct(text, matches)
        await ctx.response.send_message(prefix+corrected)

def setup(bot):
    bot.add_cog(Language_Tool(bot))