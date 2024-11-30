import unittest
from primetlista import Primetlista
from primet import Primet
from generator import PQgeneraattori
from keys import Keys
from decrypt import Decryption
from encrypt import Encryption

class Testprimetlista(unittest.TestCase):  
    """
    testaa primelistan
    """
    def testilista(self): 
        verrokki=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
        self.assertEqual(Primetlista.lista(), verrokki)

class Testprimet(unittest.TestCase):  
    """
    testaa alkulukujen testaus luokan
    """
    def testiprime(self): 
        isotprimet=[662184036900686266043305387651,107269498754639459686153895261,
                    466970157734318698514208954263,631379121341522939869949517061]
        for i in isotprimet:   
            self.assertEqual(Primet.MillerRabintesti(i), True)

class Testgenerator(unittest.TestCase):  
    """
    testaa generoidut alkuluvut
    """
    def testigeneraattori(self): 
        p,q=PQgeneraattori.generaattori()
        self.assertEqual(Primet.MillerRabintesti(p), True)
        self.assertEqual(Primet.MillerRabintesti(q), True)

class Testkeys(unittest.TestCase):  
    """
    testaa julkisen ja yksityisen avaimen
    """
    def testikeys(self): 
        public, tulo, totient= Keys.publickey()
        private= Keys.privatekey(totient,public)
        self.assertEqual(Primet.MillerRabintesti(public), True)
        self.assertTrue((private*public)%totient==1)

class Testencrypt(unittest.TestCase):  
    """
    testaa viestin salauksen toiminnan
    """
    def testiencrypt(self): 
        viesti="testing"
        yksityinen=41
        julkinen=29
        tulo=133
        salattu=Encryption.encoder(viesti,julkinen,tulo)
        salattu=str(salattu)
        print(salattu)
        purettu=Decryption.decoder(salattu,yksityinen,tulo)
        purettu=str(purettu)
        print(purettu)
        self.assertTrue(viesti==purettu)

class Testdecrypt(unittest.TestCase):  
    """
    testaa viestin purun toiminnan
    """
    def testidecrypt(self): 
        viesti="second test"
        yksityinen=41
        julkinen=29
        tulo=133
        salattu=Encryption.encoder(viesti,julkinen,tulo)
        salattu=str(salattu)
        print(salattu)
        purettu=Decryption.decoder(salattu,yksityinen,tulo)
        purettu=str(purettu)
        print(purettu)
        self.assertTrue(viesti==purettu)

if __name__ == '__main__':
    unittest.main()