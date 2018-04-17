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
        await bot.change_presence(game=discord.Game(name='type "!help"'))


@bot.command(pass_context=True)
async def ping(ctx):
        await bot.say("Pong!")
        print("The user has issued the command !ping")

@bot.command(pass_context=True)
async def rcs(ctx):
        await bot.say("RILEIGH :heart:")
        print("The user has issued the command !rcs")


@bot.command(pass_context=True)
async def math(ctx):
        await bot.say("")
        await bot.say(a + b + c)
        print("The user has issued the command !math")

@bot.command(pass_context=True)
async def about(ctx):
        embed = discord.Embed(title="About The Author", color=0x00fff00)
        embed.set_footer(text="v1.0.0")
        embed.add_field(name="Austin is a young web engineer looking for work. If you would like to contact him send him an email at austinleath18@gmail.com", value="test")
        embed.set_author(name="Austin Leath AKA - @Game-King#0519")
        await bot.say(embed=embed)
        print("The user has issued the command !about")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
        embed = discord.Embed(title="{}'s info" .format(user.name) color=0x00fff00)
        embed.set_footer(text="v1.0.0")
        embed.add_field(name="Name", value="user.name")
        embed.add_field(name="Status", value="user.status")
        embed.add_field(name="ID", value="user.id")
        embed.add_field(name="Role", value="user.role")
        embed.add_field(name="Joined", value="user.joined_at")
        embed.set_thumbnail(url-user.avatar_url)
        await bot.say(embed=embed)
        print("The user has issued the command !info")


bot.run("NDM0NDMyOTczMzYyOTU0MjQx.DbZsFg.YBXSYlhU0pICJgiCv1smjhuefLc")
