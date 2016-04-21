# -*-coding:utf-8 -*-
# Script python qui implémente un algorithme de stéganographie modifiant la valeur du bit de poit faible de chaque pixel pour cacher un message ou le récupérer

from PIL import Image
from numpy import *
import random


class SteganoClass:

    def __init__(self, img, message):
        self.img = img
        self.message = message


    def bit_generator(self, mess):
        for ch in mess:
            ascii = ord(ch)
            ct = 0
            while ct < 7:
                b = ascii & 1
                yield ascii & 1
                ascii >>= 1
                ct += 1
        for i in range(7):
            yield 0
        while True:
            yield random.randrange(1)

    def setbit(self, oldbyte, newbit):
        if newbit:
            return oldbyte | newbit
        else:
            return oldbyte & 0b11111110

    # fonction permetant de cacher un message dans une image   
    def hide(self):
        bitstream = SteganoClass.bit_generator(self, self.message)
        wImg, hImg = self.img.size
        imgCrypted = self.img.copy()
        imgPix = imgCrypted.load()
        for row in range(hImg):
            for col in range(wImg):
                r, g, b = self.img.getpixel((col, row))

                redbit = bitstream.next()
                r = SteganoClass.setbit(self, r, redbit)

                greenbit = bitstream.next()
                g = SteganoClass.setbit(self, g, greenbit)

                bluebit = bitstream.next()
                b = SteganoClass.setbit(self, b, bluebit)

                imgPix[col, row] = (r, g, b)

        return imgCrypted

    def bitToInt(self, bit_list):
        output = 0
        for bit in bit_list:
            output = output * 2 + bit
        return output

    # fonction permettant de révéler le message caché dans une image
    def reveal(self):
        data = list(self.img.getdata())
        mess = []
        tempMess = []
        for pix in data:
            for i in range(3):
                ch = bin(pix[i])
                tempMess.append(int(ch[-1]))
                if tempMess.__len__() == 7:
                    tempMess.reverse()
                    lettInt = SteganoClass.bitToInt(self, tempMess)
                    if lettInt == 0:
                        return ''.join(map(str, mess))
                    letter = str(unichr(lettInt))
                    mess.append(letter)
                    tempMess = []
        strMess = ''.join(map(str, mess))
        return strMess

