# -*- coding: utf-8 -*-

import cgi 
from os import listdir
from os.path import isfile, join

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

#print(form.getvalue("name"))

html = """<!DOCTYPE html>
<head>
	<meta charset="utf-8">
    <title>Mon programme</title>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
	<link rel="stylesheet" href="//blueimp.github.io/Gallery/css/blueimp-gallery.min.css">
	<link rel="stylesheet" href="css/style.css">
	<link rel="stylesheet" href="css/hexagone-grid.css">
</head>
<body>
	<div class="jumbotron">
	<div class="row">
		<div class="col-md-9">
		<h1>Crypt'Image</h1>
		<p>Crypt'Image est un service imaginé dans le cadre du projet de sécurité informatique à l'Université de Sherbrooke.</p>
		<p>Il met en place divers mécanismes pour protéger le serveur web, les informations transférées, et propose d'encrypter des données dans une image.</p>
		</div>
		<div class="col-md-3">
		<ul class="categories" class="clr">
			<li>
		      <div>
		        <img src="data/img/team/arnaud.jpg" alt=""/>
		     </div>
		  </li>
			<li>
		      <div>
		        <img src="data/img/chaton.jpg" alt="Arnaud Lods"/>
		     </div>
		  </li>
		  <li class="pusher"></li>
			<li>
		      <div>
		        <img src="data/img/chaton.jpg" alt=""/>
		     </div>
		  </li>
			<li>
		      <div>
		        <img src="data/img/chaton.jpg" alt=""/>
		     </div>
		  </li>

		  <li class="pusher"></li>

		  <li class="pusher"></li>
			<li>
		      <div>
		        <img src="data/img/chaton.jpg" alt=""/>
		     </div>
		  </li>
		</ul>
		</div>
	</div>
	</div>
	<div class="container">
"""

html+="""<div class="row"><div class="col-md-6"> """

html+="""<h1>Cacher un message</h1>
<h3>Étape 1 : Sélectionner ou uploader une image</h3>
<p>Sélectionnez l'image qui servira à cacher votre message. Si aucune image ne vous plait, vous pouvez nous envoyer les votre, elles seront mise à disposition immédiatement</p>


"""
pathToImg = "data/img/"
imgs = [f for f in listdir(pathToImg) if isfile(join(pathToImg, f))]

links = """<ul class="categories" class="clr">"""
for img in imgs:
	links+="""<li>
		      <div>
		        <img src=""" + pathToImg + img + """ alt=""/>
		     </div>
		  </li>"""

links += """</ul>"""

html+=links


html+="""<h3>Étape 2 : Entrer le message à cacher</h3>
<p>Écrivez le message que vous souhaitez cacher dans l'image.</p>
"""

html+="""<h3>Étape 3 : Entrer le mot de passe</h3>
<p>Entrez le mot de passe qui servira à crypter le message. Une clé publique vous sera fournie vous permettant de décrypter le message de l'image.</p>

<button type="button" class="btn btn-primary">Cache moi ça !</button>
</div>"""

html+="""<div class="col-md-6"><h1>Récupérer un message</h1>
<h3>Étape 1 : Uploader votre image</h3>
<p>Uploadez l'image qui contient le message caché que vous souhaitez récupérer.</p>
"""

html+="""<h3>Étape 2 : Entrer la clé</h3>
<p>Écrivez la clé qui vous a été fournie après l'encryptage du message pour récupérer ce dernier.</p>
<button type="button" class="btn btn-primary">Montre moi ça !</button>
</div>"""

html+="""	
	</div>
</body>
</html>
"""

print(html)
