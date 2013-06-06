#Michael Claveria
#Python Challenge 004
#http://www.pythonchallenge.com/pc/def/linkedlist.php
#
#goal: go to the url -
#http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
#which contains the message:
#'and the next nothing is 44827'
#read the number in the body of the page and replace the nothing=xxxxx
#with that number for each URL for 400 times

#the hint is: 
#urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
#end. 400 times is more than enough.

import re,urllib2

baseStr = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nbr = '12345'
answer = ''
for x in xrange (1,400):
    response = urllib2.urlopen(baseStr + nbr)
    print 'URL: ', response.geturl()
    data = response.read()
    print 'data is: ' + data
    #After running this I found a special case: telling you to divide old number by 2
    if 'Divide by two' in data:
		nbr = str(int(nbr)/2)
		print 'number is: ' + nbr
    else:
       #search for the number to replace nbr and move to next nothing 
       nbrList = re.findall('next nothing is (\d+)',data)
       # if there is no next number, then you found the solution so stop
       if str(nbrList) == '[]':
		   answer = data
		   break
       nbr = ''.join([n for n in nbrList])
       print 'number is: ' + nbr
    
print 'the answer is ' + answer

#URL:  http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831
#data is: peak.html
#the answer is peak.html




