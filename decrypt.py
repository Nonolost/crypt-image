#!C:/Python27/python.exe
#print "Content-type: text/html\r\n\r\n";
#//20256542

import cgi, os
import cgitb; cgitb.enable()
import requests

form = cgi.FieldStorage()


fileitem = form.getvalue('image')


# Test if the file was uploaded
   # strip leading path from file name to avoid 
   # directory traversal attacks
nom = form.getvalue('nom').split('\\')[-1]
path = "data/img/tmp/"+nom
f = open(path, 'wb')
f.write(fileitem)
f.close()

from SteganoClass import SteganoClass
from PIL import Image

lenaPure = Image.open(path)

steg2 = SteganoClass(lenaPure, '')
hiddenMess = SteganoClass.reveal(steg2)

print 'Content-Type: text/html\n\n'
print '<p class="result">'+hiddenMess+'</p>'

#crypt.show()

#