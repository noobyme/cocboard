import discord
import asyncio
from cocapi import CocApi
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv()
TOKEN1 = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='|')

clantags = []
GUILD = os.getenv('DISCORD_GUILD')
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjA5OTA5Nzc1LWVkM2UtNDk3ZC05Mjg1LTc0YzQyNzViNjM4NyIsImlhdCI6MTYwMDUwMDgzMiwic3ViIjoiZGV2ZWxvcGVyLzc4MjEyYjViLTAyMjgtNmMyMS1mMDMyLThlNDNlNzZlMTZjMCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEyMi41Ny4wLjExOSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.yQzJnfE8gmeuVzG09qZC-QdvuzdWVU00N4lCXCMKMRdj69BWGfXlpcqxEbNsZw3Wvz8-1vWq-0ivqc2dYZceLg'
timeout = 1  # requests timeout
api = CocApi(token, timeout)

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
            clantags.append(arg[0:])
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
        for clantag in clantags:
            var1 = api.clan_tag(clantag)
            name = var1["name"]
            level = var1["clanLevel"]
            cwl = var1["warLeague"]["name"]
            members = var1['members']
            link = 'https://link.clashofclans.com/en?action=OpenClanProfile&tag=' + str(clantag[1:])
            dilist = [name + ' | Level:' + str(level), 'Members:' + str(members) + ' | ' + cwl, link]
            answers = "\n".join(f'{b}' for a, b in enumerate(dilist, 1))

            clanlist.append(answers)
        for clan in clanlist:
            send = "\n".join(f'{b}' for a, b in enumerate(clanlist, 1))
            abc = await place.send(send)
            await asyncio.sleep(5)
            await abc.delete()
            #id = abc.id
            #listofids.append(id)
        clanlist = []
    #for msgid in listofids:
        #await bot.delete_message(msgid)
        #listofids = []


@bot.command()
async def remove(ctx, arg):
    global clantags
    if arg in clantags:
        clantags.remove(arg)

bot.run(TOKEN1)