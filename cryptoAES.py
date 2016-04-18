import os

from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)

class cryptoAES:
    #lorsque l'on créé un objet dans le but de décrypter le message,
    #il est necessaire de fournir le même iv que lors de l'encryption.
    def __init__(key, message, iv=os.urandom(12)):
        self.key=key
        self.message=message
        self.iv=iv
        self.associated_data=b"authenticated but not encrypted payload"

        
    def encrypt():
        #constitution de l'encrypteur
        AES = algorithms.AES(key)
        cipher=Cipher(AES,modes.GCM(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()

        #informations utiles pour la décryption
        encryptor.authenticate_additional_data(self.associated_data)

        # Encryption
        ciphertext = encryptor.update(self.message) + encryptor.finalize()

        return (self.iv, ciphertext, encryptor.tag)

    def decrypt(tag):
        #constitution du decrypteur
        AES = algorithms.AES(this.key)
        cipher = Cipher(AES,modes.GCM(this.iv, tag),backend=default_backend())
        decryptor = cipher.decryptor()

        # on aplique les infos donné dans l'encryption
        decryptor.authenticate_additional_data(associated_data)

        # Decryption
        # InvalidTag exception si le tag ne correspond pas
        return decryptor.update(this.message) + decryptor.finalize()

