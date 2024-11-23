import random
import math
from primet import Primet

class PQgeneraattori(): 
    """
    luokka generoi alkuluvut salaukseen
    """
    def generaattori(): 
        while True:
            n = 2048
            luku1 = Primet.pienetprimet(n)
            if not Primet.MillerRabintesti(luku1):
                continue
            else:
                p=luku1
                break
        while True:
            n = 2048
            luku2 = Primet.pienetprimet(n)
            if not Primet.MillerRabintesti(luku2):
                continue
            else:
                q=luku2
                break
        return p,q
