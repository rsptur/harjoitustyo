from encrypt import Encryption
from decrypt import Decryption
from keys import Keys
import sys

#Ohjelman käyttöliittymä  

if __name__ == '__main__':
    print("Valitse")
    print("1. Salaa viesti")
    print("2. Pura viesti")
    print("3. Tee avaimet")
    print("4. Lopeta")
    jatka=True
    while jatka==True: 
        valinta=input("Syötä numero:")
        oikea=False
        while not oikea:
            try: 
                valinta=int(valinta) 
                oikea=True   
            except ValueError: 
                print("Et syöttänyt numeroa")
                break
            if valinta==1: 
                message1=input("Salattava viesti:" )
                javain=int(input("Anna julkinen avain:" ))
                tulo=int(input("Anna alkulukujen tulo: " ))
                tulos1 = Encryption.encoder(message1,javain, tulo)
                print(tulos1)      
            elif valinta==2: 
                message2=input("Purettava viesti:" )
                tulo=int(input("Anna alkulukujen tulo: " ))
                yavain=int(input("Anna yksityinen avain:" ))
                tulos2 = Decryption.decoder(message2, yavain, tulo)
                print(tulos2)
            elif valinta==3: 
                Keys.publickey()
            elif valinta==4: 
                jatka=False    