import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import math
import re
# below fetches the path and securely reads the token
path = 'token.txt'
token_file = open(path,'r')
token = token_file.read()
tokenmain = token.strip()
# below is a variable that stores the prefix in which A user inputs in Discord, for instance: "!ping", where the "!", symbolizes the usage of a command
# for instance: "!ping", where the "!" in front of "ping" symbolizes the usage of a command which then captures the the string
# that comes directly after "!" which then executes a command, if valid
bot = commands.Bot(command_prefix="!")
bot.remove_command('help')
# below is the on_ready event which is ALWAYS required
@bot.event
async def on_ready():
    print("Using the Token: " + tokenmain)
    print("BOT IS READY WITH USER ID: " + bot.user.id)
    print("BOT IS ONLINE WITH USERNAME: " + bot.user.name)
    while 1 == 1:
        await bot.change_presence(game=discord.Game(name='type !help'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='type !calc'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='type !list'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='type !server'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='type !about'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='type !invite'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='type !app'))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name='type !website'))
        await asyncio.sleep(20)

@bot.command(pass_context=True)
async def help(ctx):
    await bot.say('**!help** : displays this message')
    await bot.say('**!info** : displays information about a user')
    await bot.say('**!about** : gives A user more information about the bot and the developer')
    await bot.say('**!invite** : gives A user a link to invite the R6RC bot to their Discord')
    await bot.say('**!app** : gives A user a link to the direct download for the R6RC desktop application')
    await bot.say('**!twitter** : displays a dialogue directing A user to the R6RC Twitter account')
    await bot.say('**!website** : gives A user a link to the online version of R6RC')
    await bot.say('**!calc** : calculates user ranks when you give it three sets of data like this: **!calc MMR ELO GOAL**')
    await bot.say('**!list** : displays all ranks with their associated MMR values')
    await bot.say('**!server** : displays an invite to the official R6RC server')

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info" .format(user.name), color=0x00fff00)
    embed.set_footer(text="v1.0.0 - @Game-King#0519")
    embed.add_field(name="Status", value="{}" .format(user.status), inline=True)
    embed.add_field(name="ID", value="{}" .format(user.id), inline=True)
    embed.add_field(name="Role", value="{}" .format(user.top_role), inline=True)
    embed.add_field(name="Joined", value="{}" .format(user.joined_at), inline=True)
    await bot.say(embed=embed)
    print("A user has issued the command !info")

@bot.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(title="About the developer", color=0x00fff00)
    embed.add_field(name="Info", value="The developer of this bot is Austin Leath, he is a young web engineer looking for work. If you would like to contact him send him an email at austinleath18@gmail.com")
    embed.set_footer(text="v1.0.0 - @Game-King#0519")
    await bot.say(embed=embed)
    print("A user has issued the command !about")

@bot.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(title="Invite the R6RC bot to your server!", color=0x00fff00)
    embed.add_field(name="Link", value="https://discordapp.com/api/oauth2/authorize?client_id=434432973362954241&permissions=8&scope=bot")
    embed.set_footer(text="v1.0.0 - @Game-King#0519")
    await bot.say(embed=embed)
    print("A user has issued the command !invite")

@bot.command(pass_context=True)
async def app(ctx):
    embed = discord.Embed(title="Get the R6RC desktop app!", color=0x00fff00)
    embed.add_field(name="Link", value="https://electronjs.org/apps/r6rc")
    embed.set_footer(text="v1.0.0 - @Game-King#0519")
    await bot.say(embed=embed)
    print("A user has issued the command !app")

@bot.command(pass_context=True)
async def twitter(ctx):
    embed = discord.Embed(title="Follow R6RC on Twitter!", color=0x00fff00)
    embed.add_field(name="Link", value="https://twitter.com/R6RankCalc")
    embed.set_footer(text="v1.0.0 - @Game-King#0519")
    await bot.say(embed=embed)
    print("A user has issued the command !twitter")

@bot.command(pass_context=True)
async def website(ctx):
    embed = discord.Embed(title="Visit the R6RC website!", color=0x00fff00)
    embed.add_field(name="Link", value="https://r6rc.com")
    embed.set_footer(text="v1.0.0 - @Game-King#0519")
    await bot.say(embed=embed)
    print("A user has issued the command !website")

@bot.command(pass_context=True)
async def calc(ctx, arg1, arg2, arg3):
    send_typing(message.channel)
    mmr = str(arg1)
    elo = str(arg2)
    goal = str(arg3)

    SearchObjOne = re.search(r"[\D+]", mmr, re.I)
    SearchObjTwo = re.search(r"[\D+]", elo, re.I)
    SearchObjThree = re.search(r"[\D+]", goal, re.I)

    if(SearchObjOne):
        await bot.say('Some of the characters that you entered were not integers, please try again')
        print("A user has issued the command !calc with some characters that were not integers")
    elif(SearchObjTwo):
        await bot.say('Some of the characters that you entered were not integers, please try again')
        print("A user has issued the command !calc with some characters that were not integers")
    elif(SearchObjThree):
        await bot.say('Some of the characters that you entered were not integers, please try again')
        print("A user has issued the command !calc with some characters that were not integers")
    elif(int(mmr) < -10000 or int(mmr) > 10000):
        await bot.say('Some of the numbers that you entered were either above the maximum or below the minimum value that R6RC supports, please try again')
        print("A user has issued the command !calc with some characters that were either above the maximum or below the minimum value that R6RC supports")
    elif(int(elo) < 1 or int(elo) > 500):
        await bot.say('Some of the numbers that you entered were either above the maximum or below the minimum value that R6RC supports, please try again')
        print("A user has issued the command !calc with some characters that were either above the maximum or below the minimum value that R6RC supports")
    elif(int(goal) < -10000 or int(goal) > 10000):
        await bot.say('Some of the numbers that you entered were either above the maximum or below the minimum value that R6RC supports, please try again')
        print("A user has issued the command !calc with some characters that were either above the maximum or below the minimum value that R6RC supports")
    else:
        mmr = int(arg1)
        elo = int(arg2)
        goal = int(arg3)

        equation = (goal - mmr) / elo
        round = int(math.ceil(equation))
        final = str(int(math.fabs(round)))

        if(final == "0"):
            final = ""

        if(round < 0):
            winorlose = "You need to lose "
        elif(round > 0):
            winorlose = "You need to win "
        else:
            winorlose = "You do not need to win or lose any "
        if(int(math.fabs(round)) == 1):
            matchcount = " (± 1) match "
        elif(int(math.fabs(round)) > 1):
            matchcount = " (± 1) matches "
        else:
            matchcount = "matches "


        embed = discord.Embed(
            title = 'R6RC !calc',
            description = 'Response to !calc',
            color = discord.Colour.blue()
        )

        embed.add_field(name='MMR', value=str(mmr) + inline=True)
        embed.add_field(name='ELO', value=str(elo) + inline=True)
        embed.add_field(name='GOAL', value=str(goal) + inline=True)
        #embed.add_field(name='RESPONSE', value=winorlose + final + matchcount +'to reach your goal')
        #embed.set_footer("Get this bot on your server from r6rc.com/discord")
        print("A user has issued the command !calc")

@bot.command(pass_context=True)
async def list(ctx):
    await bot.say('https://imgur.com/dc1REQz')
    print("A user has issued the command !list")

@bot.command(pass_context=True)
async def server(ctx):
    await bot.say('https://discord.gg/NaAmbbb')
    print("A user has issued the command !server")

bot.run(tokenmain)
