import chatot
import SAMData as data
import SAMInfo as info
import random
import datetime
import os
import discord
from os.path import exists
from datetime import datetime

# these get set by the setup() function, which also sets them to be global
list_noun = []
list_verb = []
list_verbing = []
list_adjective = []
list_adverb = []

def grumpQuote():
    random.seed()
    if(exists("text-files/grumps_curated.txt")):
        with open(r"text-files/grumps_curated.txt",'r') as g:
            list_grump = to_list(g)
    else:
        return "Document not found"
    quote = "This text should not appear"
    randy=random.randint(1,len(list_grump)) - 1 # yeah i could change the randint params but fuck off this is my code
    
    # stolen from Vishal at PYnative
    for i, line in enumerate(list_grump):
        if i == randy:
            quote=line
            break
    return quote


def artPrompt(args):
    setting = 0
    try:
        setting = int(args[0])
        if setting <= 1 or setting > 5:
            raise ValueError
    except ValueError:
        return "Invalid input, use \"}help draw\" for more information"
    except IndexError:
        setting = random.randint(2,4)

    random.seed()
    prompt = ""

    if setting == 0:
        return "How did you manage this?"
    elif setting == 2: # 2 words
        rand = random.randint(1,2)
    elif setting == 3: # 3 words
        rand = random.randint(1,4)
    elif setting == 4: # 4 words
        rand = random.randint(1,6)

    if setting == 2:
        if rand == 1: # adjective noun
            randae = rand_PoS(list_adjective)
            randn = rand_PoS(list_noun)
            prompt = "{} {}".format(randae,randn)
        elif rand == 2: # noun verbing
            randn = rand_PoS(list_noun)
            randvg = rand_PoS(list_verbing)
            prompt = "{} {}".format(randn,randvg)
    elif setting == 3:
        if rand == 1: # adjective noun verbing
            randae = rand_PoS(list_adjective)
            randn = rand_PoS(list_noun)
            randvg = rand_PoS(list_verbing)
            prompt = "{} {} {}".format(randae,randn,randvg)
        elif rand == 2: #noun verbing adverb
            randn = rand_PoS(list_noun)
            randvg = rand_PoS(list_verbing)
            randab = rand_PoS(list_adverb)
            prompt = "{} {} {}".format(randn,randvg,randab)
        elif rand == 3: # adjective adjective noun
            randae1 = rand_PoS(list_adjective)
            randae2 = rand_PoS(list_adjective)
            randn = rand_PoS(list_noun)
            prompt = "{} {} {}".format(randae1,randae2,randn)
        elif rand == 4: # noun verbing noun
            randn1 = rand_PoS(list_noun)
            randvg = rand_PoS(list_verbing)
            randn2 = rand_PoS(list_noun)
            prompt = "{} {} {}".format(randn1,randvg,randn2)
    elif setting == 4:
        prompt = "Work in progress, these may not be as coherent\n"
        if rand == 1: # adjective adjective noun verbing
            randae1 = rand_PoS(list_adjective)
            randae2 = rand_PoS(list_adjective)
            randn = rand_PoS(list_noun)
            randvg = rand_PoS(list_verb)
            prompt += "{} {} {} {}".format(randae1,randae2,randn,randvg)
        elif rand == 2: # adjective noun verbing adverb
            randae = rand_PoS(list_adjective)
            randn = rand_PoS(list_noun)
            randvg = rand_PoS(list_verbing)
            randab = rand_PoS(list_adverb)
            prompt += "{} {} {} {}".format(randae,randn,randvg,randab)
        elif rand == 3: # adjective adjective adjective noun
            randae1 = rand_PoS(list_adjective)
            randae2 = rand_PoS(list_adjective)
            randae3 = rand_PoS(list_adjective)
            randn = rand_PoS(list_noun)
            prompt += "{} {} {} {}".format(randae1,randae2,randae3,randn)
        elif rand == 4: # adjective noun verbing noun
            randae = rand_PoS(list_adjective)
            randn1 = rand_PoS(list_noun)
            randvg = rand_PoS(list_verbing)
            randn2 = rand_PoS(list_noun)
            prompt += "{} {} {} {}".format(randae,randn1,randvg,randn2)
        elif rand == 5: # noun verbing adjective noun
            randn1 = rand_PoS(list_noun)
            randvg = rand_PoS(list_verbing)
            randae = rand_PoS(list_adjective)
            randn2 = rand_PoS(list_noun)
            prompt += "{} {} {} {}".format(randn1,randvg,randae,randn2)
        elif rand == 6: # noun verbing noun adverb
            randn1 = rand_PoS(list_noun)
            randvg = rand_PoS(list_verbing)
            randn2 = rand_PoS(list_noun)
            randab = rand_PoS(list_adverb)
            prompt += "{} {} {} {}".format(randn1,randvg,randn2,randab)
    else:
        prompt = "Work in progress, please be patient"
    return prompt

def rand_PoS(PoS):
    return PoS[random.randint(1,len(PoS))-1].strip()

def schoolNight():
    DOTW = datetime.today().weekday()
    dir_path = ""
    count = 0
    img = r"images/shiro_sad.png"
    
    if(DOTW < 4 or DOTW == 6):
        dir_path = r"images/school-night"
    elif DOTW == 4:
        dir_path = r"images/friday"
    else:
        dir_path = r"images/not-school-night"
    
    # stolen, forgot who from
    for path in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1

    rando = random.randint(1,count)
    i = 1
    for path in os.listdir(dir_path):
        if i == rando:
            img = os.path.join(dir_path,path)
            break
        i += 1
    return discord.File(img)


def condescend(ctx):
    random.seed()
    condescend = "N is a terrible programmer"
    usr = str(ctx.author)
    
    if usr == "NickIcarus#4082" and random.randint(1,10) == 1:
        return "Hey Nicki, I'm not trying to kink shame you, but I think you're developing an unhealthy relationship with my sass protocol"
    elif usr == "Dr. N#9753":
        return "Were you testing to see if this worked or did you actually mess up typing a command?"
    elif usr == "seriousSleuth#0248":
        return "I could never be mean to you, Maddy"
    else:
        if(exists("text-files/condescending_phrases_curated.txt")):
            with open(r"text-files/condescending_phrases_curated.txt",'r') as cond:
                list_condescend = to_list(cond)
        else:
            return condescend

        randy=random.randint(1,len(list_condescend)) - 1 # yeah i could change the randint params but fuck off this is my code
        
        # stolen from Vishal at PYnative
        for i, line in enumerate(list_condescend):
            if i == randy:
                condescend=line
                break
        return condescend


def rollBones(args):
    acceptable=[2,4,6,8,10,12,20,100]

    try:
        die=int(args[0])
        if die not in acceptable:
            raise ValueError
    except ValueError:
        return "Invalid input, use \"}help roll\" for more info"
    except IndexError:
        return "Don't forget to specify the number of sides for the die"

    try:
        iterations = int(args[1])
    except (ValueError,IndexError):
        iterations = 1
    if iterations < 1:
        return "The only thing that're being rolled are my digital eyes"
    elif iterations > 20:
        return ("Why do you need to roll {} dice?".format(iterations))
    rolls = []
    for i in range(iterations):
        rolls.append(random.randint(1,die))
    return ("You rolled {}".format(rolls))


def ourQuotes():
    random.seed()
    
    if(exists("text-files/genius_quotes_curated.txt")):
        with open(r"text-files/genius_quotes_curated.txt",'r') as quotes:
            list_quote = to_list(quotes)
    else:
        return "\"Document not found\" - SAManTHBot"
    dumb = "\"This message should not appear\" - SAManTHBot"
    
    randy=random.randint(1,len(list_quote)) - 1 # yeah i could change the randint params but fuck off this is my code
    
    # stolen from Vishal at PYnative
    for i, line in enumerate(list_quote):
        if i == randy:
            dumb=line
            break
    return dumb

def to_list(doc):
    lost = []
    for line in enumerate(doc):
        lost.append(line)
    return lost

def eventLogger(event, eventType): # event is only used in special cases, otherwise you can pass anything it doesn't matter
    if exists("SAManTHBot-docs/"):
        with open("SAManTHBot-docs/log.txt",'a') as f:
            if eventType == 0: # error encountered
                f.write("{} - I've encountered an issue, context: {}\n".format(str(datetime.utcnow()),event))
                print("Shutting down")
            elif eventType == 1: # lost connection
                f.write("{} - I've lost connection\n".format(str(datetime.utcnow())))
            elif eventType == 2: # resumed connection
                f.write("{} - I've resumed normal operation\n".format(str(datetime.utcnow())))
            elif eventType == 3: # logged in for the first time
                f.write("{} - I've logged in\n".format(str(datetime.utcnow())))
            elif eventType == 4: # doing setup
                f.write("{} - Beggining setup procedure\n".format(str(datetime.utcnow())))
            elif eventType == 5: # logging out
                f.write("{} - Logging out\n".format(str(datetime.utcnow())))
    else:
        with open("ERROR.txt",'w') as bad:
            bad.write("Directory SAManTHBot-docs does not exist")

def setup(first):
    eventLogger("null",4)
    random.seed()
    if(exists("text-files/nouns_curated.txt")) and exists("text-files/verbs_curated.txt") and exists("text-files/verbs-ing_curated.txt") and exists("text-files/adjectives_curated.txt") and exists("text-files/adverbs_curated.txt"):
        # making the varibles global as a ""temporary"" fix until i find a better way
        global list_noun, list_verb, list_verbing, list_adjective, list_adverb
        with open(r"text-files/nouns_curated.txt",'r') as doc_noun:
            list_noun = to_list(doc_noun)
        with open(r"text-files/verbs_curated.txt",'r') as doc_verb:
            list_verb = to_list(doc_verb)
        with open(r"text-files/verbs-ing_curated.txt",'r') as doc_verbing:
            list_verbing = to_list(doc_verbing)
        with open(r"text-files/adjectives_curated.txt",'r') as doc_adjective:
            list_adjective = to_list(doc_adjective)
        with open(r"text-files/adverbs_curated.txt",'r') as doc_adverb:
            list_adverb = to_list(doc_adverb)
    else:
        eventLogger("Missing POS files",0)
        return False
    
    if first:
        eventLogger("null",3)
    else:
        eventLogger("null",2)
    return True