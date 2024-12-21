class Primetlista():
    """
    luokka generoi pienten alkulukujen listan - Sieve of Eratosthenes
    """
    def lista():
        lst = []
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
        return lst
