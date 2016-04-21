#!C:/Python27/python.exe
# -*-coding:utf-8 -*-
#print "Content-type: text/html\r\n\r\n";
#//20256542

import cgi, os
import cgitb; cgitb.enable()
import requests

form = cgi.FieldStorage()




# Test if the file was uploaded
   # strip leading path from file name to avoid 
   # directory traversal attacks
if (form.getvalue('new')=='1'):

	nom = form.getvalue('nom').split('\\')[-1]
	fileitem = form.getvalue('image')
	npath = "data/img/tmp/"+nom
	f = open(npath, 'wb')
	f.write(fileitem)
	f.close()

	from SteganoClass import SteganoClass
	from PIL import Image

	lenaPure = Image.open(npath)
	stegMess = form.getvalue('mess')

	steg = SteganoClass(lenaPure, stegMess)

	crypt = SteganoClass.hide(steg)
	crypt.save(npath)

else:
	path = form.getvalue('image')
	coupe = path.split('/')

	path = "data/img/"+coupe[-1]
	from SteganoClass import SteganoClass
	from PIL import Image
	import time

	lenaPure = Image.open(path)
	stegMess = form.getvalue('mess')

	steg = SteganoClass(lenaPure, stegMess)

	crypt = SteganoClass.hide(steg)
	npath = "data/img/tmp/"+str(time.time())+coupe[-1]
	crypt.save(npath)


print 'Content-Type: text/html\n\n'
print '<h1 class="center-block">Prend ça et va-t-en !</h1>'
print '<img class="center-block" src="'+npath+'"/>'