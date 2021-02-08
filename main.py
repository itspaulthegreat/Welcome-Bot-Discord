import discord
import asyncio
import sys
import random
import re
import os
from discord.utils import get
import json
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='|', description="Daj eno zgodlej")

with open('config.json') as fh:
    client.config = json.load(fh)
    #client.run(client.config['token'])


@client.event
async def on_ready():
    print('Welcome message bot Logged in')
    print(client.user.name)
    print(client.user.id)
    print('-----')

newUserMessage = """your messages"""


@client.event
async def on_member_join(member):
    print("inside onmember oin function")
    if member.bot == True:
        botimg = '📈'
        role = get(member.guild.roles, name="BOTS")
        await member.add_roles(role)
        
    elif member.bot == False:
        memimg = '📈'
        await member.send("Welcome!We hope you have a great day here.")
        channel = client.get_channel(808012829285154886)
        
       
        await channel.send(f"EveryOne Please welcome {member.mention}. We hope you have a great day here.")
        role = get(member.guild.roles, name="Members")
        await member.add_roles(role)

   
        
    guild =  client.get_guild(807120796051832862) #get guild or discord server name

    memberchannel = client.get_channel(808082031456026665)
    botchannel = client.get_channel(808082696189247488)

    membercount = [mem for mem in guild.members if not mem.bot]
    botcount = [mem for mem in guild.members if mem.bot]
    await memberchannel.edit(name = memimg + 'Member count: {}'.format(len(membercount))) #member count
    await botchannel.edit(name = botimg + 'Bot count: {}'.format(len(botcount))) #bot count

@client.event       
async def on_member_remove(member):
    print("inside onmember oin function")
    if member.bot == True:
        botimg = '📉'
    elif member.bot == False:
        memimg = '📉'

        channel = client.get_channel(808094758244581438)
        
       
        await channel.send(f"Bye Bye {member.mention}. We hope you stay well.")
   
        
    guild =  client.get_guild(807120796051832862) #get guild or discord server name

    memberchannel = client.get_channel(808082031456026665)
    botchannel = client.get_channel(808082696189247488)

    membercount = [mem for mem in guild.members if not mem.bot]
    botcount = [mem for mem in guild.members if mem.bot]
    await memberchannel.edit(name = memimg + 'Member count: {}'.format(len(membercount))) #member count
    await botchannel.edit(name = botimg +'Bot count: {}'.format(len(botcount))) #bot count
  
      
    
# @loop(seconds=10)
# async def serverstats(ctx):
    




client.run(client.config['token']) #for local

#client.run(os.environ['token']) ##for hosting



#     member_count = len(ctx.guild.members) # includes bots
#     true_member_count = len([m for m in ctx.guild.member
#s if not m.bot])
# name = 'Member Count:' + member_count
#     names = 'Member Count no bots:' + true_member_count