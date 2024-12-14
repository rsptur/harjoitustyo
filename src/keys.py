import math
import random
from generator import PQgeneraattori
from primet import Primet


class Keys:
    """
    luokka generoi julkisen ja yksityisen avaimen
    """

    def publickey():
        prime1, prime2 = PQgeneraattori.generaattori()
        n = prime1 * prime2
        t = (prime1 - 1) * (prime2 - 1)
        while True:
            e = random.randint(2, t-1)
            if math.gcd(e, t) == 1:
                tulos = Primet.MillerRabintesti(e)
                if tulos == True:
                    break
        print("Alkulukujen tulo")
        print(n)
        print("Julkinen avain")
        print(e)
        print("Yksityinen avain")
        print(Keys.privatekey(t, e))
        return e, n, t

    def privatehelper(a, b):
        x, xx = 0, 1
        y, yy = 1, 0
        while (b != 0):
            osa = a // b
            a, b = b, a - osa * b
            xx, x = x, xx - osa * x
            yy, y = y, yy - osa * y
        return a, xx, yy

    def privatekey(totient, publickey):
        g, x, y = Keys.privatehelper(publickey, totient)
        if (x < 0):
            d = x + totient
        else:
            d = x
        return d
