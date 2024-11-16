from encrypt import Encryption
from decrypt import Decryption

if __name__ == '__main__':
    message1=input("Syötä salattava viesti")
    message2=input("Syötä purettava viesti")
    tulos1 = Encryption().encoder(message1)
    print(tulos1)
    tulos2 = Decryption.decoder(message2)
    print(tulos2)