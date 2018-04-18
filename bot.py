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

@bot.event
async def gamepresenceloop():
        while 1 == 1:
            await bot.change_presence(game=discord.Game(name='type "!help"'))
            time.sleep(15)
            await bot.change_presence(game=discord.Game(name='type "!math"'))
            time.sleep(15)
            await bot.change_presence(game=discord.Game(name='type "!info"'))
            time.sleep(15)

@bot.command(pass_context=True)
async def ping(ctx):
        embed = discord.Embed(title="Respone for !ping", color=0x00fff00)
        embed.add_field(name="Response" value=":ping_pong: PONG!")
        print("The user has issued the command !ping")

@bot.command(pass_context=True)
async def rcs(ctx):
        embed = discord.Embed(title="Respone for !rcs", color=0x00fff00)
        embed.add_field(name="Response" value="RILEIGH :heart:")
        print("The user has issued the command !rcs")

@bot.command(pass_context=True)
async def math(ctx):
        embed = discord.Embed(title="Respone for !math", color=0x00fff00)
        embed.add_field(name="Description", value="his command adds three variables together which returns a sum", inl$
        embed.add_field(name="Games you need to win", value=a + b + c, inline=True)
        embed.set_footer(text="v1.0.0")
        await bot.say(embed=embed)
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
        embed = discord.Embed(title="{}'s info" .format(user.name), color=0x00fff00)
        embed.set_footer(text="v1.0.0")
        embed.add_field(name="Status", value="{}" .format(user.status), inline=True)
        embed.add_field(name="ID", value="{}" .format(user.id), inline=True)
        embed.add_field(name="Role", value="{}" .format(user.top_role), inline=True)
        embed.add_field(name="Joined", value="{}" .format(user.joined_at), inline=True)
        await bot.say(embed=embed)
        print("The user has issued the command !info")

bot.run("NDM0NDMyOTczMzYyOTU0MjQx.DbZsFg.YBXSYlhU0pICJgiCv1smjhuefLc")
