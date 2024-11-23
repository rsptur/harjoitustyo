import math
import random
from generator import PQgeneraattori
from primet import Primet

class Keys: 
    """
    luokka generoi julkisen ja yksityisen avaimen
    """
    def publickey():
        prime1,prime2=PQgeneraattori.generaattori()
        n = prime1 * prime2
        t = (prime1 - 1) * (prime2 - 1)
        while True:
            e = random.randint(2,t-1)
            if math.gcd(e, t) == 1:
                tulos=Primet.MillerRabintesti(e) 
                if tulos==True:
                    break   
        return e, n, t
    
    def privatekey(e,t):
        j = 2
        while True:
            if (j * e) % t == 1:
                d = j
                break
            j += 1
        return d



