'''
Created on Nov 5, 2014

@author: Avinash
'''

import random


def mimic_dict(filename):
    f = open(filename)
    text = f.read().split()
    
    myDict ={}
    prev=''
    for t in text:
        if prev in myDict.keys():
            myDict[prev] =  myDict[prev]+[t]
        else:
            myDict[prev] = [t]
        prev=t
    return myDict
            

def print_mimic(myDict, word):
    
    key=word
    for i in range(200):
        if key not in myDict:
            key=''
        myList = myDict[key]
        word = random.choice(myList)
        print word
        key=word


myDict = mimic_dict("alice.txt")
print_mimic(myDict,"")