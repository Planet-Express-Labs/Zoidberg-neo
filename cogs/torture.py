# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.
import disnake
from disnake.ext import commands
from disnake import Option, OptionType

class Torture(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.toTorture={}
    
    @commands.has_permissions(manage_messages=True)
    @commands.slash_command(
        name="torture",
        description="Ruthlessly torture your enemies!",
        options=[
            Option("torturee", "Person to torture", OptionType.user, required=True)
        ]
    )
    async def torture(self, ctx, torturee):
        if torturee.id in self.toTorture.get(ctx.guild.id, {}):
            self.toTorture[ctx.guild.id].pop(torturee.id)
            await ctx.response.send_message(f"No longer torturing {torturee.mention}")
        else:
            self.toTorture[ctx.guild.id]=self.toTorture.get(ctx.guild.id,{}) | {torturee.id:True}
            await ctx.response.send_message(f"Torturing {torturee.mention}! Brace yourself!")
    
    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        if user.id in self.toTorture.get(channel.guild.id,{}):
            await channel.send(f"What are you typing, {user.mention}???")

def setup(bot):
    bot.add_cog(Torture(bot))