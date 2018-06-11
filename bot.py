import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import math
# below fetches the path and securely reads the token
path = 'token.txt'
token_file = open(path,'r')
token = token_file.read()
tokenmain = token.strip()
# below is a list of variables that stores information for the "!math" command
mmr = 1300
elo = 100
goal = 4500
equation = (goal - mmr) / elo
round = math.ceil(equation)
final = math.fabs(round)
# below is a variable that stores the prefix in which the user inputs in Discord, for instance: "!ping", where the "!", symbolizes the usage of a command
# for instance: "!ping", where the "!" in front of "ping" symbolizes the usage of a command which then captures the the string
# that comes directly after "!" which then executes a command, if valid
bot = commands.Bot(command_prefix="!")
# below is the on_ready event which is ALWAYS required
@bot.event
async def on_ready():
        print("Using the Token: " + tokenmain)
        print("BOT IS READY WITH USER ID: " + bot.user.id)
        print("BOT IS ONLINE WITH USERNAME: " + bot.user.name)
        while 1 == 1:
            await bot.change_presence(game=discord.Game(name='type !help'))
            await asyncio.sleep(20)
            await bot.change_presence(game=discord.Game(name='type !math'))
            await asyncio.sleep(20)
            await bot.change_presence(game=discord.Game(name='type !about'))
            await asyncio.sleep(20)
            await bot.change_presence(game=discord.Game(name='type !invite'))
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
        embed.add_field(name="You need to play", value=final, inline=True)
        embed.add_field(name="Your current MMR is:", value=mmr, inline=True)
        embed.add_field(name="Your current ELO per match is:", value=elo, inline=True)
        embed.add_field(name="The your goal is:", value=goal, inline=True)
        embed.set_footer(text="v1.0.0 - @Game-King#0519")
        await bot.say(embed=embed)
        print("The user has issued the command !math")

@bot.command(pass_context=True)
async def about(ctx):
        embed = discord.Embed(title="About The Author", color=0x00fff00)
        embed.add_field(name="Info", value="Austin is a young web engineer looking for work. If you would like to contact him send him an email at austinleath18@gmail.com")
        embed.set_footer(text="v1.0.0 - @Game-King#0519")
        await bot.say(embed=embed)
        print("The user has issued the command !about")

@bot.command(pass_context=True)
async def invite(ctx):
        embed = discord.Embed(title="Invite me to your server!", color=0x00fff00)
        embed.add_field(name="Link", value="https://discordapp.com/api/oauth2/authorize?client_id=434432973362954241&permissions=8&scope=bot")
        embed.set_footer(text="v1.0.0 - @Game-King#0519")
        await bot.say(embed=embed)
        print("The user has issued the command !invite")

@bot.command(pass_context=True)
async def app(ctx):
        embed = discord.Embed(title="Get the desktop app!", color=0x00fff00)
        embed.add_field(name="Link", value="https://electronjs.org/apps/mmrcalculator")
        embed.set_footer(text="v1.0.0 - @Game-King#0519")
        await bot.say(embed=embed)
        print("The user has issued the command !app")

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

bot.run(tokenmain)
