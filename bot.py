import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

a = 2
b = 2
c = 2


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
        print("BOT IS READY")
        print("BOT IS ONLINE WITH USERNAME: " + bot.user.name)


@bot.command(pass_context=True)
async def ping(ctx):
        await bot.say("Pong!")
        print("The user has issued the command !ping")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
        await bot.say("Your username is: " .format(user.name))
        await bot.say("The users ID is: " .format(user.id))
        await bot.say("The users status is: " .format(user.status))
        await bot.say("The users highest role is: " .format(user.top_role))
        await bot.say("The user specified joined this server at: ") .format(user.joined_at))
        print("The user has issued the command !ping")


@bot.command(pass_context=True)
async def math(ctx):
        await bot.say("```YO I AM SO BLOCKED RN```")
        await bot.say(a + b + c)
        print("The user has issued the command !math")


bot.run("NDM0NDMyOTczMzYyOTU0MjQx.DbZsFg.YBXSYlhU0pICJgiCv1smjhuefLc")
