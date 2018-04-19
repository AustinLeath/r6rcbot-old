import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

path = 'token.txt'
token_file = open(path,'r')
token = token_file.read()
tokenmain = token.strip()

mmr = 1300
elo = 100
goal = 4500

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
        print("Using the Token: " + tokenmain)
        print("BOT IS READY")
        print("BOT IS ONLINE WITH USERNAME: " + bot.user.name)
        while 1 == 1:
            await bot.change_presence(game=discord.Game(name='type !help'))
            await asyncio.sleep(20)
            await bot.change_presence(game=discord.Game(name='type !math'))
            await asyncio.sleep(20)
            await bot.change_presence(game=discord.Game(name='type !about'))
            await asyncio.sleep(20)

@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("PONG!")
	print("The user has issued the command !ping")

@bot.command(pass_context=True)
async def rcs(ctx):
	await bot.say("RILEIGH :heart:")
	print("The user has issued the command !rcs")

@bot.command(pass_context=True)
async def math(ctx):
        embed = discord.Embed(title="Respone for !math", color=0x00fff00)
        embed.add_field(name="Description", value="This command adds three variables together which returns a sum", inline=True)
        embed.add_field(name="Games you need to win", value=(goal - mmr) / elo, inline=True)
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

bot.run(tokenmain)
