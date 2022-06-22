import os
import codeBits

for path in os.listdir("text-files/"):
    doc = os.path.join("text-files/", path)
    if os.path.isfile(doc) and doc[-11:-4] != "curated" and doc[-10:-4] != "output":
        with open(doc,'r') as x:
            wordList = codeBits.to_list(x)
        for line in wordList: # first clean up the lines
            line = line.strip()

        # stolen from manjeet_04 at geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
        curated = []
        [curated.append(x) for x in wordList if x not in curated]

        # i would rather have a separate curated file than risk overwriting the original document and something going wrong
        # which, may i add, did happen
        with open(doc[:-4] + "_curated.txt",'w') as y:
            for line in curated:
                y.write(line)