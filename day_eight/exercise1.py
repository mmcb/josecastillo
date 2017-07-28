



#Please write a program which count and print the numbers of each character, from file letters.txt, in a string input by console.




#exercise 1

import string

def count_letters(string):
	finalResultDict = {}
	for letter in string:
		character = letter.lower()
		if character in finalResultDict.keys():
			finalResultDict[character] += 1
		else:
			finalResultDict[character] = 1
		return finalResultDict

with open("letters.txt") as lettFile:
	lettFileString = lettFile.read()
	letterCountDict = count_letters(lettFileString)
	for key, value in letterCountDict.items():
		print(key, value)
	lettFile.close()




