import random
import math

    lst=[]
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            lst.append(p)
    return lst

def bit(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)
 
def pieniprime(n):
    while True:
        p = bit(n)
        for jakaja in nrolst:
            if p % jakaja == 0 and jakaja**2 <= p:
                break
        else:
            return p
        
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

def generaattori(): 
    while True:
        n = 2048
        luku1 = pieniprime(n)
        if not MillerRabintesti(luku1):
            continue
        else:
            p=luku1
            break
    while True:
        n = 2048
        luku2 = pieniprime(n)
        if not MillerRabintesti(luku2):
            continue
        else:
            q=luku2
            break
    return p,q    
p,q=generaattori()

def publickey(prime1,prime2):
    n = prime1 * prime2
    t = (prime1 - 1) * (prime2 - 1)
    e = t-1
    while True:
        if math.gcd(e, t) == 1:
            tulos=MillerRabintesti(e) 
            if tulos==True:
                break
        e -= 1    
    return n,t,e
n,t,public=publickey(p,q)

def privatehelper(a, b):
    x, xx = 0, 1
    y, yy = 1, 0
    while (b != 0):
        osa = a // b
        a, b = b, a - osa * b
        xx, x = x, xx - osa * x
        yy, y = y, yy - osa * y
    return a, xx, yy

def privatekey(totient,publickey):
    g, x, y = privatehelper(publickey, totient)
    if (x < 0):
        d = x + totient
    else:
        d = x
    return d
private=privatekey(t,public)

def encrypt(message):
    global public, n
    eletter=(message**public)%n
    return eletter

def decrypt(encrypted):
    global private, n
    dletter=(encrypted**private)%n
    return dletter

def encoder(message,public,n):
    encoded = []
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded

def decoder(encoded,private,n):
    decoded= ''
    for m in encoded:
        decoded+=chr(decrypt(m))
    return decoded

if __name__ == '__main__':
    message="testing"
    tulos1 = encoder(message,public,n)
    print(tulos1)
    tulos2 = decoder(message,private,n)
    print(tulos2)