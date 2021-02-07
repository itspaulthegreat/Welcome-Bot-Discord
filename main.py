import discord
import asyncio
import sys
import random
import re
import os
from discord.utils import get
import json

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
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
        channel = client.get_channel(808012829285154886)
        # await channel.edit(name = 'Member count: {}'.format(channel.guild.member_count()))
        await channel.send(f"EveryOne Please welcome {member.mention}. We hope you have a great day here.")
        role = get(member.guild.roles, name="Members")
        await member.add_roles(role)
    

with open('config.json') as fh:
    client.config = json.load(fh)
    #client.run(client.config['token'])

client.run(client.config['token']) #for local


#client.run(os.environ['token']) ##for hosting



#     member_count = len(ctx.guild.members) # includes bots
#     true_member_count = len([m for m in ctx.guild.member
#s if not m.bot])
# name = 'Member Count:' + member_count
#     names = 'Member Count no bots:' + true_member_count