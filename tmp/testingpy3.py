from random import randint
import sys
import glob
import errno
import os

# variables
x = 5
y = 7
z = 5

def randomness (n):
	line = ""
	while (n > 0):
		temp = randint(1, n)
		line = line + str(temp)
		n-=temp
	return line

print ("line1 is: " + randomness (x) + " line2 is: " + randomness(y) + " line3 is: " + randomness(z) )





wordList1 = ["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"]
wordList2 = ["visions", "distance", "conscience", "process", "chaos"]
wordList3 = ["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"]
wordList4 = ["true", "dark", "cold", "warm", "great"]
wordList5 = ["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]
wordList6 = ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]
wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]
		
  
# path = '/home/andy/Desktop/School/cmps112/projectslojd/dict/nouns/4syllablenouns.txt'   
# This path2 seems to work
path2 = os.path.dirname(os.path.abspath(__file__)) + "/dict/nouns/1syllablenouns.txt"

print (path2)

text_file = open(path2, "r")
# lines = text_file.readlines()
lines = text_file.read().split('\r\n')
lines = list(filter(None, lines))
# print lines #too many words so I'll comment out
x = len(lines)
print (len(lines))
text_file.close()
wordIndex8=randint(0, len(lines)-1)
print (lines[wordIndex8] + " ,APPLES TEST!")


# # This thing just prints out the contents of the file
# files = glob.glob(path2)   
# for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
#     try:
#         with open(name) as f: # No need to specify 'r': this is the default.
#             sys.stdout.write(f.read())
#     except IOError as exc:
#         if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
#             raise # Propagate other kinds of IOError.

wordIndex1=randint(0, len(wordList1)-1)
wordIndex2=randint(0, len(wordList2)-1)
wordIndex3=randint(0, len(wordList3)-1)
wordIndex4=randint(0, len(wordList4)-1)
wordIndex5=randint(0, len(wordList5)-1)
wordIndex6=randint(0, len(wordList6)-1)
wordIndex7=randint(0, len(wordList7)-1)

haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",\n" 
haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",\n"
haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."

print(haiku)
