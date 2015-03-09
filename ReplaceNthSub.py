'''
Created on Sep 22, 2014

@author: Avinash
'''



def findnthIndex(sub,text,n):
    subs = text.split(sub,n)
    if len(subs) < n+1:
        return -1
    else:
        return  len(text)-len(subs[n])-len(sub)
         

def replaceNsub(sub,replstr,text,n):
    index = findnthIndex(sub, text, n)
    if index >= 0:
        text= text[0:index] + text[index:].replace(sub,replstr,1)
    return text


name1 = "avinashchander"
print replaceNsub("a","yoyo",name1,3)




