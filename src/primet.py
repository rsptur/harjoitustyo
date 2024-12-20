import random
from primetlista import Primetlista


class Primet():
    """
    luokka testaa alkuluvut
    """
    def pienetprimet(n):
        lst = Primetlista.lista()
        while True:
            #muodostetaan tarpeeksi suuri luku
            l = random.randrange(2**(n-1)+1, 2**n - 1)
            for jakaja in lst:
                #testataan onko luku jaollinen pienillä primeillä
                if l % jakaja == 0 and jakaja**2 <= l:
                    break
            else:
                return l

    def MillerRabintesti(m):
        #jos iteroinnin jälkeen palauttaa False ei ole alkuluku
        #jos palauttaa True on alkuluku
        # 1. löydä m-1=(2**k)*e
        k = 0
        e = m-1
        # toista niin pitkään että ei jaollinen 2:lla
        while e % 2 == 0:
            #e/(2**1)
            e >>= 1
            k += 1

        def iterointi(t):
            #arvottiin luku t, 2 ja m:n välillä
            #testataan tuleeko t:n ja e:n tulon ja m jakojäännöksestä 1
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
