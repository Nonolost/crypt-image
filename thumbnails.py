from PIL import Image
from os import listdir
from os.path import isfile, join

pathToImg = "data/img/"
imgs = [f for f in listdir(pathToImg) if isfile(join(pathToImg, f))]

pathToThumb = "data/img/thumbnails/"
thumbs = [f for f in listdir(pathToThumb) if isfile(join(pathToThumb, f))]

size = (120,120)
for img in imgs:
	if img not in thumbs:
		print pathToImg+img
		tmp = Image.open(pathToImg+img)
		tmp.thumbnail(size)
		tmp.save("data/img/thumbnails/%s" % (img))