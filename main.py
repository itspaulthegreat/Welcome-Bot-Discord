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
bot = commands.Bot(command_prefix='~', description="I am DevCord")

# with open('config.json') as fh:
#     client.config = json.load(fh)
#     #client.run(client.config['token'])

@client.event
async def on_ready():
    activity = discord.Game(name="Hi I am Your Moderator")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Welcome message bot Logged in')
    print(client.user.name)
    print(client.user.id)
    print('-----')

newUserMessage = """your messages"""


@client.event
async def on_member_join(member):
    print("inside onmember in function")
    guild =  client.get_guild(807120796051832862) #get guild or discord server name

    membercount = [mem for mem in guild.members if not mem.bot]
    botcount = [mem for mem in guild.members if mem.bot]
    
    category = client.get_channel(808344068656070666)
    
    for channel in category.voice_channels:
        await channel.delete()
   
    await guild.create_voice_channel(f"📈Member count:{len(membercount)}",overwrites=None,category=category,reason = None)
    await guild.create_voice_channel(f"📊Bot count:{len(botcount)}",overwrites=None,category=category,reason = None)

    if member.bot == True:
        role = get(member.guild.roles, name="BOTS")
        await member.add_roles(role)
       
    elif member.bot == False:
        
        await member.send("Welcome!We hope you have a great day here.")
        channel = client.get_channel(808012829285154886)
        
       
        await channel.send(f"EveryOne Please welcome {member.mention}. We hope you have a great day here.")
        role = get(member.guild.roles, name="Members")
        await member.add_roles(role)
        
        

   
    

@client.event       
async def on_member_remove(member):
    print("inside onmember leave function")
    guild =  client.get_guild(807120796051832862) #get guild or discord server name

    membercount = [mem for mem in guild.members if not mem.bot]
    botcount = [mem for mem in guild.members if mem.bot]

    category = client.get_channel(808344068656070666)

    for channel in category.voice_channels:
        await channel.delete()
    await guild.create_voice_channel(f"📉Member count:{len(membercount)}",overwrites=None,category=category,reason = None)
    await guild.create_voice_channel(f"📊Bot count:{len(botcount)}",overwrites=None,category=category,reason = None)
   
    if member.bot == False:
        
        channel = client.get_channel(808094758244581438)
        
       
        await channel.send(f"Bye Bye {member.mention}. We hope you stay well.")
        
        
  
  
      
    
# @loop(seconds=10)
# async def serverstats(ctx):
    




#client.run(client.config['token']) #for local

client.run(os.environ['token']) ##for hosting



#     member_count = len(ctx.guild.members) # includes bots
#     true_member_count = len([m for m in ctx.guild.member
#s if not m.bot])
# name = 'Member Count:' + member_count
#     names = 'Member Count no bots:' + true_member_count