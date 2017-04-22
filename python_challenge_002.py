#Michael Claveria
#Python Challenge 002
#http://www.pythonchallenge.com/pc/def/ocr.html
#goal find the rare characters in a text file full of symbols:
#
#The first 3 of 1220 lines:
#%%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*
#@##&{#&{&)*%(]{{([*}@[@&]+!!*{)!}{%+{))])[!^})+)$]#{*+^((@^@}$[**$&^{$!@#$%)!@(&
#+^!{%_$&@^!}$_${)$_#)!({@!)(^}!*^&!$%_&&}&_#&@{)]{+)%*{&*%*&@%$+]!*__(#!*){%&@++

#use collections for counting the symbol occurances
import collections

#read in txt file
with open('pc_002.txt', 'r') as f:
	data = f.read()

#go through each character in the txt file and count the number of 
# instances that it occurs

results = collections.OrderedDict()
for c in data:
	results[c] = results.get(c,0) + 1
#	print results[c]

#define rare occurence as below a given percent (used one percent at first)

percent = 1
#define the lower bound as the num of occ below x percent of total length
lb = percent * .001 * len(data)

#append the rare symbol to string if it appears less than lb times in the text
print ''.join([c for c in data if results[c] < lb])

#result is 'equality'

#######################################
#Notes:
#orginally I used collections.Counter to count occurances but the letters are
#not in order so even though I know the letters are 'aeilquty' I can't be 
#sure of the order (even though equality is pretty obvious!) instead I
#used OrderedDict() to get the count in order
#
#result = collections.Counter(mess_txt)
#print result
#Counter({')': 6186, '@': 6157, '(': 6154, ']': 6152, '#': 6115, '_': 6112, '[': 6108,
# '}': 6105, '%': 6104, '!': 6079, '+': 6066, '$': 6046, '{': 6046, '&': 6043, '*': 6034,
# '^': 6030, '\n': 1220, 'a': 1, 'e': 1, 'i': 1, 'l': 1, 'q': 1, 'u': 1, 't': 1, 'y': 1})
#
#####################################################


	
