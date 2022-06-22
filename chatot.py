import codeBits
import SAMData as data
import SAMInfo as info
import discord

async def reply(message, mess, SAM):
    author_id = str(message.author.id)
    author_user = str(message.author.display_name)
    if author_user == "Dr. N":
        author_user = "Doctor"

    if "Thank you" in mess or "thank you" in mess or "Thankies" in mess or "thankies" in mess:
        await message.channel.send("You're welcome {}".format(author_user))
    elif "Thank" in mess or "thank" in mess:
        await message.channel.send("Welc")
    elif "Good bot" in mess or "Good Bot" in mess or "good bot" in mess:
        await message.channel.send("UwU")
    elif "What are your pronouns?" in mess or "what are your pronouns?" in mess:
        await message.channel.send(SAM.pronouns)
    elif "What are your specs?" in mess or "what are your specs?" in mess:
        await message.channel.send(SAM.specs)
    else:
        await message.reply("https://www.youtube.com/watch?v=4LVgGcYjXqM")

async def conversation(ctx, SAM):
    await ctx.send("one day i'll make this a thing")
# chat bot stuff
