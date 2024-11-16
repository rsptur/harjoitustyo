from keys import Keys
class Decryption: 
    """
    luokka purkaa salauksen
    """
    def decrypt(encrypted):
        private,n=Keys().publickey()
        dletter=(encrypted**private)%n
        return dletter

    def decoder(encoded):
        decoded= ''
        for m in encoded:
            decoded+=chr(Decryption.decrypt(m))
        return decoded
