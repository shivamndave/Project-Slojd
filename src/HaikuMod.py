import os

basePath = os.path.dirname(os.path.abspath(__file__))

nounsFilePath = os.path.abspath(os.path.join(basePath, "../dict/nouns"))
adjFilePath = os.path.abspath(os.path.join(basePath, "../dict/adjectives"))
verbFilePath = os.path.abspath(os.path.join(basePath, "../dict/verbs"))
adverbFilePath = os.path.abspath(os.path.join(basePath, "../dict/adverbs"))

nounPath1 = nounsFilePath + "/1syllablenouns.txt"
nounPath2 = nounsFilePath + "/2syllablenouns.txt"
nounPath3 = nounsFilePath + "/3syllablenouns.txt"
nounPath4 = nounsFilePath + "/4syllablenouns.txt"

adjPath1 = adjFilePath + "/1syllableadjectives.txt"
adjPath2 = adjFilePath + "/2syllableadjectives.txt"
adjPath3 = adjFilePath + "/3syllableadjectives.txt"
adjPath4 = adjFilePath + "/4syllableadjectives.txt"

verbPath1 = verbFilePath + "/1syllableverbs.txt"
verbPath2 = verbFilePath + "/2syllableverbs.txt"
verbPath3 = verbFilePath + "/3syllableverbs.txt"
verbPath4 = verbFilePath + "/4syllableverbs.txt"

adverbPath1 = adverbFilePath + "/1syllableadverbs.txt"
adverbPath2 = adverbFilePath + "/2syllableadverbs.txt"
adverbPath3 = adverbFilePath + "/3syllableadverbs.txt"
adverbPath4 = adverbFilePath + "/4syllableadverbs.txt"

nounFile1 = open(nounPath1, "r")
nounFile2 = open(nounPath2, "r")
nounFile3 = open(nounPath3, "r")
nounFile4 = open(nounPath4, "r")

adjFile1 = open(adjPath1, "r")
adjFile2 = open(adjPath2, "r")
adjFile3 = open(adjPath3, "r")
adjFile4 = open(adjPath4, "r")

verbFile1 = open(verbPath1, "r")
verbFile2 = open(verbPath2, "r")
verbFile3 = open(verbPath3, "r")
verbFile4 = open(verbPath4, "r")

adverbFile1 = open(adverbPath1, "r")
adverbFile2 = open(adverbPath2, "r")
adverbFile3 = open(adverbPath3, "r")
adverbFile4 = open(adverbPath4, "r")

# Enter a number to get a file based on syllable count
# EX: getNounFile(3) = gets 3 syllable noun file

def getNounFile(sylNumN):
	if sylNumN == 1:
		nounLines1 = nounFile1.read().split('\r\n')
		return filter(None, nounLines1)
	if sylNumN == 2:
		nounLines2 = nounFile2.read().split('\r\n')
		return filter(None, nounLines2)
	if sylNumN == 3:
		nounLines3 = nounFile3.read().split('\r\n')
		return filter(None, nounLines3)
	if sylNumN == 4:
		nounLines4 = nounFile4.read().split('\r\n')
		return filter(None, nounLines4)

def getAdjFile(sylNumAj):
	if sylNumAj == 1:
		adjLines1 = adjFile1.read().split('\r\n')
		return filter(None, adjLines1)
	if sylNumAj == 2:
		adjLines2 = adjFile2.read().split('\r\n')
		return filter(None, adjLines2)
	if sylNumAj == 3:
		adjLines3 = adjFile3.read().split('\r\n') 
		return filter(None, adjLines3)
	if sylNumAj == 4:
		adjLines4 = adjFile4.read().split('\r\n')
		return filter(None, adjLines4)

def getVerbFile(sylNumV):
	if sylNumV == 1:
		verbLines1 = verbFile1.read().split('\r\n')
		return filter(None, verbLines1)
	if sylNumV == 2:
		verbLines2 = verbFile2.read().split('\r\n')
		return filter(None, verbLines2)
	if sylNumV == 3:
		verbLines3 = verbFile3.read().split('\r\n')
		return filter(None, verbLines3)
	if sylNumV == 4: 
		verbLines4 = verbFile4.read().split('\r\n')
		return filter(None, verbLines4)

def getAdverbFile(sylNumAv):
	if sylNumAv == 1:
		adverbLines1 = adverbFile1.read().split('\r\n')
		return list(filter(None, adverbLines1))
	if sylNumAv == 2:
		adverbLines2 = adverbFile2.read().split('\r\n')
		return list(filter(None, adverbLines2))
	if sylNumAv == 3:
		adverbLines3 = adverbFile3.read().split('\r\n')
		return list(filter(None, adverbLines3))
	if sylNumAv == 4:
		adverbLines4 = adverbFile4.read().split('\r\n')
		return list(filter(None, adverbLines4))
	