from random import randint
import sys
import glob
import errno
import HaikuMod

randomNounSylNum =randint(1, 4)
randomNounLines = HaikuMod.getNounFile(randomNounSylNum)

randomAdjSylNum =randint(1, 4)
randomAdjLines = HaikuMod.getAdjFile(randomAdjSylNum)

randomVerbSylNum =randint(1, 4)
randomVerbLines = HaikuMod.getVerbFile(randomVerbSylNum)

randomAdverbSylNum =randint(1, 4)
randomAdverbLines = HaikuMod.getAdverbFile(randomAdverbSylNum)

print "Random Noun List(" + str(randomNounSylNum) + ")"
print "Random Adj List(" + str(randomAdjSylNum) + ")"
print "Random Verb List(" + str(randomVerbSylNum) + ")"
print "Random Adverb List(" + str(randomAdverbSylNum) + ")"



