import math
from generator import PQgeneraattori
from primet import Primet

class Keys: 
    """
    luokka generoi julkisen ja yksityisen avaimen
    """
    def publickey():
        prime1,prime2=PQgeneraattori().generaattori()
        n = prime1 * prime2
        t = (prime1 - 1) * (prime2 - 1)
        e = t-1
        while True:
            if math.gcd(e, t) == 1:
                tulos=Primet().millerRabintesti(e) 
                if tulos==True:
                    break
            e -= 1    
        return e, n
  
    def privatekey(t,e):
        x, xx = 0, 1
        y, yy = 1, 0
        while (t != 0):
            osa = e // t
            e, t = t, e - osa * t
            xx, x = x, xx - osa * x
            yy, y = y, yy - osa * y
        if (xx < 0):
            d = xx + t
        else:
            d = xx
        return d    
    



