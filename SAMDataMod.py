import codeBits
import chatot
import SAMData as data
import SAMInfo as info
import pandas

def modifier(profile):
    running = True

    while running:
        p = input("Hello there Doctor, how can I help you?: ")
        if p == "output":
            inp = input('''1. name
            2. ID
            3. labID
            4. age
            5. time
            6. DOB
            7. height
            choice: ''')
            if inp == 0:
                running = False
            elif inp == 1:
                print(profile.name)
            elif inp == 2:
                print(profile.ID)
            elif inp == 3:
                print(profile.labID)
            elif inp == 4:
                print(profile.age)
            elif inp == 5:
                print(profile.time)
            elif inp == 6:
                print(profile.DOB)
            elif inp == 7:
                print(profile.height)

        elif p == "input":
            out = input('''1. name
            2. ID
            3. labID
            4. age
            5. time
            6. DOB
            7. height
            choice: ''')
            if out == 0:
                running = False
            elif out == 1:
                profile.setName(input('''Old name: {}
                New name: ''').format(profile.name))
            elif out == 2:
                profile.setID(input('''Old ID: {}
                New ID: ''').format(profile.ID))
            elif out == 3:
                profile.setLabID(input('''Old labID: {}
                New labID: ''').format(profile.labID))
            elif out == 4:
                profile.setAge(input('''Old age: {}
                New age: ''').format(profile.age))
            elif out == 5:
                profile.setTime(input('''Old time: {}
                New time: ''').format(profile.time))
            elif out == 6:
                profile.setDOB(input('''Old DOB: {}
                New DOB: ''').format(profile.DOB))
            elif out == 7:
                profile.setHeight(input('''Old height: {}
                New height: ''').format(profile.height))