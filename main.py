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

# with open('config.json') as fh:
#     client.config =  json.load(fh)
#     #client.run(os.environ['token'])


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
        role = get(member.guild.roles, name="BOTS")
        await member.add_roles(role)
    elif member.bot == False:
        
        await member.send("Welcome!We hope you have a great day here.")
        channel = client.get_channel(os.environ['MessageChannelID'])
        
       
        await channel.send(f"EveryOne Please welcome {member.mention}. We hope you have a great day here.")
        role = get(member.guild.roles, name="Members")
        await member.add_roles(role)

   
        
    guild =  client.get_guild(os.environ['GuildID']) #get guild or discord server name

    memberchannel = client.get_channel(os.environ['MemberChannelID'])
    botchannel = client.get_channel(os.environ['BotChannelID'])

    membercount = [mem for mem in guild.members if not mem.bot]
    botcount = [mem for mem in guild.members if mem.bot]
    await memberchannel.edit(name = '📈Member count: {}'.format(len(membercount))) #member count
    await botchannel.edit(name = '📈Bot count: {}'.format(len(botcount))) #bot count

        
  
      
    
# @loop(seconds=10)
# async def serverstats(ctx):
    




#client.run(os.environ['token']) #for local

client.run(os.environ['token']) ##for hosting



#     member_count = len(ctx.guild.members) # includes bots
#     true_member_count = len([m for m in ctx.guild.member
#s if not m.bot])
# name = 'Member Count:' + member_count
#     names = 'Member Count no bots:' + true_member_count