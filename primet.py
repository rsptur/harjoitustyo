import random
import math

class Primet(): 
    """
    luokka testaa alkuluvut
    """
    def pienetprimet(n):
        lst=[]
        prime = [True for i in range(500+1)]
        p = 2
        while (p * p <= 500):
            if (prime[p] == True):
                for i in range(p * p, 500+1, p):
                    prime[i] = False
            p += 1
        for p in range(2, 500+1):
            if prime[p]:
                lst.append(p)        
        while True:
            p = random.randrange(2**(n-1)+1, 2**n - 1)
            for jakaja in lst:
                if p % jakaja == 0 and jakaja**2 <= p:
                    break
            else:
                return p       

    def millerRabintesti(m):
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