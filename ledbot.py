# for Discord command array
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import math
# for GPIO LED array
import RPi.GPIO as GPIO
import time
#GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO LED's that are going to be in use
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
# fetches the path and securely reads the token
path = 'token.txt'
token_file = open(path,'r')
token = token_file.read()
tokenmain = token.strip()
# variables and equations that formulate a response
mmr = 1300
elo = 100
goal = 4500
equation = (goal - mmr) / elo
round = math.ceil(equation)
final = math.fabs(round)
# stores the prefix in which the user inputs in Discord, for instance: "!ping", where the "!", signifies the usage of a command
# for instance: "!ping", where the "!", signifies the usage of a command followed by a string which coorelates to a defined command
bot = commands.Bot(command_prefix="!")
# After this is completed the bot starts
@bot.event
async def on_ready():
        print("Using the Token: " + tokenmain)
        print("BOT IS READY WITH USER ID: " + bot.user.id)
        print("BOT IS ONLINE WITH USERNAME: " + bot.user.name)
        while 1 == 1:
            GPIO.output(17,GPIO.HIGH)
            await bot.change_presence(game=discord.Game(name='type !help'))
            await asyncio.sleep(5)
            await bot.change_presence(game=discord.Game(name='type !math'))
            await asyncio.sleep(5)
            await bot.change_presence(game=discord.Game(name='type !about'))
            GPIO.output(17,GPIO.LOW)
            await asyncio.sleep(5)
# !ping command
@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("PONG!")
	print("The user has issued the command !ping")
# !math command
@bot.command(pass_context=True)
async def math(ctx):
        GPIO.output(22,GPIO.HIGH)
        await asyncio.sleep(5)
        GPIO.output(22,GPIO.LOW)
        embed = discord.Embed(title="Respone for !math", color=0x00fff00)
        embed.add_field(name="Description", value="This command adds three variables together which returns a sum", inline=True)
        embed.add_field(name="You need to play", value=final, inline=True)
        embed.add_field(name="Since your MMR is:", value=mmr, inline=True)
        embed.add_field(name="Since your current ELO per match is:", value=elo, inline=True)
        embed.add_field(name="Also because your goal is:", value=goal, inline=True)
        embed.set_footer(text="v1.0.0 - @Game-King#0519")
        await bot.say(embed=embed)
        print("The user has issued the command !math")
        GPIO.output(22,GPIO.HIGH)
        await asyncio.sleep(5)
        GPIO.output(22,GPIO.LOW)
# !about command
@bot.command(pass_context=True)
async def about(ctx):
        embed = discord.Embed(title="About The Author", color=0x00fff00)
        embed.add_field(name="Info", value="Austin is a young web engineer looking for work. If you would like to contact him send him an email at austinleath18@gmail.com")
        embed.set_footer(text="v1.0.0 - @Game-King#0519")
        await bot.say(embed=embed)
        print("The user has issued the command !about")
# !invite command
@bot.command(pass_context=True)
async def invite(ctx):
        embed = discord.Embed(title="Invite me to your server!", color=0x00fff00)
        embed.add_field(name="Link", value="https://discordapp.com/api/oauth2/authorize?client_id=434432973362954241&permissions=8&scope=bot", inline=True)
        embed.set_footer(text="v1.0.0 - @Game-King#0519")
        await bot.say(embed=embed)
        print("The user has issued the command !invite")
# !info command
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
        embed = discord.Embed(title="{}'s info" .format(user.name), color=0x00fff00)
        embed.set_footer(text="v1.0.0 - @Game-King#0519")
        embed.add_field(name="Status", value="{}" .format(user.status), inline=True)
        embed.add_field(name="ID", value="{}" .format(user.id), inline=True)
        embed.add_field(name="Role", value="{}" .format(user.top_role), inline=True)
        embed.add_field(name="Joined", value="{}" .format(user.joined_at), inline=True)
        await bot.say(embed=embed)
        print("The user has issued the command !info")
# Reads token which in turn activates the bot
bot.run(tokenmain)
