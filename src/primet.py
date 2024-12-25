import random
from primetlista import Primetlista


class Primet():
    """
    luokka testaa alkuluvut
    """
    def pienetprimet(n):
        lst = Primetlista.lista()
        while True:
            # muodostetaan tarpeeksi suuri luku
            l = random.randrange(2**(n-1)+1, 2**n - 1)
            for jakaja in lst:
                # testataan onko luku jaollinen pienillä primeillä
                if l % jakaja == 0 and jakaja**2 <= l:
                    break
            else:
                return l

    def MillerRabintesti(m):
        k = 0
        e = m-1
        while e % 2 == 0:
            e >>= 1
            k += 1

        def iterointi(t):
            if pow(t, e, m) == 1:
                return False
            for i in range(k):
                if pow(t, 2**i * e, m) == m-1:
                    return False
            return True

        luku = 20
        for i in range(luku):
            t = random.randrange(2, m)
            if iterointi(t):
                return False
        return True
