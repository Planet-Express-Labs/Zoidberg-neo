# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.
import disnake
from disnake.ext import commands
from disnake import Option, OptionType
from utils.languagetool_utils import get_matches, correct
import requests
from async_google_trans_new import AsyncTranslator
from async_google_trans_new.constant import LANGUAGES

class Text_Processor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ltool_codes = ['auto']+[lang['longCode'].lower() for lang in requests.get("https://api.languagetoolplus.com/v2/languages").json()]
        self.translate_langs = LANGUAGES
        self.translator = AsyncTranslator()

    @commands.slash_command(
        name="proofread",
        description="Proofreads and replies with changed text.",
        options=[
            Option("text", "The text to proofread", OptionType.string, required=True),
            Option("lang", "Language to proofread in (default: en-US)", OptionType.string)
        ]
    )
    async def proofread(self, ctx, text, lang="auto"):
        prefix = ''
        if lang != "auto":
            lang = lang.lower()
            if not lang in self.ltool_codes:
                prefix = f"It seems that your selected language ({lang}) is not supported. Language codes should be formatted by locale (eg. en-US or fr). Falling back to Automatic.\n\n"
                lang = "auto"
        matches = await get_matches(text, lang)
        if len(matches) == 0:
            await ctx.response.send_message(prefix+"No problems were detected with your text!")
            return
        corrected = correct(text, matches)
        await ctx.response.send_message(prefix+corrected)

    @commands.slash_command(
        name="translate",
        description="Translates text to a new language!",
        options=[
            Option("text", "The text to translate", OptionType.string, required=True),
            Option("lang", "Language to translate to (default: en)", OptionType.string)
        ]
    )
    async def translate(self, ctx, text, lang="en"):
        prefix = ''
        if lang != "en":
            lang = lang.lower()
            if lang not in self.translate_langs:
                prefix = f"It seems your selected language ({lang}) is not supported. Language codes should be formatted by 2-letter locale (eg. en or fr). Falling back to English.\n\n"
                lang = "en"
        text = await self.translator.translate(text, lang)
        await ctx.response.send_message(prefix + text)

    @commands.command(name="proofread")
    async def proofread(self, ctx):
        ref = ctx.message.reference
        if ref is not None and ref.resolved:
            replied_to = await ctx.channel.fetch_message(ref.message_id)
            text = replied_to.content
            if not text:
                return
            matches = await get_matches(text, "en")
            if len(matches) == 0:
                await replied_to.reply("No problems were detected with your text!", mention_author=False)
                return
            corrected = correct(text, matches)
            await replied_to.reply(corrected, mention_author=False)

    @commands.command(name="translate")
    async def translate(self, ctx):
        ref = ctx.message.reference
        if ref is not None and ref.resolved:
            replied_to = await ctx.channel.fetch_message(ref.message_id)
            text = replied_to.content
            if not text:
                return
            translated = await self.translator.translate(text, "en")
            await replied_to.reply(translated, mention_author=False)

def setup(bot):
    bot.add_cog(Text_Processor(bot))