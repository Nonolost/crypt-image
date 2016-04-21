# -*-coding:utf-8 -*-

import cgi, os
import cgitb; cgitb.enable()
from SteganoClass import SteganoClass
from PIL import Image

def decrypt():
	# on récupère la requête utilisateur et l'image qu'il nous envoie
	requete = cgi.FieldStorage()
	image = requete.getvalue('image')
	cheminImage = requete.getvalue('nom')

	if image and cheminImage:
		# on récupère le nom de l'image pour consituer le path sur le serveur
		nomImage = cheminImage.split('\\')[-1]

		# idéalement, on a un script qui supprime toutes les heures les fichierd dans tmp
		cheminServeur = "data/img/tmp/" + nomImage

		# on reconstitue l'image
		f = open(cheminServeur, 'wb')
		f.write(image)
		f.close()

		# on récupère le message caché
		messageCache = SteganoClass.reveal(SteganoClass(Image.open(cheminServeur), ''))

		# on consitute une réponse que le client va récupérer avec le message caché récupéré
		print 'Content-Type: text/html\n\n'
		print '<p class="result">'+messageCache+'</p>'

if __name__ == '__main__':
	decrypt()