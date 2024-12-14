from keys import Keys


class Encryption:
    """
    luokka salaa viestin
    """
    def encrypt(m, p, nn):
        eletter = (m**p) % nn
        return eletter

    def encoder(message, jkey, tul):
        encoded = []
        for letter in message:
            encoded.append(Encryption.encrypt(ord(letter), jkey, tul))
        return encoded
