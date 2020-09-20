import discord
import asyncio
from cocapi import CocApi
from dotenv import load_dotenv
from discord.ext import commands
import os
import re


load_dotenv()
TOKEN1 = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
token = os.getenv('token')

fileopen = open("list.txt", "r")
file = fileopen.read()
print(file + "17")
clantags = re.sub("[^#\w]", " ",  file).split()
print(clantags)
print("20")
taglist = []
fileopen.close()

timeout = 1  # requests timeout
api = CocApi(token, timeout)

bot = commands.Bot(command_prefix='|')
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.command()
async def add(ctx, arg):
    if arg.startswith('#') and arg not in clantags:
        var = api.clan_tag(arg[0:])
        print(var)
        if len(var) < 4:
            print("notFound")
        else:
            clantags.append(str(arg[0:]))
            tagstring = ' '.join(clantags)
            fileopen = open("list.txt", "w")
            fileopen.write("\"" + str(tagstring) + "\"")
            fileopen.close()
            print("52")
            print(taglist)
            print(tagstring)
            print(file)
            print(clantags)


global clanlist
clanlist = []
@bot.command()
async def channel(ctx):

    """for clantag in clantags:
        var1 = api.clan_tag(clantag)
        name = var1["name"]
        level = var1["clanLevel"]
        cwl = var1["warLeague"]["name"]
        members = var1['members']
        link = 'https://link.clashofclans.com/en?action=OpenClanProfile&tag=' + str(clantag[1:])
        dilist = [name + ' | Level:'+str(level) ,'Members:' + str(members) +' | '+ cwl , link]
        answers = "\n".join(f'{b}' for a, b in enumerate(dilist, 1))
        clanlist.append(answers)"""
@bot.command()
async def board(ctx):

    #listofids = []
    global clanlist
    global place
    place = ctx.channel
    ii = 1
    while ii ==  1:
        fileopen = open("list.txt", "r")
        file = fileopen.read()
        clantags = re.sub("[^\w]", " ", file).split()
        for clantag in clantags:
            var1 = api.clan_tag("#"+clantag)
            name = var1["name"]
            level = var1["clanLevel"]
            cwl = var1["warLeague"]["name"]
            members = var1['members']
            link = 'https://link.clashofclans.com/en?action=OpenClanProfile&tag=' + str(clantag[0:])
            dilist = [name + ' | Level:' + str(level), 'Members:' + str(members) + ' | ' + cwl, link]
            answers = "\n".join(f'{b}' for a, b in enumerate(dilist, 1))

            clanlist.append(answers)
        for clan in clanlist:
            send = "\n".join(f'{b}' for a, b in enumerate(clanlist, 1))
            abc = await place.send(send)
            await asyncio.sleep(60)
            await abc.delete()
            print("102")
            #id = abc.id
            #listofids.append(id)
        clanlist = []

    #for msgid in listofids:
        #await bot.delete_message(msgid)
        #listofids = []


@bot.command()
async def remove(ctx, arg):
    global clantags
    print("116")
    print(clantags)
    print(taglist)
    if arg in clantags:
        clantags.remove(arg)
        var2 = ' '.join(clantags)
        print(var2 + "121")
        fileopen = open("list.txt", "w")
        fileopen.write("\"" + str(var2) + "\"")
        fileopen.close()
        print("126")
        print(clantags)

bot.run(TOKEN1)
