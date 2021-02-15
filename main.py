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



@bot.command(name="clear")  #clearing
async def clear(ctx,arg):
    await ctx.channel.purge(limit=int(arg))



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
        
        
        
        channel = bot.get_channel(808012829285154886)
        m= member.id
        c = member.avatar
        avatar = str(member.avatar_url).split('?')
        pfp = avatar[0] + "?size=1024"
        rolech = bot.get_channel(809339141791809568)
        ticketch = bot.get_channel(809356256112017408)
        rulech = bot.get_channel(807121650389876776)
        print("pfp",pfp)
        embed=discord.Embed(title="WELCOME To DevCord", description="Hello! **{0}** \n\n **Please get your roles from** **{1}**.\n **And if you have issues raise a ticket by using ~ticket yourreason in** **{2}**. \n\n Read the rulebook an react to it {3}".format(member.mention,rolech.mention,ticketch.mention,rulech.mention) , color=0xecce8b)
        embed.set_thumbnail(url=(pfp))
        embed.set_footer(text="Please follow our rules as mentioned in the rulebook.Breaking of any  guidlines can result in against the defaulter.")

        await channel.send(embed=embed)
        role = get(member.guild.roles, name="Members")
        await member.add_roles(role)
        await member.send(embed=embed)
        

   
    

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
    

@bot.command(name='helpme')    #helps
async def gethelp(ctx):
    flag =0
    async for kk in ctx.guild.fetch_members(limit=None):
            if ctx.message.author.id == kk.id:
                print(kk.roles[-1])
                if str(kk.roles[-1]) == "Moderator" or str(kk.roles[-1]) == "Administrator":
                    flag = 1
    # if "Administrator" == str(ctx.message.author.roles[-1]) or "Moderator" == str(ctx.message.author.roles[-1]):
    #     print("done")
    guild = bot.get_guild(807120796051832862)
    await ctx.message.delete()
    info_channel = ['💬-discussion', '🏆-project-showcase', '📚-resources','❔-questions']
    normal_text = ['🔇💬no-mic','👨🔬introductions','🗑spam-here','💬off-topic-discussion']
    for ch in info_channel:
        if str(discord.utils.get(guild.text_channels, name=ch)) == str(ctx.message.channel.name):
            embed=discord.Embed(title="Specialization Corner", description="This is Specialization Corner. Use it for the the specific specilization",color=0xff00f6)
            mes = await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await mes.delete()
            return
        
    for ch in normal_text:
        discord.utils.get(guild.text_channels, name=ch)
        if str(discord.utils.get(guild.text_channels, name=ch)) == str(ctx.message.channel.name):
            embed=discord.Embed(title="Normal Text Channel", description="This a normal text channel \n Type Whatever you want. \n No NSFW though !!!",color=0xff00f6)
            mes = await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await mes.delete()
            return
    

    
    if ctx.message.channel.id == 809371578172440607:  #raise ticket channel
        
        embed=discord.Embed(title="Ticket status Help", description="**Hello Users ** \n To know the status of your Ticket please use this channel only \n  Ticket status can be seen by using  **~tickstatus ticketnumber** command. \n Type your ticket number after the command .",color=0xff00f6)
        mes = await ctx.send(embed=embed)
        if flag == 0:
                await asyncio.sleep(5)
                await mes.delete()

    elif ctx.message.channel.id == 809356256112017408:   #ticket status channel
            role = discord.utils.get(ctx.guild.roles, name='Moderator')
            embed=discord.Embed(title="Ticket raising Help", description="**Hello Users ** \n To generate a new Ticket please use this channel only \n A new ticket can be raised by using  **~ticket reason** command. \n Type your reason after the command . \n As soon as a ticket has been raised a **{}** will resolve the issue. An example is shown below by an admin.".format(role.mention),color=0xff00f6)
            mes = await ctx.send(embed=embed)
            if flag == 0:
                await asyncio.sleep(5)
                await mes.delete()
    
    elif ctx.message.channel.id == 809339141791809568:   #role channel
            role = discord.utils.get(ctx.guild.roles, name='Moderator')
            embed=discord.Embed(title="How to get Roles", description="**Hello Users ** \n To get Role use this channel \n Use the following command **>gr** to get the roles. \n **A embed will come up . Type 1 or 2 or the respect number for the respected role**  \n\n. Incase of help ask **{}**  . They will resolve the issue.".format(role.mention),color=0xff00f6)
            mes = await ctx.send(embed=embed)
            if flag == 0:
                await asyncio.sleep(5)
                await mes.delete()

    elif ctx.message.channel.id == 807121650389876776:   #Rulebook
            
            desc = '''General Server Rules :white_check_mark: 
                    \n Violation of the Rules, may result in getting banned or kicked.
                    \n1. Be good to each other, don't keep any intention to hurt others.
                    \n2. Don't be Toxic
                    \n3. Respect all members.
                    \n4. In case of conflict Admin's decision in final.
                    \n5. Don't Promote or Advertise in our Server. No Server Promotion.
                    \n6. No DM Promotion. 
                    \n7. No Doxing. 

                    \n\nChat Rules :white_check_mark: 
                    \n1. No Religious or Racist Comments.
                    \n2. Don't use extreme Slangs.
                    \n3. No NSFW content in non-NSFW Channel.
                    \n4. No Spamming.
                    \n5. Post appropriate content in appropriate channels.
                    \n6. No Nudity or Pornography.

                    \n\nVoice Channel Rules :white_check_mark:
                    \n1. You must utilize the Voice Channels (VC) for the right purpose of their creation.
                    \n2. You must not call the @music-bots in the Gaming or Non-music VCs to disturb others. However you can listen to music in a non-music channel if others in the VC agree.
                    \n3. You must not use verbal abuse against anyone. Or hurt anyone's sentiments. 
                    \n4. Don't Occupy a VC if you are not talking.
                    '''
            print(flag)

            embed=discord.Embed(title="DevCord Rulebook", description=desc,color=0xff00f6)
            mes = await ctx.send(embed=embed)
            if flag == 0:
                await asyncio.sleep(5)
                await mes.delete()



    else:
        print("hi")
        embed=discord.Embed(title="Wrong channel ", description="hello {} no help available for this channel".format(ctx.message.author.mention),color=0xff00f6)
        mes = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await mes.delete()















########## RAISING TICKETS MODERATION #####################





@bot.command(name='ticket')    #ticker raise
async def on_messae(ctx,*,arg):
    await ctx.message.delete()
    ch = bot.get_channel(809356256112017408)
    if ctx.message.channel.id == 809356256112017408:
        user = bot.get_user(ctx.author.id)
        role = discord.utils.get(ctx.guild.roles, name='Moderator')
        embed=discord.Embed(title="Ticket raised", description="**Hello {0}** A new ticket has been raised by **{1}** . \n **Issue** : **{2}**. \n Thank you.".format(role.mention,user.mention, arg),color=0xff00f6)
        allticket = bot.get_channel(809370568297545759)
        allticketmsg = await allticket.send(embed =embed)
        raisedmsg = await ctx.send(embed=embed)
        newembedallticket=discord.Embed(title="Ticket raised . **ID:{0}**".format(allticketmsg.id), description="**Hello {0}** A new ticket has been raised by **{1}** . \n **Issue** : **{2}**. \n Please type **~tickresol {3}** after resolvin the issue".format(role.mention,user.mention, arg,allticketmsg.id),color=0xfae593)
        newembedraisedticket=discord.Embed(title="Ticket raised . **ID:{0}**".format(allticketmsg.id), description="**Hello {0}** A new ticket has been raised by **{1}** . \n **Issue** : **{2}**. \n Thank you".format(role.mention,user.mention, arg),color=0xaadff1)
        await allticketmsg.edit(embed = newembedallticket)
        await raisedmsg.edit(embed = newembedraisedticket)
    else:
        await ctx.message.delete()
        user = bot.get_user(ctx.author.id)
        embed=discord.Embed(title="Ticket not raised ", description="hello **{0}** . please raise your ticket in **{1}**  channel".format(user.mention,ch.mention),color=0xff00f6)
        await ctx.send(embed=embed)


@bot.command(name='tickresol')    #ticker raise
@has_permissions(kick_members=True,ban_members = True)
async def resolve(ctx,msgid):
    ch = bot.get_channel(809370568297545759)
    if ctx.message.channel.id == 809370568297545759:
        await ctx.message.delete()
        channel = bot.get_channel(809370568297545759)
        msg = await channel.fetch_message(msgid)
        await msg.delete()
        user = bot.get_user(ctx.author.id)
        role = discord.utils.get(ctx.guild.roles, name='Moderator')
        newembedallticket=discord.Embed(title="Ticket raised . **ID:{0}**".format(msgid), description="**The Ticket has been Resolved by **{0}** .".format(role.mention),color=0xaaf1b9)
        resolvedticket = bot.get_channel(809371595051237416)
        await resolvedticket.send(embed =newembedallticket)
    else:
        await ctx.message.delete()
        user = bot.get_user(ctx.author.id)
        embed=discord.Embed(title="Ticket not raised ", description="hello **{0}** . please raise your ticket in **{1}**  channel".format(user.mention,ch.mention),color=0xff00f6)
        await ctx.send(embed=embed)


@resolve.error
async def resolve_error(ctx,error):
    await ctx.message.delete()
    print("fuck",type(error))
    if isinstance(error,MissingPermissions):
        await ctx.send("**{}** ,You don't have permission!".format(ctx.message.author))









@bot.command(name='tickstatus')    #ticker raise
async def tickstatus(ctx,msgid):
    await ctx.message.delete()
    ch = bot.get_channel(809371578172440607)
    if ctx.message.channel.id == 809371578172440607:

        outputchannel = bot.get_channel(809371578172440607) #ticket status channel

        msgid = int(msgid)
        user = bot.get_user(ctx.author.id)
        
        inprogress = discord.Embed(title="Ticket is in progress. **ID:{0}**".format(msgid), description="Hello **{0}** \n **The Ticket is in progress** .".format(user.mention),color=0xfae593)
        done = discord.Embed(title="Ticket has been resolved . **ID:{0}**".format(msgid), description="Hello **{0}** \n **The Ticket has been Resolved**.".format(user.mention),color=0xaaf1b9)
        notfound = discord.Embed(title="Ticket Not Found", description="Hello **{0}** \n **The Ticket is not present** . \n **Please check the ID you entered.**.".format(user.mention),color=0xab2339)
        
        
        channel = bot.get_channel(809370568297545759)  #allticket channel
        messages = await channel.history(limit=200).flatten()
        print("hi there",messages)
        if messages !=[]:
            list1 = []
            for msg in messages:
                for e in msg.embeds:
                    listid = e.title.split(':')
                    ticketid = listid[1].split('*')
                    list1.append(int(ticketid[0]))
                    print("list1",list1)
            if msgid in list1:
                print("hi")
                await outputchannel.send(embed =inprogress)
                return
        
            elif msgid not in list1:
                print("hi there 2")
                channel1 = bot.get_channel(809371595051237416)   #done channel
                messages1 = await channel1.history(limit=200).flatten()
                if messages1 != []:
                    list2 = []
                    for msg in messages1:
                        for e in msg.embeds:
                            listid1 = e.title.split(':')
                            ticketid1 = listid1[1].split('*')
                            
                            list2.append(int(ticketid1[0]))
                            print("list2",list2)
                    if msgid in list2:
                        await outputchannel.send(embed =done)
                        return

                    elif msgid not in list2:
                        await outputchannel.send(embed =notfound)
                        return

                elif messages1 == []:
                    await outputchannel.send(embed =notfound)


        elif messages == []:       
            channel1 = bot.get_channel(809371595051237416)
            messages1 = await channel1.history(limit=200).flatten()
            if messages1 != []:
                list3 = []
                for msg in messages1:
                    for e in msg.embeds:
                        listid1 = e.title.split(':')
                        ticketid1 = listid1[1].split('*')
                        list3.append(int(ticketid1[0]))
                        print("list3",list3)
                if msgid in list3:
                    await outputchannel.send(embed =done)
                    return

                elif msgid not in list3:
                    await outputchannel.send(embed =notfound)
                    return
            
            elif messages1 ==[]:
                await outputchannel.send(embed =notfound)

    
    else:
        await ctx.message.delete()
        user = bot.get_user(ctx.author.id)
        embed=discord.Embed(title="Ticket not raised ", description="hello **{0}** . please raise your ticket in **{1}**  channel".format(user.mention,ch.mention),color=0xff00f6)
        await ctx.send(embed=embed)



@tickstatus.error
async def tickstatus_error(ctx,error):
    await ctx.message.delete()
    print("fuck",error)
    if str(type(error))== "<class 'discord.ext.commands.errors.CommandInvokeError'>":
        await ctx.send("**{}** ,You have entered invalid Ticket ID!".format(ctx.message.author))


    


################# END ###########################################








########################## channel creation #####################



@bot.command(name="creatch")
@has_permissions(administrator=True)
async def createch(ctx,*,arg):
    if ctx.message.channel.id == 807120796051832865:
        guild = bot.get_guild(807120796051832862)
        catid = await guild.create_category(arg)

        await guild.create_text_channel("📃-info",overwrites=None,category=catid,reason = None)
        await guild.create_text_channel("💬-discussion",overwrites=None,category=catid,reason = None)
        await guild.create_text_channel("🏆-project-showcase",overwrites=None,category=catid,reason = None)
        await guild.create_text_channel("📚-resources",overwrites=None,category=catid,reason = None)
        await guild.create_text_channel("❔-questions",overwrites=None,category=catid,reason = None)
        await guild.create_voice_channel("📞-voice",overwrites=None,category=catid,reason = None)
 
    else:
        await ctx.message.delete()



########################## the end #################################






####################add reaction to messages by admin############################

@bot.event
async def on_message(msg):
    flag = 0
    guild = bot.get_guild(807120796051832862)
    async for kk in msg.guild.fetch_members(limit=None):
            if msg.author.id == kk.id:
                print(kk.roles[-1])
                if str(kk.roles[-1]) == "Moderator" or str(kk.roles[-1]) == "Administrator" or str(kk.roles[-1]) == "DevCord (ModBot)":
                    emoji = '💕'
                    emoji2 = '🤟'
                    emoji3 = '😍'
                    await msg.add_reaction(emoji)
                    await msg.add_reaction(emoji2)
                    await msg.add_reaction(emoji3)
    await bot.process_commands(msg)
















# bot.run(bot.config['token']) #for local

# bot.run(bot.config['token'])

bot.run(os.environ['token']) ##for hosting



#     member_count = len(ctx.guild.members) # includes bots
#     true_member_count = len([m for m in ctx.guild.member
#s if not m.bot])
# name = 'Member Count:' + member_count
#     names = 'Member Count no bots:' + true_member_count