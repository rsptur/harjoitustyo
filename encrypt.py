from keys import Keys

class Encryption:
    """
    luokka salaa viestin
    """
    def encrypt(message):
        public,n,t=Keys.publickey()
        eletter=(message**public)%n
        return eletter

    def encoder(message):
        encoded = []
        for letter in message:
            encoded.append(Encryption.encrypt(ord(letter)))
        return encoded