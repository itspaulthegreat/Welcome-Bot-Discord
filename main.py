import discord
import asyncio
import sys
import random
import re
import os
from discord.utils import get
import json
from discord.ext import commands
from discord.ext.commands import has_permissions,CheckFailure, BadArgument,has_guild_permissions
from discord.ext.commands import MissingPermissions
from discord.errors import HTTPException

intents = discord.Intents.default()
intents.members = True

# bot = discord.bot(intents=intents)
bot = commands.Bot(command_prefix='~', description="I am DevCord",intents=intents,case_insensitive = True)

with open('config.json') as fh:
    bot.config = json.load(fh)
    #bot.run(bot.config['token'])




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
    await ctx.message.delete()
    print("hi")
    # if ctx.message.channel.guild.me.guild_permissions.administrator:
    # if member.roles.has(809008966167167006):
    #     print("hi")
    role = discord.utils.get(member.guild.roles, name='ChatMuted')
    await member.add_roles(role)
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
    await ctx.message.delete()
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
    await ctx.message.delete()
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
@has_permissions(administrator=True)
async def vunmute(ctx, member: discord.Member):
    await ctx.message.delete()
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


@bot.command(name='kick') #kick voice for users
@has_permissions(kick_members= True)
async def kick(ctx, member: discord.Member,*,arg):
    await ctx.message.delete()
    kickreason = arg
    await member.kick(reason =kickreason )
    embed=discord.Embed(title="User Muted!", description="**{0}** has been kicked by **{1}** because **{2}**!".format(member, ctx.message.author,kickreason), color=0xff00f6)
    await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
    print("hello",error)
    if isinstance(error, MissingPermissions):
        print("hello")
        await ctx.send("**{}** ,You don't have permission to do that!".format(ctx.message.author))

    else:
        await ctx.send("Error Kicking. Please check if you have entered correct arguments or you have right permissions.")



@bot.command(name='move') #kick voice for users
@has_guild_permissions(move_members= True)
async def move(ctx,channel : discord.VoiceChannel):
    await ctx.message.delete()
    # print(channel)
    for members in ctx.author.voice.channel.members:
        await members.move_to(channel)

@move.error
async def move_error(ctx, error):
    print("hello",error)
    if isinstance(error, MissingPermissions):
        print("hello")
        await ctx.send("**{}** ,You don't have permission to do that!".format(ctx.message.author))

    else:
        await ctx.send("Error moving. Please check if you have entered correct arguments or you have right permissions.")






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
    

@bot.command(name='helpticket')    #ticker raise
@has_permissions(administrator= True)
async def gethelpticket(ctx):
    ch = bot.get_channel(809356256112017408)
    if ctx.message.channel.id == 809356256112017408:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name='Moderator')
        embed=discord.Embed(title="Ticket raised ", description="**Hello Users ** \n To generate a new Ticket please use this channel only \n A new ticket can be raised by using  **~ticket reason** command. \n Type your reason after the command . \n As soon as a ticket has been raised a **{}** will resolve the issue. An example is shown below by an admin.".format(role.mention),color=0xff00f6)
        await ctx.send(embed=embed)
    else:
        await ctx.message.delete()
        user = bot.get_user(ctx.author.id)
        embed=discord.Embed(title="Ticket raised ", description="hello **{0}** . please raise your ticket in **{1}**  channel".format(user.mention,ch.mention),color=0xff00f6)
        await ctx.send(embed=embed)















########## RAISING TICKETS MODERATION #####################





@bot.command(name='ticket')    #ticker raise
async def on_message(ctx,*,arg):
    ch = bot.get_channel(809356256112017408)
    if ctx.message.channel.id == 809356256112017408:
        user = bot.get_user(ctx.author.id)
        role = discord.utils.get(ctx.guild.roles, name='Moderator')
        embed=discord.Embed(title="Ticket raised", description="**Hello {0}** A new ticket has been raised by **{1}** . \n **Issue** : **{2}**. \n Thank you.".format(role.mention,user.mention, arg),color=0xff00f6)
        allticket = bot.get_channel(809370568297545759)
        allticketmsg = await allticket.send(embed =embed)
        raisedmsg = await ctx.send(embed=embed)
        newembedallticket=discord.Embed(title="Ticket raised . **ID:{0}**".format(allticketmsg.id), description="**Hello {0}** A new ticket has been raised by **{1}** . \n **Issue** : **{2}**. \n Please type **~tickresol {3}** after resolvin the issue".format(role.mention,user.mention, arg,allticketmsg.id),color=0xff00f6)
        newembedraisedticket=discord.Embed(title="Ticket raised . **ID:{0}**".format(allticketmsg.id), description="**Hello {0}** A new ticket has been raised by **{1}** . \n **Issue** : **{2}**. \n Thank you".format(role.mention,user.mention, arg),color=0xff00f6)
        await allticketmsg.edit(embed = newembedallticket)
        await raisedmsg.edit(embed = newembedraisedticket)
    else:
        await ctx.message.delete()
        user = bot.get_user(ctx.author.id)
        embed=discord.Embed(title="Ticket raised ", description="hello **{0}** . please raise your ticket in **{1}**  channel".format(user.mention,ch.mention),color=0xff00f6)
        await ctx.send(embed=embed)


@bot.command(name='tickresol')    #ticker raise
async def resolve(ctx,msgid):
    ch = bot.get_channel(809370568297545759)
    if ctx.message.channel.id == 809370568297545759:
        await ctx.message.delete()
        channel = bot.get_channel(809370568297545759)
        msg = await channel.fetch_message(msgid)
        await msg.delete()
        user = bot.get_user(ctx.author.id)
        role = discord.utils.get(ctx.guild.roles, name='Moderator')
        newembedallticket=discord.Embed(title="Ticket raised . **ID:{0}**".format(msgid), description="**The Ticket has been Resolved by **{0}** .".format(role.mention),color=0xff00f6)
        resolvedticket = bot.get_channel(809371595051237416)
        await resolvedticket.send(embed =newembedallticket)
    else:
        await ctx.message.delete()
        user = bot.get_user(ctx.author.id)
        embed=discord.Embed(title="Ticket raised ", description="hello **{0}** . please raise your ticket in **{1}**  channel".format(user.mention,ch.mention),color=0xff00f6)
        await ctx.send(embed=embed)






@bot.command(name='tickstatus')    #ticker raise
async def tickstatus(ctx,msgid):
    ch = bot.get_channel(809371578172440607)
    if ctx.message.channel.id == 809371578172440607:
        channel = bot.get_channel(809370568297545759)
        msg = await channel.fetch_message(msgid)
        print(msg)
    else:
        await ctx.message.delete()
        user = bot.get_user(ctx.author.id)
        embed=discord.Embed(title="Ticket raised ", description="hello **{0}** . please raise your ticket in **{1}**  channel".format(user.mention,ch.mention),color=0xff00f6)
        await ctx.send(embed=embed)



@tickstatus.error
async def tickstatus_error(ctx, error):
   print("fuck",error)
   if isinstance(error,HTTPException):
       print("hello")
       #await ctx.send("**{}** ,You don't have permission to do that!".format(ctx.message.author))


################# END ###########################################



# bot.run(bot.config['token']) #for local

bot.run(bot.config['token'])

# bot.run(os.environ['token']) ##for hosting



#     member_count = len(ctx.guild.members) # includes bots
#     true_member_count = len([m for m in ctx.guild.member
#s if not m.bot])
# name = 'Member Count:' + member_count
#     names = 'Member Count no bots:' + true_member_count