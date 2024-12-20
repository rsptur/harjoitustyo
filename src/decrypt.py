from keys import Keys


class Decryption:
    """
    luokka purkaa salauksen
    """
    def decrypt(encrypted, private, n):
        encrypted = int(encrypted)
        #dletter = (number**privatekey) % (primes p*q)   
        dletter =pow(encrypted,private,n)
        return dletter

    def decoder(encoded, private, n):
        decoded = ''
        encoded = str(encoded)
        encoded = encoded[1:-1]
        res = [int(ele) for ele in encoded.split(",")]
        for m in res:
            decoded += chr(Decryption.decrypt(m, private, n))
        return decoded
