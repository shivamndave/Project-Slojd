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

<<<<<<< HEAD
def makeHaiku1():
	print ("\n" + makeLine1(randSylLine(5)))
	print (makeLine1(randSylLine(7)))
	print (makeLine1(randSylLine(5)) + "\n")
	# apple1=makeLine1(randSylLine(5))
	# apple2=makeLine1(randSylLine(7))
	# apple3=makeLine1(randSylLine(5))
	apple = "\n\" " + makeLine1(randSylLine(5))+ "\n  " + makeLine1(randSylLine(7)) + "\n  " +makeLine1(randSylLine(5)) + "\"\n"
	return apple

=======
def randFileLine (size):
	startNum = randint(1, 4)
	fileList = []
	count = 0
	while (count < size):
		tempNum = randint(1, 4)
		fileList.append(tempNum)
		count+=1
	return fileList
>>>>>>> f7f40a5f0e22b6076d090a4a684c2276057f8d2d

def makeLine(sylCountList, fileCountList):
	# print ("SYL: " + str(sum(sylCountList)))
	# print ("FILE: " + str(fileCountList))
	retLine = ""
	for tempSy, tempFi in zip(sylCountList, fileCountList):
		tempLines = HaikuMod.getWordFile(tempFi, tempSy)
		if (len(tempLines)-1 < 1):
			print("\n**ERROR**\n")
			break
		tempLinesNum = randrange(0, len(tempLines))

		retLine += tempLines[tempLinesNum] + " "
	return retLine;	


def haikuType1():
	sylList1 = randSylLine(5)
	sylList2 = randSylLine(7)
	sylList3 = randSylLine(5)
	haikuStr = ("\n" + makeLine(sylList1, randFileLine(len(sylList1))) + "\n" + 
				makeLine(sylList2, randFileLine(len(sylList2))) + "\n" + 
				makeLine(sylList3, randFileLine(len(sylList3))) + "\n")
	return haikuStr

def haikuType2():
	sylList1 = randSylLine(5)
	sylList2 = randSylLine(7)
	sylList3 = randSylLine(5)
	haikuStr = ("\n" + makeLine(sylList1, randFileLine(len(sylList1))) + "\n" + 
				makeLine(sylList2, randFileLine(len(sylList2))) + "\n" + 
				makeLine(sylList3, randFileLine(len(sylList3))) + "\n")
	return haikuStr	

print (haikuType1() + haikuType2())





