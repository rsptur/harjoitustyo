import random
import math
from primetlista import Primetlista

class Primet(): 
    """
    luokka testaa alkuluvut
    """
    def pienetprimet(n):            
        lst=Primetlista.lista()
        while True:
            l = random.randrange(2**(n-1)+1, 2**n - 1)
            for jakaja in lst:
                if l % 2 != 0 and l % jakaja == 0 and jakaja**2 <= l:
                    break
            else:
                return l

    def MillerRabintesti(m):
        kaksijakaja = 0
        e = m-1
        while e % 2 == 0:
            e >>= 1
            kaksijakaja += 1
        assert(2**kaksijakaja * e == m-1)
        def iterointi(testit):
            if pow(testit, e, m) == 1:
                return False
            for i in range(kaksijakaja):
                if pow(testit, 2**i * e, m) == m-1:
                    return False
            return True
        testiluku = 20
        for i in range(testiluku):
            testit = random.randrange(2, m)
            if iterointi(testit):
                return False
        return True