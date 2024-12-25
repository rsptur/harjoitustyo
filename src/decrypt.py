from keys import Keys


class Decryption:
    """
    luokka purkaa salauksen
    """
    def decrypt(encrypted, private, n):
        # dletter = (number**privatekey) % (primes p*q)
        dletter = pow(encrypted, private, n)
        return dletter

    def decoder(encoded, private, n):
        d = Decryption.decrypt(encoded, private, n)
        s = (d.bit_length()+7//8)
        dec = d.to_bytes(s, byteorder='big')
        decoded = dec.decode().strip('\x00')
        return decoded
