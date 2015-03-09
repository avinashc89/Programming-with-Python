'''
Created on Oct 10, 2014

@author: Avinash
'''


import re, urllib

textfile = file('depth_1.txt','wt')
print "Enter the URL you wish to crawl.."
print 'Usage  - "http://www.google.com/" <-- With the double quotes'
myurl = input("@> ")
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
        print i  
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                print ee
                textfile.write(ee+'\n')
textfile.close()

