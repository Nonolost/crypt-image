# -*- coding: utf-8 -*-

import cgi 
from os import listdir
from os.path import isfile, join
from flask import request

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")


html = """
<!DOCTYPE html>
<head>
	<meta charset="utf-8">
    <title>Mon programme</title>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1/jquery.js"></script>
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
				        	<img src="data/img/team/arnaud.jpg" alt="Arnaud Lods"/>
				     	</div>
				  	</li>
					<li>
				      	<div>
				        	<img src="data/img/team/antoine.jpg" alt="Antoine Vella"/>
				     	</div>
				  	</li>
				  	<li class="pusher"></li>
					<li>
				      	<div>
				        	<img src="data/img/team/jeremy.jpg" alt=""/>
				     	</div>
				  	</li>
					<li>
				      	<div>
				        	<img src="data/img/team/flavien.jpg" alt=""/>
				     	</div>
				  	</li>
				  	<li class="pusher"></li>
				  	<li class="pusher"></li>
					<li>
				      	<div>
				        	<img src="data/img/team/yann.jpg" alt=""/>
				     	</div>
				  	</li>
				</ul>
			</div>
		</div>
	</div>
	<div class="container">
	<div class="row">
		<form action="/index.py" method="post" class="col-md-6 my-form form-left" enctype="multipart/form-data"> 
			<h1>Cacher un message</h1>
			<h3>Étape 1 : Sélectionner ou uploader une image</h3>
			<p>Envoie-nous l'image que tu souhaites utiliser...</p>
			<div class="input-group">
				<span class="input-group-btn">
					<span class="btn btn-primary btn-file">
				    	Upload un fichier <input name="fichier" type="file" id="encrypt-fichier" class="de-file">
					</span>
				</span>
				<input id="encrypt-img" type="text" class="form-control" readonly>
			</div>
			<br>
			<p>... ou sélectionne une image parmis nos exemples disponibles !</p>
"""

pathToImg = "data/img/"
imgs = [f for f in listdir(pathToImg) if isfile(join(pathToImg, f))]

links = """
			<ul class="categories" class="clr">
"""
for img in imgs:
	links+="""
				<li>
		      		<div class="imgSelection" onclick="selectImg(this)">
		        		<img class="imgBB" src=""" + pathToImg + img + """ alt=""/>
		     		</div>

		  		</li>
	"""

links += """
			</ul>
"""

html+=links


html+="""
			<h3>Étape 2 : Entrer le message à cacher</h3>
			<p>Écrit le message à cacher dans l'image.</p>
			<div class="form-group">
				<textarea class="form-control" rows="5" id="encrypt-message"></textarea>
			</div>

			<h3>Étape 3 : Entrer le mot de passe</h3>
			<p>Entre le mot de passe qui servira à crypter le message. Elle servira à récupérer le message à partir de l'image plus tard !</p>
			<div class="form-group">
				<input type="password" class="form-control" id="encrypt-mdp">
			</div>
			<br>
			<button type="button" class="btn btn-primary btn-lg center-block" onclick="preparerEnvoieEncrypt()">Cache moi ça !</button>
		</form>

		<form class="col-md-6 my-form"><h1>Récupérer un message</h1>
			<h3>Étape 1 : Uploader votre image</h3>
			<p>Envoie nous l'image qui contient le message caché à récupérer.</p>
			<div class="input-group">
				<span class="input-group-btn">
					<span class="btn btn-primary btn-file">
				    	Upload un fichier <input type="file" id="decrypt-fichier">
					</span>
				</span>
				<input id="decrypt-img" type="text" class="form-control" readonly>
			</div>

			<h3>Étape 2 : Entrer la clé</h3>
			<p>Écrit le mot de passe qui a servi à cacher le message initialement !</p>
			<div class="form-group">
				<input type="password" class="form-control" id="decrypt-mdp">
			</div>

			<br>

			<button type="button" class="btn btn-primary btn-lg center-block" onclick="preparerEnvoieDecrypt()">Montre moi ça !</button>
		</form>

		<div class="col-md-6" id="result"></div>
	</div>

	<script>
		function selectImg(object) {
			$("#selected-icon").remove();
			$(".selected").removeClass("selected");
			$(object).append('<img id="selected-icon" src="data/img/icons/selected-icon.png"/>');
			$(object).addClass("selected");
			$('#encrypt-img').val("");
		}

		$(document).on('change', '.btn-file :file', function() {
			var input = $(this),
				label = input.val();
			
			input.trigger('fileselect', [label]);
		});

		$(document).ready( function() {
			$('.btn-file :file').on('fileselect', function(event, label) {
				if($(this).hasClass('de-file'))
					$('#encrypt-img').val(label);
				else
					$('#decrypt-img').val(label);
				$("#selected-icon").remove();
				$(".selected").removeClass("selected");
			});
		});
	</script>
	<script src="js/aes.js"></script>
	<script src="js/send.js"></script>

	<div class="test"></div>

</body>
</html>
"""

print(html)