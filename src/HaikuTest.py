from random import randint
from random import randrange
import sys
import glob
import errno
import HaikuMod

def randSylLine (max):
	startNum = randint(1, 4)
	sylList = [startNum]
	remainSyl = max - startNum
	while (remainSyl > 0):
		if(remainSyl > 4):
			tempNum = randint(1, 4)
		else: 
			tempNum = randint(1, remainSyl)
		sylList.append(tempNum)
		remainSyl-=tempNum
	return sylList

def makeHaiku1():
	print ("\n" + makeLine1(randSylLine(5)))
	print (makeLine1(randSylLine(7)))
	print (makeLine1(randSylLine(5)) + "\n")


def makeLine1(sylCountList):
	# print (sylCountList)
	retLine = ""
	for tempSy in sylCountList:
		tempFileNum = randint(1, 4)
		tempLines = HaikuMod.getWordFile(tempFileNum, tempSy)

		# print ("\nSyl Count: " + str(tempSy))
		# print ("File: " + str(tempFileNum))
		# print ("File Length: " + str(len(tempLines)))

		if (len(tempLines)-1 < 1):
			print("\n**ERROR**\n")
			break
		tempLinesNum = randrange(0, len(tempLines))

		# print ("Word: " + tempLines[tempLinesNum])

		retLine += tempLines[tempLinesNum] + " "
	return retLine;

makeHaiku1()



# ranSylNum = randint(1, 4)
# ranFileNum = randint(1, 4)
# ranLines = HaikuMod.getWordFile(ranFileNum, ranSylNum)
# randNounNum = randint(0, len(ranLines)-1)
# print ("Random " + str(ranFileNum) + " List(" + str(ranSylNum) + ") " + ranLines[randNounNum])

# Each of these gets a random file from each type and 
# puts it into a variable
# randomNounSylNum = randint(1, 4)
# randomNounLines = HaikuMod.getNounFile(randomNounSylNum)
# randNounNum = randint(0, len(randomNounLines)-1)

# randomAdjSylNum = randint(1, 4)
# randomAdjLines = HaikuMod.getAdjFile(randomAdjSylNum)
# randAdjNum = randint(0, len(randomAdjLines)-1)

# randomVerbSylNum = randint(1, 4)
# randomVerbLines = HaikuMod.getVerbFile(randomVerbSylNum)
# randVerbNum = randint(0, len(randomVerbLines)-1)

# randomAdverbSylNum = randint(1, 4)
# randomAdverbLines = HaikuMod.getAdverbFile(randomAdverbSylNum)
# randAdverbNum = randint(0, len(randomAdverbLines)-1)

# Shows which random syllable list is returned from each type
# print ("Random Noun List(" + str(randomNounSylNum) + ") " + randomNounLines[randNounNum])
# print ("Random Adj List(" + str(randomAdjSylNum) + ") " + randomAdjLines[randAdjNum])
# print ("Random Verb List(" + str(randomVerbSylNum) + ") " + randomVerbLines[randVerbNum])
# print ("Random Adverb List(" + str(randomAdverbSylNum) + ") " + randomAdverbLines[randAdverbNum])

