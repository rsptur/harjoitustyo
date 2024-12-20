class Primetlista():
    """
    luokka generoi pienten alkulukujen listan - Sieve of Eratosthenes
    """
    def lista():
        lst = []
        #tehdään lista jossa kaikki luvut merkitään ensin True
        prime = [True for i in range(500+1)]
        p = 2
        while (p * p <= 500):
            if (prime[p] == True):
                #merkataan kaikki luvut listassa jotka ovat jaollisia p:llä False
                for i in range(p * p, 500+1, p):
                    prime[i] = False
            p += 1
        #liitetään kaikki luvut jotka True listaan ja se sisältää kaikki alle 500 alkuluvut
        for p in range(2, 500+1):
            if prime[p]:
                lst.append(p)
        return lst
