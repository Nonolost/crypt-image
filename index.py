# -*- coding: utf-8 -*-

import cgi 
from os import listdir
from os.path import isfile, join

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

#print(form.getvalue("name"))

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

#Premier
html+="""<div class="row"><form class="col-md-6 my-form form-left"> """

html+="""<h1>Cacher un message</h1>
<h3>Étape 1 : Sélectionner ou uploader une image</h3>
<p>Envoie-nous l'image que tu souhaites utiliser...</p>
<div class="input-group">
	<span class="input-group-btn">
		<span class="btn btn-primary btn-file">
		    Upload un fichier <input type="file">
		</span>
	</span>
	<input id="encrypt-img" type="text" class="form-control" readonly>

</div>
<br>
<p>... ou sélectionne une image parmis nos exemples disponibles !</p>

"""
pathToImg = "data/img/"
imgs = [f for f in listdir(pathToImg) if isfile(join(pathToImg, f))]

links = """<ul class="categories" class="clr">"""
for img in imgs:
	links+="""<li>
		      <div class="imgSelection" onclick="selectImg(this)">
		        <img src=""" + pathToImg + img + """ alt=""/>
		     </div>

		  </li>"""

links += """</ul>

"""

html+=links


html+="""<h3>Étape 2 : Entrer le message à cacher</h3>
<p>Écrit le message à cacher dans l'image.</p>
<div class="form-group">
	<textarea class="form-control" rows="5" id="message"></textarea>
</div>

"""

html+="""<h3>Étape 3 : Entrer le mot de passe</h3>
<p>Entre le mot de passe qui servira à crypter le message. Elle servira à récupérer le message à partir de l'image plus tard !</p>
<div class="form-group">
	<input type="password" class="form-control" id="encrypt-mdp">
</div>
<br>
<button type="button" class="btn btn-primary btn-lg center-block">Cache moi ça !</button>
</form>"""

html+="""<form class="col-md-6 my-form"><h1>Récupérer un message</h1>
<h3>Étape 1 : Uploader votre image</h3>
<p>Envoie nous l'image qui contient le message caché à récupérer.</p>
<div class="input-group">
	<span class="input-group-btn">
		<span class="btn btn-primary btn-file">
		    Upload un fichier <input type="file">
		</span>
	</span>
	<input id="decrypt-img" type="text" class="form-control" readonly>

</div>
"""

html+="""<h3>Étape 2 : Entrer la clé</h3>
<p>Écrit le mot de passe qui a servi à cacher le message initialement !</p>
<div class="form-group">
	<input type="password" class="form-control" id="decrypt-mdp">
</div>
<br>
<button type="button" class="btn btn-primary btn-lg center-block">Montre moi ça !</button>
</form>"""

html+="""	
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
		        $('#encrypt-img').val(label);
		        $("#selected-icon").remove();
		        $(".selected").removeClass("selected");
		    });
		});
	</script>
</body>
</html>
"""

print(html)
