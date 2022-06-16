import chatot
import SAMData as data
import SAMDataMod as mod
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
    
    if(exists("text-files/grumps.txt")):
        grumpDoc=open(r"text-files/grumps.txt",'r')
    else:
        return "Document not found"
    grumpLine = 0
    quote = "This text should not appear"
    
    for line in enumerate(grumpDoc):
        grumpLine += 1
    
    randy=random.randint(1,grumpLine) - 1 # yeah i could change the randint params but fuck off this is my code
    grumpDoc.seek(0)
    
    # stolen from Vishal at PYnative
    for i, line in enumerate(grumpDoc):
        if i == randy:
            quote=line.strip()
            break
    grumpDoc.close()
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
        setting = random.randint(2,3)

    random.seed()
    prompt = ""

    if setting == 0:
        return "How did you manage this?"
    elif setting == 2: # 2 words
        rand1 = random.randint(1,2)
    elif setting == 3: # 3 words
        rand2 = random.randint(1,3)

    if setting == 2 and rand1 == 1: # adjective noun
        randae = rand_PoS(list_adjective)
        randn = rand_PoS(list_noun)
        prompt = "{} {}".format(randae, randn)
    elif setting == 2 and rand1 == 2: # noun verbing
        randn = rand_PoS(list_noun)
        randv = rand_PoS(list_verbing)
        prompt = "{} {}".format(randn,randv)
    elif setting == 3 and rand2 == 1: # adjective noun verbing
        randae = rand_PoS(list_adjective)
        randn = rand_PoS(list_noun)
        randv = rand_PoS(list_verbing)
        prompt = "{} {} {}".format(randae,randn,randv)
    elif setting == 3 and rand2 == 2: #noun verbing adverb
        randn = rand_PoS(list_noun)
        randv = rand_PoS(list_verbing)
        randab = rand_PoS(list_adverb)
        prompt = "{} {} {}".format(randn,randv,randab)
    elif setting == 3 and rand2 == 3: # adjective adjective noun
        randae1 = rand_PoS(list_adjective)
        randae2 = rand_PoS(list_adjective)
        randn = rand_PoS(list_noun)
        prompt = "{} {} {}".format(randae1,randae2,randn)
    else:
        prompt = "Work in progress, please be patient"
    return prompt

def rand_PoS(PoS):
    return PoS[random.randint(1,len(PoS))-1].strip()

def schoolNight():
    DOTW = datetime.today().weekday()
    dayName = datetime.today().strftime('%A')
    dir_path = r'images/'
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

    print(ctx.author)
    
    if str(ctx.author) == "NickIcarus" and random.randint(1,10) == 1:
        return "Hey Nicki, I'm not trying to kink shame you, but I think you're developing an unhealthy relationship with my sass protocol"

    if(exists("text-files/condescending_phrases.txt")):
        condescend_list=open(r"text-files/condescending_phrases.txt",'r')
    else:
        return condescend
    lines = 0
    
    for line in enumerate(condescend_list):
        lines += 1
    
    randy=random.randint(1,lines) - 1 # yeah i could change the randint params but fuck off this is my code
    condescend_list.seek(0)
    
    # stolen from Vishal at PYnative
    for i, line in enumerate(condescend_list):
        if i == randy:
            condescend=line.strip()
            break
    condescend_list.close()
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
    
    if(exists("text-files/genius_quotes.txt")):
        quote_list=open(r"text-files/genius_quotes.txt",'r')
    else:
        return "\"Document not found\" - SAManTHBot"
    lines = 0
    dumb = "\"This message should not appear\" - SAManTHBot"
    
    for line in enumerate(quote_list):
        lines += 1
    
    randy=random.randint(1,lines) - 1 # yeah i could change the randint params but fuck off this is my code
    quote_list.seek(0)
    
    # stolen from Vishal at PYnative
    for i, line in enumerate(quote_list):
        if i == randy:
            dumb=line.strip()
            break
    quote_list.close()
    return dumb

def to_list(doc):
    lost = []
    for i, line in enumerate(doc):
        lost.append(line)
    return lost

def eventLogger(event, eventType): # event is only used in special cases, otherwise you can pass anything it doesn't matter
    if exists("SAManTHBot-docs/log.txt"):
        try:
            f = open("SAManTHBot-docs/log.txt",'a')
        except FileNotFoundError:
            f = open("ERROR.txt",'w')
            f.write("Directory SAManTHBot-docs does not exist")
            f.close()
            return
    else:
        f = open("SAManTHBot-docs/log.txt",'w')
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
    f.close()

def setup(first):
    eventLogger("null",4)
    random.seed()
    if(exists("text-files/nouns.txt")) and exists("text-files/verbs.txt") and exists("text-files/verbs-ing.txt") and exists("text-files/adjectives.txt") and exists("text-files/adverbs.txt"):
        doc_noun=open(r"text-files/nouns.txt",'r')
        doc_verb=open(r"text-files/verbs.txt",'r')
        doc_verbing=open(r"text-files/verbs-ing.txt",'r')
        doc_adjective=open(r"text-files/adjectives.txt",'r')
        doc_adverb=open(r"text-files/adverbs.txt",'r')
    else:
        eventLogger("Missing POS files",0)
        return False

    # making the varibles global as a ""temporary"" fix until i find a better way
    global list_noun, list_verb, list_verbing, list_adjective, list_adverb
    list_noun = to_list(doc_noun)
    list_verb = to_list(doc_verb)
    list_verbing = to_list(doc_verbing)
    list_adjective = to_list(doc_adjective)
    list_adverb = to_list(doc_adverb)

    doc_noun.close()
    doc_verb.close()
    doc_verbing.close()
    doc_adjective.close()
    doc_adverb.close()
    
    if first:
        eventLogger("null",3)
    else:
        eventLogger("null",2)
    return True