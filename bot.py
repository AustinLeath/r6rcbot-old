import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
        print("BOT IS READY")
        print("TIME TO BOOL MY GUY")


@bot.command(pass_context=True)
async def ping(ctx):
        await bot.say("Pong!")
        print("The user has issued the command !ping")


@bot.command(pass_context=True)
async def ding(ctx):
        await bot.say("Dong!")
        print("The user has issued the command !ping")


@bot.command(pass_context=True)
async def ring(ctx):
        await bot.say("Rong!")
        print("The user has issued the command !ping")

bot.run("NDM0NDMyOTczMzYyOTU0MjQx.DbZsFg.YBXSYlhU0pICJgiCv1smjhuefLc")
