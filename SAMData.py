import codeBits
import chatot
import SAMDataMod as mod
import SAMInfo as info
import scipy as sci
import numpy as num
import matplotlib as plt
import pandas
from datetime import datetime

class userProfile:
    """Don't be afraid, I won't sell your data. I'll just check it whenever I feel like it"""
    name = ""
    pronouns = ["They","Them","Their"]
    ID = 0
    labID = 0
    age = 0
    time = 2267718
    DOB = ""
    height = "6.9m"
    bloodType = ""
    eyeColor = ""
    study = ""
    dept = ""
    entryDate = ""
    joinDate = ""
    coatSize = ""
    phone = ""
    email = ""
    MBPT = ""
    PSA = ""
    RA = ""
    MS = ""
    OI = ""


    # the one SAM makes automatically
    def __init__(self, id, nombre):
        try:
            self.ID = id
        except ValueError:
            print("ID: Invalid data type")
            return
        try:
            self.name = nombre
        except ValueError:
            print("Name: Invalid data type")
            return
        try:
            now = datetime.utcnow()
            if now.month < 10:
                month = "0" + str(now.month)
            else:
                month = str(now.month)
            if now.day < 10:
                day = "0" + str(now.day)
            else:
                day = str(now.day)
            self.entryDate = str(now.year) + month + day
        except ValueError:
            print("Entry Date: Invalid data type")
            return

    # not necessary?
    def setName(self, nombre):
        try:
            self.name = nombre
        except ValueError:
            print("Invalid data type")

    def setID(self, id):
        try:
            self.ID = id
        except ValueError:
            print("Invalid data type")

    def setLabID(self, lid):
        try:
            self.labID = lid
        except ValueError:
            print("Invalid data type")

    def setAge(self, old):
        try:
            self.age = old
        except ValueError:
            print("Invalid data type")

    def setTime(self, numero):
        try:
            self.time = numero
        except ValueError:
            print("Invalid data type")

    def setDOB(self,birf):
        try:
            c = checkDateValid(birf)
            if c == "a":
                self.DOB = birf
            else:
                print(c)
        except ValueError:
            print("Invalid data type")

    def setHeight(self, high):
        try:
            self.height = high
        except ValueError:
            print("Invalid data type")

    def setBloodType(self, blood):
        try:
            self.bloodType = blood
        except ValueError:
            print("Invalid data type")

    def setEyeColor(self, color):
        try:
            self.eyeColor = color
        except ValueError:
            print("Invalid data type")

    def setStudy(self, stud):
        try:
            self.study = stud
        except ValueError:
            print("Invalid data type")

    def setDept(self, arment):
        try:
            self.dept = arment
        except ValueError:
            print("Invalid data type")
    
    def setEntryDate(self, ahora):
        try:
            c = checkDateValid(ahora)
            if c == "a":
                self.entryDate = ahora
            else:
                print(c)
        except ValueError:
            print("Invalid data type")

    def setJoinDate(self, dato):
        try:
            c = checkDateValid(dato)
            if c == "a":
                self.joinDate = dato
            else:
                print(c)
        except ValueError:
            print("Invalid data type")

    def setCoatSize(self, coat):
        try:
            self.coatSize = coat
        except ValueError:
            print("Invalid data type")

    def setPhone(self, telephono):
        try:
            self.phone = telephono
        except ValueError:
            print("Invalid data type")

    def setEmail(self, mail):
        try:
            self.email = mail
        except ValueError:
            print("Invalid data type")
    
    def setMBPT(self, LMAO):
        try:
            self.MBPT = LMAO
        except ValueError:
            print("Invalid data type")

    def setPSA(self, info):
        try:
            self.PSA = info
        except ValueError:
            print("Invalid data type")

    def setRA(self, TS):
        try:
            self.RA = TS
        except ValueError:
            print("Invalid data type")

    def setMS(self, NA):
        try:
            self.MS = NA
        except ValueError:
            print("Invalid data type")

    def setOI(self, info):
        try:
            self.OI = info
        except ValueError:
            print("Invalid data type")


def checkDateValid(date):
    try:
        ycheck = int(date[0 : 2])
        fycheck = int(date[0 : 4])
        lycheck = int(date[2 : 4])
        mcheck = int(date[4 : 6])
        dcheck = int(date[6 : ])
    except ValueError:
        print("Please check your input")
    except IndexError:
        print("Please check your input, it should be 8 numbers long")
    
    longMonths = [1,3,5,7,8,10,12]
    leapYear = False

    if lycheck == 0:
        if fycheck % 400 == 0:
            leapYear = True
    elif fycheck % 4 == 0:
        leapYear = True
    
    if ycheck < 19 or ycheck > 20:
        print("Please format date as YearMonthDate")
    elif fycheck > datetime.year:
        print("Please enter a valid date")
    elif fycheck > (datetime.year - 18):
        print("I'm pretty sure it's illegal to store information on minors")
    elif mcheck > 12:
        print("Please format date as YearMonthDate")
    elif mcheck < 1:
        print("Please enter a valid month")
    elif dcheck < 1 or dcheck > 31:
        print("Please enter a valid day")
    elif mcheck == 2 and dcheck > 29:
        print("Please enter a valid day")
    elif mcheck == 2 and dcheck == 29 and not leapYear:
        print("Please enter a valid day, {} was not a leap year".format(fycheck))
    elif mcheck not in longMonths and dcheck == 31:
        print("Please enter a valid day")
    else:
        return "a"


class commandData:
    """Keeping track of how many times each command is used"""
    total = 0
    incorrect = 0

    def __init___(self):
        print("Command data {} created".format(self))


class draw(commandData):
    """Special class for draw"""
    varientCount = [] # counts times each varient called
    POSCount = [] # counts times each POS is called
    words = [] # list of every word
    wordsCount = [] # counts times each word is used
    wrdCnt = []
    # words and wordsCount could be combined into a single 2D array if i want to get into that mess

    def __init__(self, list_nouns, list_verbs, list_verbing, list_adjectives, list_adverbs):
        self.varientCount = [0,0,0,0,0] # 0:draw, 1:2, 2:3, 3:4, 4:5
        self.POSCount = [0,0,0,0,0] # 0:noun, 1:verb, 2:verbing, 3:adjective, 4:adverb
        self.words.append(list_nouns + list_verbs + list_verbing + list_adjectives + list_adverbs)
        for i in self.words: # a new 0 for every word
            self.wordsCount.append(0)


class roll(commandData):
    dieCount = [] # how many times each die is rolled
    rollsCount = [] # how many times each number of rolls is called
    outcomes = [[]] # list of every outcome from each die

    def __init__(self):
        self.dieCount = [0] * 8 # 0:2, 1:4, 2:6, 3:8, 4:10, 5:12, 6:20, 7:100