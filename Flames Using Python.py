'''
Created on Oct 8, 2014

@author: Avinash
'''

from _collections import deque

class flames:
    
    def main(self):
        self.__init__()
    
    def __init__(self):
        self.flames = {"F":"Friends forever", 
                       "L":"Lovers in heaven",
                       "A":"Affectionate to each other",
                       "M":"Married or gonna marry soon",
                       "E":"Enemies for life",
                       "S":"Sibling"
                       }
        self.getNames()
       
    
    def getNames(self):
        print "-------FLAMES--BY--AVINASH-----" 
        self.name1 = raw_input("enter first name")
        self.name2 = raw_input("enter second name")
        self.name1 = self.name1.lower().strip()
        self.name2 = self.name2.lower().strip()
        
        if (self.validNames()):
            self.calcFlameLen()
        else:
            print "invalid names - Only alphabets are allowed!!!"
            self.getNames()
            
    def validNames(self):
        flag = True
        if(not (self.name1.isalpha() and self.name2.isalpha())):
            flag=False
        return flag
    
    def calcFlameLen(self):
        nam1 = list(self.name1)
        nam2 = list(self.name2)
        for i in range(len(nam1)):
            for j in range(len(nam2)):
                if( nam1[i] == nam2[j]):
                    nam1[i] = '#'
                    nam2[j] = '#'
                    break
        newList = nam1 + nam2
        uniqLetters =  [ x for x in newList if x is not '#' ]
        totUniqLen = len(uniqLetters)
        self.totalLen = totUniqLen
        self.calFlames()
        
    def calFlames(self):    
        text = deque(list("FLAMES"))
        for i in range(5):
            flameLen = len(text)
            position = self.totalLen%flameLen
            text.remove(text[position-1])
            text.rotate(position)          
        self.flamesText = str(text[0])
        self.result()
    
    def result(self):
        flamesText = self.flamesText
        print ('{0} and {1} are {2}'.format(self.name1.upper(),self.name2.upper(),self.flames[flamesText]))



flames()