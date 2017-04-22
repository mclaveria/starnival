#Michael Claveria
#Python Challenge 001
#
#Goal: Unscramble the following message:
#
#g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
#bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
#sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. 
#
#the hint given is a picture with the following: K->M, O->Q, E->G
#
#the shift is two letters to the right with Y wrapping around to A and
#Z wrapping around to B

import string
#read in the code message file in read only form
with open('pc_001_message.txt','r') as f:
    scram_txt = f.read()
#get the letters a-z
alphabet = string.ascii_lowercase
#get the letters shifted by two aka c..z,a,b
alphabetSh = alphabet.lstrip('ab')+'ab'
print 'The alphabet is: ' + alphabet
print 'The shifted alphabet is: ' + alphabetSh
print 'The coded message is: ' + scram_txt
#map the letters in the coded message a->c, b->d, ...x->z, y->a, z->b
table = string.maketrans(alphabet,alphabetSh)
print (scram_txt.translate(table))
##################################################################
#result:
# i hope you didnt translate it by hand. 
# thats what computers are for. doing it in by hand is inefficient
# and that's why this text is so long. using string.maketrans()
# is recommended. now apply on the url.
#
###################################################################

#url file ending is map:

print ('map'.translate(table))
#result is ocr
