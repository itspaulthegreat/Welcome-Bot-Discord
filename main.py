import discord
import asyncio
import sys
import random
import re
import os
from discord.utils import get
import json
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions

intents = discord.Intents.default()
intents.members = True

# bot = discord.bot(intents=intents)
bot = commands.Bot(command_prefix='~', description="I am DevCord",intents=intents,case_insensitive = True)

# with open('config.json') as fh:
#     bot.config = json.load(fh)
#     #bot.run(bot.config['token'])




#MODERATION BOT CODE

@bot.event
async def on_ready():
    activity = discord.Game(name="Hi I am Your Moderator")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('Welcome message bot Logged in')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')

newUserMessage = """your messages"""


@bot.command(name='cmute', aliases=['cm'],reason=True)
@has_permissions(manage_messages=True)      # chat mute to users 
async def cmute(ctx, member: discord.Member,*,arg):
    cmreason = arg
    print("hi")
    # if ctx.message.channel.guild.me.guild_permissions.administrator:
    # if member.roles.has(809008966167167006):
    #     print("hi")
    role = discord.utils.get(member.guild.roles, name='ChatMuted')
    await member.remove_roles(role)
    embed=discord.Embed(title="User Muted!", description="**{0}** was chat muted by **{1}** because **{2}**!".format(member, ctx.message.author,cmreason),color=0xff00f6)
    await ctx.send(embed=embed)
    # else:
    #     embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
    #     await ctx.send(embed=embed)

@cmute.error
async def cmute_error(ctx, error):
   print(error)
   if isinstance(error, MissingPermissions):
       print("hello")
       await ctx.send("**{}** ,You don't have permission to do that!".format(ctx.message.author))




@bot.command(name='cunmute', aliases=['cunm']) #unmute chat for users.
@has_permissions(manage_messages=True) 
async def cunmute(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name='ChatMuted')
    await member.remove_roles(role)
    embed=discord.Embed(title="User UnMuted!",description="**{0}** was unmuted from chatting by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
    await ctx.send(embed=embed)

@cunmute.error
async def cunmute_error(ctx, error):
   print(error)
   if isinstance(error, MissingPermissions):
       print("hello")
       await ctx.send("**{}** ,You don't have permission to do that!".format(ctx.message.author))
    


@bot.command(name='vmute', aliases=['vm']) #mute voice for users
@has_permissions(administrator= True)
async def vmute(ctx, member: discord.Member,*,arg):
    vmreason = arg
    role = discord.utils.get(member.guild.roles, name='VoiceMuted')
    await member.add_roles(role)
    embed=discord.Embed(title="User Muted!", description="**{0}** was Voice muted by **{1}** because **{2}**!".format(member, ctx.message.author,vmreason), color=0xff00f6)
    await ctx.send(embed=embed)

@vmute.error
async def vmute_error(ctx, error):
   print(error)
   if isinstance(error, MissingPermissions):
       print(error)
       await ctx.send("**{}** ,You don't have permission to do that!".format(ctx.message.author))




@bot.command(name='vunmute', aliases=['vunm']) #unmute voice for users
@has_permissions(mute_members=True, administrator=True)
async def vunmute(ctx, member: discord.Member):
    print("hi")
    role = discord.utils.get(member.guild.roles, name='VoiceMuted')
    await member.remove_roles(role)
    embed=discord.Embed(title="User UnMuted!", description="**{0}** was unmuted from voice by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
    await ctx.send(embed=embed)

@vunmute.error
async def vunmute_error(ctx, error):
   print(error)
   if isinstance(error, MissingPermissions):
       print("hello")
       await ctx.send("**{}** ,You don't have permission to do that!".format(ctx.message.author))





#END OF MODERATION






#WELCOMER BOT CODE

@bot.event
async def on_member_join(member):
    print("inside onmember in function")
    guild =  bot.get_guild(807120796051832862) #get guild or discord server name

    membercount = [mem for mem in guild.members if not mem.bot]
    botcount = [mem for mem in guild.members if mem.bot]
    
    category = bot.get_channel(808344068656070666)
    
    for channel in category.voice_channels:
        await channel.delete()
   
    await guild.create_voice_channel(f"📈Member count:{len(membercount)}",overwrites=None,category=category,reason = None)
    await guild.create_voice_channel(f"📊Bot count:{len(botcount)}",overwrites=None,category=category,reason = None)

    if member.bot == True:
        role = get(member.guild.roles, name="BOTS")
        await member.add_roles(role)
       
    elif member.bot == False:
        
        await member.send("Welcome!We hope you have a great day here.")
        channel = bot.get_channel(808012829285154886)
        
       
        await channel.send(f"EveryOne Please welcome {member.mention}. We hope you have a great day here.")
        role = get(member.guild.roles, name="Members")
        await member.add_roles(role)
        
        

   
    

@bot.event       
async def on_member_remove(member):
    print("inside onmember leave function")
    guild =  bot.get_guild(807120796051832862) #get guild or discord server name

    membercount = [mem for mem in guild.members if not mem.bot]
    botcount = [mem for mem in guild.members if mem.bot]

    category = bot.get_channel(808344068656070666)

    for channel in category.voice_channels:
        await channel.delete()
    await guild.create_voice_channel(f"📉Member count:{len(membercount)}",overwrites=None,category=category,reason = None)
    await guild.create_voice_channel(f"📊Bot count:{len(botcount)}",overwrites=None,category=category,reason = None)
   
    if member.bot == False:
        
        channel = bot.get_channel(808094758244581438)
        
       
        await channel.send(f"Bye Bye {member.mention}. We hope you stay well.")
        
        
  
  
      
    
# @loop(seconds=10)
# async def serverstats(ctx):
    



# bot.run(bot.config['token']) #for local

# bot.run(bot.config['token'])

bot.run(os.environ['token']) ##for hosting



#     member_count = len(ctx.guild.members) # includes bots
#     true_member_count = len([m for m in ctx.guild.member
#s if not m.bot])
# name = 'Member Count:' + member_count
#     names = 'Member Count no bots:' + true_member_count