from keys import Keys


class Encryption:
    """
    luokka salaa viestin
    """
    def encrypt(m, p, nn):
        # eletter = (letter**publickey) % (primes p*q)
        eletter = pow(m, p, nn)
        return eletter

    def encoder(message, jkey, tul):
        m = message.encode()
        m = int.from_bytes(m, "big")
        encoded = Encryption.encrypt(m, jkey, tul)
        return encoded
