import discord
from discord.ext import commands


class Watcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("received")


async def setup(bot):
    await bot.add_cog(Watcher(bot))
