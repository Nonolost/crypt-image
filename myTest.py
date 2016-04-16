from SteganoClass import SteganoClass
from PIL import Image

lenaPure = Image.open('lena.png')
stegMess = 'je veux des bananes'
steg = SteganoClass(lenaPure, stegMess)

crypt = SteganoClass.hide(steg)
#crypt.show()

steg2 = SteganoClass(crypt, '')
hiddenMess = SteganoClass.reveal(steg2)
print (hiddenMess)




