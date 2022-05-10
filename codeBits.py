import random
import datetime
import os
import discord
from os.path import exists
from datetime import datetime


def grumpQuote():
    random.seed()
    
    if(exists("text_files/grumps.txt")):
        grumpDoc=open(r"text_files/grumps.txt",'r')
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
        if setting <= 1:
            raise ValueError
    except ValueError:
        return "Invalid input, use \"}help draw\" for more information"
    except IndexError:
        setting = 2

    random.seed()

    if(exists("text_files/nouns.txt")) and exists("text_files/verbs.txt") and exists("text_files/verbs-ing.txt") and exists("text_files/adjectives.txt") and exists("text_files/adverbs.txt"):
        doc_noun=open(r"text_files/nouns.txt",'r')
        doc_verb=open(r"text_files/verbs.txt",'r')
        doc_verbing=open(r"text_files/verbs-ing.txt",'r')
        doc_adjective=open(r"text_files/adjectives.txt",'r')
        doc_adverb=open(r"text_files/adverbs.txt",'r')
    else:
        return "Missing necessary files, please yell at N for me"

    noun = []
    verb = []
    verbing = []
    adjective = []
    adverb = []
    prompt = ""

    if setting == 0:
        return "How did you manage this?"
    elif setting == 2: # 2 words
        rand1 = random.randint(1,2)
    elif setting == 3: # 3 words
        rand2 = random.randint(1,3)

    if setting == 2 and rand1 == 1: # adjective noun
        adjective = to_list(adjective,doc_adjective)
        noun = to_list(noun,doc_noun)
        randae = rand_PoS(adjective)
        randn = rand_PoS(noun)
        prompt = "{} {}".format(randae, randn)
    elif setting == 2 and rand1 == 2: # noun verbing
        noun = to_list(noun,doc_noun)
        verbing = to_list(verbing,doc_verbing)
        randn = rand_PoS(noun)
        randv = rand_PoS(verbing)
        prompt = "{} {}".format(randn,randv)
    elif setting == 3 and rand2 == 1: # adjective noun verbing
        adjective = to_list(adjective,doc_adjective)
        noun = to_list(noun,doc_noun)
        verbing = to_list(verbing,doc_verbing)
        randae = rand_PoS(adjective)
        randn = rand_PoS(noun)
        randv = rand_PoS(verbing)
        prompt = "{} {} {}".format(randae,randn,randv)
    elif setting == 3 and rand2 == 2: #noun verbing adverb
        noun = to_list(noun,doc_noun)
        verbing = to_list(verbing,doc_verbing)
        adverb = to_list(adverb,doc_adverb)
        randn = rand_PoS(noun)
        randv = rand_PoS(verbing)
        randab = rand_PoS(adverb)
        prompt = "{} {} {}".format(randn,randv,randab)
    elif setting == 3 and rand2 == 3: # adjective adjective noun
        adjective = to_list(adjective,doc_adjective)
        noun = to_list(noun,doc_noun)
        randae1 = rand_PoS(adjective)
        randae2 = rand_PoS(adjective)
        randn = rand_PoS(noun)
        prompt = "{} {} {}".format(randae1,randae2,randn)
    else:
        prompt = "Work in progress, please be patient"

    doc_noun.close()
    doc_verb.close()
    doc_verbing.close()
    doc_adjective.close()
    doc_adverb.close()
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
    
    if ctx.author.name == "Nicki (Mak)" and random.randint(1,50) == 1:
        return "Hey Nicki, I'm not trying to kink shame you, but I think you're developing an unhealthy relationship with my sass protocol"

    if(exists("text_files/condescending_phrases.txt")):
        condescend_list=open(r"text_files/condescending_phrases.txt",'r')
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
    elif iterations > 10:
        return "Less than 10 rolls please, I don't trust N's coding skills that much"
    rolls = []
    for i in range(iterations):
        rolls.append(random.randint(1,die))
    return ("You rolled {}".format(rolls))


def ourQuotes():
    random.seed()
    
    if(exists("text_files/genius_quotes.txt")):
        quote_list=open(r"text_files/genius_quotes.txt",'r')
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

def to_list(list, doc):
    for i, line in enumerate(doc):
        list.append(line)
    return list