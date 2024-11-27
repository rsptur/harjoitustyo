from encrypt import Encryption
from decrypt import Decryption

#Ohjelman käyttöliittymä  

if __name__ == '__main__':
    print("Valitse")
    print("1. Salaa viesti")
    print("2. Pura viesti")
    valinta=input("Syötä numero:")
    try: 
        valinta=int(valinta)
        if valinta==1: 
            message1=input("Salattava viesti:" )
            tulos1 = Encryption.encoder(message1)
            print(tulos1)
        elif valinta==2: 
            message2=input("Purettava viesti:" )
            tulos2 = Decryption.decoder(message2)
            print(tulos2)        
    except ValueError: 
        print("Et syöttänyt numeroa")
        if valinta==1: 
            tulos1 = Encryption.encoder(message1)
            print(tulos1)
