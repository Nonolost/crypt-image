# -*-coding:utf-8 -*-

import cgi, os
import cgitb; cgitb.enable()
from SteganoClass import SteganoClass
from PIL import Image
import time

def encrypt():
	# on récupère la requête et les éléments de la requête
	requete = cgi.FieldStorage()

	nouveau = requete.getvalue('new')
	message = requete.getvalue('mess')
	image = requete.getvalue('image')
	cheminImage = requete.getvalue('nom')

	# on vérifie que la requête contient toutes les variables dont on a besoin suivant l'état (image envoyée ou présente sur le serveur)
	if not nouveau or not message or (nouveau == '1' and (not image or not cheminImage)) :
		return


	if nouveau == '1':
		# on va recomposer l'image qui nous a été envoyée et l'ouvrir pour s'en servir
		nomImage = cheminImage.split('\\')[-1]
		cheminServeur = "data/img/tmp/"+str(time.time())+nomImage

		f = open(cheminServeur, 'wb')
		f.write(image)
		f.close()

		imagePIL = Image.open(cheminServeur)
	elif nouveau == '0':
		cheminServeur = "data/img/tmp/"+str(time.time())+image.split('/')[-1]

		# on ouvre simplement l'image présente sur notre serveur
		imagePIL = Image.open("data/img/"+image.split('/')[-1])
		
	SteganoClass.hide(SteganoClass(imagePIL, message)).save(cheminServeur)

	# on renvoie au client du code html qui contient un lien vers la nouvelle image créée contenant le message crypté
	print 'Content-Type: text/html\n\n'
	print '<h1 class="center-block">Prend ça et va-t-en !</h1>'
	print '<img class="center-block" src="'+cheminServeur+'"/>'

if __name__ == '__main__':
	encrypt()