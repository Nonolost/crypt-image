// fonction qui va vérifier que les conditions sont bonnes (champs remplis et correct) lorsqu'on veut cacher du texte
function preparerEnvoieEncrypt() {
	var fichier = $('#encrypt-fichier').val();
	if(fichier === '' && !$('.selected')[0]) {
		alert("Il faut sélectionner une image ici ou nous en envoyer une !");
		return;
	}

	var message = $('#encrypt-message').val();
	if(message === '') {
		alert("Il faut entrer un message");
		return;
	}

	var mdp = $('#encrypt-mdp').val();
	if(mdp === '') {
		alert("Il faut entrer un mot de passe.");
		return;
	}
	else if (mdp.length < 5) {
		alert("Il faut entrer un mot de passe d'au moins 6 caractères, pour la sécurité.")
		return;
	}

	if(!$('.selected')[0] && analyseFichier(fichier)) {
		alert("Le fichier que tu as fourni n'a pas l'air valide, il faut fournir une image de format non compressé.");
		return;
	}

	if(analyseMessage(message)) {
		alert("Petit filou, ton message ne passe pas notre filtre !")
		return;
	}

	if($('#encrypt-fichier').prop('files')[1]) {
		alert("Hop hop hop, qu'un seul fichier petit !");
		return;
	}

	var encrypted = CryptoJS.AES.encrypt(message, mdp);
	var formData = new FormData();

	formData.append('nom',fichier);
	formData.append('mess',encrypted);

	if(!$('.selected')[0]) {
		formData.append('new',1);
		formData.append('image',$('#encrypt-fichier')[0].files[0]);
	}
	else {
		formData.append('new',0);
		formData.append('image',$('.selected').find('.imgBB')[0].src);
	}
	
	$.ajax({
		type: 'POST',
		url: 'encrypt.py',
		data: formData,
		contentType: false,
		cache: false,
		processData: false,
		async: true,
		success: function(data) {
		    $('#result').html(data);
		},
	});
}

function preparerEnvoieDecrypt() {
	var fichier = $('#decrypt-fichier').val();
	if(fichier === '') {
		alert("Il faut sélectionner une image ici ou nous en envoyer une !");
		return;
	}

	var mdp = $('#decrypt-mdp').val();
	if(mdp === '') {
		alert("Il faut entrer un mot de passe.");
		return;
	}
	else if (mdp.length < 5) {
		alert("Il faut entrer un mot de passe d'au moins 6 caractères, pour la sécurité.")
		return;
	}

	if(analyseFichier(fichier)) {
		alert("Le fichier que tu as fourni n'a pas l'air valide, il faut fournir une image de format non compressé.");
		return;
	}

	if($('#decrypt-fichier').prop('files')[1]) {
		alert("Hop hop hop, qu'un seul fichier petit !");
		return;
	}

	var formData = new FormData();

	formData.append('image',$('#decrypt-fichier')[0].files[0]);
	formData.append('nom',fichier);

	$.ajax({
	    type: 'POST',
	    url: 'decrypt.py',
	    data: formData,
	    contentType: false,
	    cache: false,
	    processData: false,
	    async: true,
	    success: function(data) {
	        $('.test').html(data);
	        var result = $('.result').text();
	        $('.test').html("");

	        var decode = CryptoJS.AES.decrypt(result, mdp).toString(CryptoJS.enc.Utf8);

	        if (decode === "") {
	        	$('#result').html('<div class="alert alert-danger">Petit filou, c\'est pas le bon mot de passe !</div>');
	        }
	        else {
	        	$('#result').html('<div class="alert alert-success"><h3>Psss, j\'ai un secret pour toi ...</h3><p>'+decode+'</p></div>');
	        }
	    },
	});
}

// fonction qui sert de filtre pour contrer l'injonction xss
function analyseMessage (message) {
	return (/^.*<[sS][cC][rR][iI][pP][tT]>.*<\/[sS][cC][rR][iI][pP][tT]>.*$/.test(message) 
	|| /^.*[aA][lL][eE][rR][tT](.*).*$/.test(message)
	|| /^.*[sS][rR][cC]=.*\.[jJ][sS].*$/.test(message)
	|| /^.*[iI][fF][rR][aA][mM][eE].*$/.test(message));
}

// on vérifie que le fichier a un format correct
function analyseFichier (fichier) {
	var res = fichier.split(".");

	var ext = ["png","bmp","tif","tiff"];

	return (ext.indexOf(res[res.length-1]) < 0);
}