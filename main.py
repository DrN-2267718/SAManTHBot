#============================================================#
#                     SAManTHBot v0.1                        #
#                     "made" by Dr. N                        #
# code stolen from various sources i will list below         #
# rule of thumb: if it works well and looks nice, it wasn't  #
# made by me                                                 #
#============================================================#
#  sources for the code i stole is usually above said code   #
#                                                            #
#                 unless i forget haha oops                  #
#============================================================#

import discord
import logging
import random
import chatot
import codeBits
import os
from discord.ext import commands
from discord.errors import Forbidden

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('SAManTHBot.main')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='SAManTHBot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix="}",case_insensitive=True)

random.seed()


# stolen from Jared Newsom
async def send_embed(ctx, embed):
    """
    Function that handles the sending of embeds
    -> Takes context and embed to send
    - tries to send embed in channel
    - tries to send normal message when that fails
    - tries to send embed private with information abot missing permissions
    If this all fails: https://youtu.be/dQw4w9WgXcQ
    """
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


@bot.event
async def on_message(message):
    # so the bot doesn't talk to itself
    if message.author == bot.user:
        return
    else:
        mess = str(message.clean_content)
        # quick and dirty way to make the bot pingable
        bot_user = "@" + str(bot.user).replace("#6434","",1)

    if message.mention_everyone:
        await message.reply(":rage:")

    # check for people talking to the bot
    elif mess.startswith(bot_user):
        await chatot.reply(message,mess)
        
    else:
        await bot.process_commands(message)
            
# the long list of commmands

@bot.command(
    hidden=True,
    help="how the fuck did you find this?",
    brief="This text should not appear")
async def test(ctx, *arg):
    await ctx.channel.send(arg)

@bot.command(
    help="this does something, unless i didn't actually put anything in which case it just says Trash",
    brief="I only say the truth")
async def anime(ctx):
    await ctx.channel.send("Trash")

@bot.command(
    help="CONGRULATIONS YOU ARE THE 100th VISITOR!!! CLICK HERE TO [Die]",
    brief="TELL ME MORE")
async def bigShot(ctx):
    await ctx.channel.send("Kromer")

@bot.command(
    help="SAManTHBot stores your ip address, bank account information, social security number, and phone number every time you use this command",
    brief="Prints pong")
async def ping(ctx):
    await ctx.channel.send("pong")

@bot.command(
    help="you tryna hold hands with my bot you son of a bitch?! i'll kill you!!",
    brief="Don't even think about it, hentai!")
async def holdhands(ctx):
    await ctx.send("We can't do that we're not married!")

@bot.command(
    help="excuse me, fuck off",
    brief="No")
async def marry(ctx):
    await ctx.send("I'm a bot we can't get married")

@bot.command(
    help="BONK",
    brief="BONK")
async def lewd(ctx):
    await ctx.send("Do not fist android girls")

@bot.command(
    help="be careful what you wish for",
    brief="Talk to me")
async def talk(ctx):
    await chatot.conversation(ctx)

@bot.command(
    help="why do people watch this? don't watch this! UNSUBSCRIBE!!!",
    brief="Liquid Game Grumps! In Text Form!")
async def grump(ctx):
    await ctx.send(codeBits.grumpQuote())

@bot.command(
    help='''Generates a drawing prompt, can be told how many words are in the propmt, defaults to 2.
    2 = adjective noun or noun verb
    3 = adjective noun verb or noun verb adverb or adjective adjective noun
    Working on allowing more customization''',
    brief="Generates a drawing prompt")
async def draw(ctx,*args):
    await ctx.send(codeBits.artPrompt(args))

@bot.command(
    help="the beginnings of the true meme machine",
    brief="Check whether it's a school night")
async def school(ctx):
    await ctx.send(file=codeBits.schoolNight())

@bot.command(
    hidden=True,
    help="she's too powerful",
    brief="Just try me")
async def logout(ctx):
    print("Logging out")
    await bot.change_presence(status=discord.Status.offline)
    await bot.logout()

@bot.command(
    help="Format: }roll <die_sides> <#_of_rolls>\n die_sides must be one of these: 2, 4, 6, 8, 10, 12, 20, 100\n #_of_roles must be > 0 and 10 max",
    brief="Roll a die or multiple dice")
async def roll(ctx,*args):
    await ctx.send(codeBits.rollBones(args))

@bot.command(
    help="goddess we're stupid",
    brief="Get a random stupid quote"
)
async def quote(ctx):
    await ctx.send(codeBits.ourQuotes())


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send(codeBits.condescend(ctx))
    else:
        raise error

@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))
    random.seed()
    activity = discord.Activity(name='over the lab', type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity)

'''
 template
 @bot.command(
     help="",
     brief="",
 )
 async def functionName(ctx):
     await ctx.send("")
'''

bot.run('OTYzNTU3MTE4ODE5MDY5OTUy.YlX0fw.duqH5C4dY0XH2Btgc6PcY9tjOZk') # haha oops good thing discord already reset it
