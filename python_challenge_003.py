#Michael Claveria
#Python Challenge 003
#http://www.pythonchallenge.com/pc/def/equality.html
#
# The hint for this puzzle is:
# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

#The file to parse contains 1250 lines of lowercase and uppercase letters
#
# I interpret the idea is to look for all the lowercase letters between exactly 3 uppercase letters:
# The format would be *XXXxXXX* where x is lowercase, X is uppercase and * is anything but an uppercase letter
# Using regular experessions should make this a simple task:

import re

#read in txt file
with open('pc_003.txt','r') as f:
	data = f.read()
#	testData = "aAAAaAAAbBBB"

# write regular expression to search for strings *XXXxXXX* in data
# (?<![A-Z]) is a lookback letter not between A-Z (uppercase)
#   [A-Z]{3} is three uppercase letters
#   ([a-z]) is the lowercase letter to find
#   (?![A-Z]) is a look forward letter not between A-Z (uppercase)
result = re.findall('(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])',data)
print('Result is: ')
print (''.join([c for c in result]))

#linkedlist is the printed final answer
