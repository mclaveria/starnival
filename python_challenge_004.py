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

import re, urllib.request

baseStr = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nbr = '12345'
answer = ''
for x in range(1,400):
    response = urllib.request.urlopen(baseStr + nbr)
    print ('URL: ', response.geturl())
    data = response.read()
    print ('data is:' + str(data))
    #After running this I found a special case: telling you to divide old number by 2
    if 'Divide by two' in str(data):
        nbr = str(int(int(nbr)/2))
        #print ('number is: ' + str(nbr))
    else:
        #search for the number to replace nbr and move to next nothing 
        nbrList = re.findall("next nothing is (\d+)",str(data))
        #if there is no next number, then you found the solution so stop
        if str(nbrList) == '[]':
            answer = data
            break
        nbr = ''.join([n for n in nbrList])
        #print ('number is: ' + str(nbr))
    
print ('the answer is ' + str(answer))

"""
URL:  http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831
data is: peak.html
the answer is peak.html
"""