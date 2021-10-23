#join the server lmao: https://discord.gg/XjSHq6VPYz

import discord
import os
from keep_alive import keep_alive
import asyncio
import time
import datetime
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import requests
import json
from time import *
#just importing stuff


intents = discord.Intents.none()
intents.reactions = True
intents.members = True
intents.guilds = True
intents.typing = True
intents.presences = True
intents.messages=True 
intents.guilds=True
#client = discord.Client()
client = commands.Bot(command_prefix = '+', intents = intents)
#prefix set
client.remove_command('help')
setup = False

servers = {}


@client.event
async def on_ready():
    print("bot online B)")
    await client.change_presence(activity=discord.Game('with my itty bitty toes uwu'))

@client.event
async def on_member_join(member):
    print(member)
    print(member.guild.id)

    with open('servers.json', 'r') as f:
      serverdict = json.load(f)

    joinTestEmbed = discord.Embed(
        title = "New Member Alert!",
        color = 0x63cf5b,
        description = "A new user has joined this here server! Please welcome" + member.mention + "!"
    ) 
    joinTestEmbed.set_thumbnail(url=member.avatar_url)
    cid = int()
    for server in serverdict:
      if int(server) == member.guild.id:
        print("check")
        cid = serverdict[server] 
    print("cid: ",cid)
    channel = client.get_channel(cid)
    print(channel)
    await channel.send(embed=joinTestEmbed)
    await member.send(f'Hey, {member} welcome to {member.guild.name}! Enjoy your stay!')



@client.event
async def on_member_remove(member : discord.Member):
    with open('servers.json', 'r') as f:
      serverdict = json.load(f)
    leavetestEmbed = discord.Embed(
        title = "Someone Left!",
        color = 0xff0000,
        description = member.mention + " has left the server."
    )
    cid2 = int()
    for server in serverdict:
      if int(server) == member.guild.id:
        print("check")
        cid2 = serverdict[server] 
    print("cid: ",cid2)
    channel = client.get_channel(cid2)
    print(channel)
    await channel.send(embed=leavetestEmbed)

@client.command()
async def dm(ctx, member : discord.Member):
    await member.send(member.guild.name)

@client.command()
async def setupmanual(ctx, welcome):
    print(welcome)
    illegalchar = ["<", ">", "#"]
    for x in illegalchar:
        if x in welcome:
                welcome.replace(x, "")
    with open('servers.json', 'r') as f:
        serverdict = json.load(f)
    if ctx.channel.id == ValueError:
        await ctx.reply("bru this isn\'t id")
    else:
        await ctx.reply('Done 👍')
        await ctx.send(str(ctx.message.guild.id))
        serverdict.update(dict({str(ctx.message.guild.id) : welcome}))
        with open('servers.json', 'w') as f:
            json.dump(serverdict, f)
#            
@client.command()
async def setupauto(ctx):
    with open('servers.json', 'r') as f:
        serverdict = json.load(f)
    if ctx.channel.id == ValueError:
        await ctx.reply("bru this isn\'t id")
    else:
        await ctx.reply('Done 👍')
        welcome = ctx.channel.id
        await ctx.send(str(ctx.guild.id))
        serverdict.update(dict({str(ctx.guild.id) : welcome}))
        with open('servers.json', 'w') as f:
            json.dump(serverdict, f)
#test command
@client.command()
async def test(ctx):
    with open('servers.json', 'r') as f:
        serverdict = json.load(f)
    await ctx.send(serverdict[str(ctx.guild.id)])
#weather command for longitude & latitude
@client.command()
async def weatherll(ctx, lat = None, lon = None):
    try:
        weatherurl = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=38de2f98cf6e68962cc0fba3018c5311')
        temperature = str(round((weatherurl.json().get('main').get('temp')-273.15)*(9/5)+32))
        desc = weatherurl.json().get('weather')[0].get('description')
        windspeed = str(weatherurl.json().get('wind').get('speed'))
        winddeg = str(weatherurl.json().get('wind').get('deg'))
        city = weatherurl.json().get('name')
        if int(temperature) >= 80:
            decis = "Drink lots of water today! (and maybe consider bringing a hat!)"
        elif int(temperature) >= 70 and int(temperature) < 80:
            decis = "Just wear some shorts/pants and a T-Shirt."
        elif int(temperature) < 70:
            decis = "Bring a jacket and wear pants today!"
        weatherembed =discord.Embed(
            title="Today\'s Weather at " + city,
            description="Right now, it's currently " + temperature + " degrees. The description for the type of weather we're having is \"" + desc + "\". The wind is moving at " + windspeed + " mph and is moving in the direction of " + winddeg + " degrees. " + decis, 
            color=discord.Color.blue()
        )
        await ctx.send(embed=weatherembed)
    except TypeError:
        await ctx.send("You silly goose, you forgot to put in a longitude and latitude!")
#weather command for cities
@client.command()
async def weatherc(ctx, *args):
    try:
        print(args[:])
        city =" ".join(args[:])
        print(city)
        newcity = city.replace(" ", "%20")
        cweatherurl = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + newcity + '&appid=38de2f98cf6e68962cc0fba3018c5311')
        temperature = str(round((cweatherurl.json().get('main').get('temp')-273.15)*(9/5)+32))
        desc = cweatherurl.json().get('weather')[0].get('description')
        windspeed = str(cweatherurl.json().get('wind').get('speed'))
        winddeg = str(cweatherurl.json().get('wind').get('deg'))
        city = cweatherurl.json().get('name')
        if int(temperature) >= 80:
            decis = "Drink lots of water today! (and maybe consider bringing a hat!)"
        elif int(temperature) >= 70 and int(temperature) < 80:
            decis = "Just wear some shorts/pants and a T-Shirt."
        elif int(temperature) < 70:
            decis = "Bring a jacket and wear pants today!"
        weatherembed =discord.Embed(
            title="Today\'s Weather at " + city,
            description="Right now, it's currently " + temperature + " degrees. The description for the type of weather we're having is \"" + desc + "\". The wind is moving at " + windspeed + " mph and is moving in the direction of " + winddeg + " degrees. " + decis, 
            color=discord.Color.blue()
        )
        await ctx.send(embed=weatherembed)
    except TypeError:
        await ctx.send("You silly goose, you forgot to put in a city!")
    except AttributeError:
        await ctx.send("Bruh that city doesn't exist m'lad")

@client.command()
async def jointest(ctx, member : discord.Member):
    joinTestEmbed = discord.Embed(
        title = "New Member Alert!",
        color = 0x63cf5b,
        description = "A new user has joined this here server! Please welcome" + member.mention + "!"
    ) 
    joinTestEmbed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=joinTestEmbed)

@client.command(pass_context=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)
    await ctx.send(f'{amount} messages have been purged by {ctx.message.author.mention}')



keep_alive()



client.run(os.environ['token'])