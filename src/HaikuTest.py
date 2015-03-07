from random import randint
import sys
import glob
import errno
import HaikuMod

# Each of these gets a random file from each type and 
# puts it into a variable
randomNounSylNum = randint(1, 4)
randomNounLines = HaikuMod.getNounFile(randomNounSylNum)
randNounNum = randint(0, len(randomNounLines)-1)

randomAdjSylNum = randint(1, 4)
randomAdjLines = HaikuMod.getAdjFile(randomAdjSylNum)
randAdjNum = randint(0, len(randomAdjLines)-1)

randomVerbSylNum = randint(1, 4)
randomVerbLines = HaikuMod.getVerbFile(randomVerbSylNum)
randVerbNum = randint(0, len(randomVerbLines)-1)

randomAdverbSylNum = randint(1, 4)
randomAdverbLines = HaikuMod.getAdverbFile(randomAdverbSylNum)
randAdverbNum = randint(0, len(randomAdverbLines)-1)

# Shows which random syllable list is returned from each type
print ("Random Noun List(" + str(randomNounSylNum) + ") " + randomNounLines[randNounNum])
print ("Random Adj List(" + str(randomAdjSylNum) + ") " + randomAdjLines[randAdjNum])
print ("Random Verb List(" + str(randomVerbSylNum) + ") " + randomVerbLines[randVerbNum])
print ("Random Adverb List(" + str(randomAdverbSylNum) + ") " + randomAdverbLines[randAdverbNum])




