#join the server lmao: https://discord.gg/XjSHq6VPYz

import discord
import os
from keep_alive import keep_alive
import time
import datetime
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import requests
import json
#just importing stuff



client = discord.Client()

client = commands.Bot(command_prefix = '-')
#prefix set

setup = False

servers = {}

@client.event
async def on_ready():
    print("bot online B)")
    await client.change_presence(activity=discord.Game('with my itty bitty toes uwu'))

@client.command()
async def setup(ctx, welcome):
    if int(welcome) == ValueError:
        await ctx.reply("bru this isn\'t id")
    else:
        await ctx.reply('Done 👍')
        servers[str(ctx.message.guild.id)] = welcome
        with open('servers.json', 'w') as f:
            json.dump(servers, f)
        


@client.command()
async def test(ctx):
        await ctx.send("yo uhh if you can see this message the bot works lmao")

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

@client.event
async def on_member_join(ctx, member : discord.Member):
    server = client.get_server("886401901887914025")
    for channel in server.channels:
        if "welcome" in channel.name:
            continue
    joinTestEmbed = discord.Embed(
        title = "New Member Alert!",
        color = 0x63cf5b,
        description = "A new user has joined this here server! Please welcome" + member.mention + "!"
    ) 
    joinTestEmbed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=joinTestEmbed)

keep_alive()
client.run("ODgzNTMwNzk5MjU1NzgxNDM3.YTLSLQ.GFmvPqibdmtbQBDUNpP7VjOmXho")