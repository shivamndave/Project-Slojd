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
	# apple1=makeLine1(randSylLine(5))
	# apple2=makeLine1(randSylLine(7))
	# apple3=makeLine1(randSylLine(5))
	apple = "\n\" " + makeLine1(randSylLine(5))+ "\n  " + makeLine1(randSylLine(7)) + "\n  " +makeLine1(randSylLine(5)) + "\"\n"
	return apple


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

