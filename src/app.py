import sys
from encrypt import Encryption
from decrypt import Decryption
from keys import Keys

"""
Ohjelman käyttöliittymä  
"""
if __name__ == '__main__':
    jatka = True
    javain=None
    yavain=None
    while jatka == True:
        print("Valitse alla olevista vaihtoehtoista")
        #print("Jos sinulla ei ole salausavaimia, aloita valitsemalla 1")
        #print("Sinun on salattava viesti ennen sen purkamista")
        print("1. Tee avaimet")
        print("2. Salaa viesti")
        print("3. Pura viesti")
        print("4. Lopeta")
        valinta = input("Syötä numero: ")
        oikea = False
        while not oikea:
            try:
                valinta = int(valinta)
                oikea = True
            except ValueError:
                print("Et syöttänyt numeroa")
                break
            
            
            if valinta == 1:
                print("Muodostetaan avaimia...")
                Keys.publickey()


            elif valinta == 2:
                message1 = input("Kirjoita salattava viesti: ")
                while len(message1) < 1:
                    print("Et antanut salattavaa viestiä")
                    message1 = input("Kirjoita salattava viesti: ")
                def v_javain(): 
                    while True: 
                        try: 
                            javain = int(input("Anna julkinen avain: "))
                            return javain
                        except ValueError: 
                            print("Et syöttänyt numeroa")
                javain=v_javain()
                def v_tulo(): 
                    while True: 
                        try: 
                            javain = int(input("Anna alkulukujen tulo: "))
                            return javain
                        except ValueError: 
                            print("Et syöttänyt numeroa")
                tulo=v_tulo()
                print("Viestiä salataan...")
                tulos1 = Encryption.encoder(message1, javain, tulo)
                print("Salattu viesti: ",tulos1)


            elif valinta == 3:
                #if javain==None: 
                    #print("Sinun täytyy ensin salata viesti") 
                #else: 
                    def v_message(): 
                        while True: 
                            try: 
                                message = int(input("Anna purettava viesti: "))
                                return message
                            except ValueError: 
                                print("Et syöttänyt käypää viestiä")
                    #message2 = tulos1
                    def v_yavain(): 
                        while True: 
                            try: 
                                yavain = int(input("Anna yksityinen avain: "))
                                return yavain
                            except ValueError: 
                                print("Et syöttänyt numeroa")
                    yavain=v_yavain()
                    message2=v_message()
                    print("Viestiä puretaan... ")
                    tulos2 = Decryption.decoder(message2, yavain, tulo)
                    print("Purettu viesti: ",tulos2)
            
            elif valinta == 4:
                jatka = False
