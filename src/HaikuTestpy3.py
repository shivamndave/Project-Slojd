from random import randint
import sys
import glob
import errno
import HaikuMod

# Each of these gets a random file from each type and 
# puts it into a variable
randomNounSylNum =randint(1, 4)
randomNounLines = HaikuModpy3.getNounFile(randomNounSylNum)

randomAdjSylNum =randint(1, 4)
randomAdjLines = HaikuModpy3.getAdjFile(randomAdjSylNum)

randomVerbSylNum =randint(1, 4)
randomVerbLines = HaikuModpy3.getVerbFile(randomVerbSylNum)

randomAdverbSylNum =randint(1, 4)
randomAdverbLines = HaikuModpy3.getAdverbFile(randomAdverbSylNum)

# Shows which random syllable list is returned from each type
print ("Random Noun List(" + str(randomNounSylNum) + ")")
print ("Random Adj List(" + str(randomAdjSylNum) + ")")
print ("Random Verb List(" + str(randomVerbSylNum) + ")")
print ("Random Adverb List(" + str(randomAdverbSylNum) + ")")



