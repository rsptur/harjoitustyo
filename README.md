# harjoitustyo

Ohjelmointikieli: Python

Projekti: Ohjelma joka salaa ja purkaa tekstiä. Ohjelma tulee salaamisen ja salauksen purkamisen lisäksi tuottamaan avaimia, joiden pituus on oikean RSA-salauksen tavoin vähintään 2048 bittiä. 

Käyttäjä voi antaa salattavaksi sen pituisen tekstin kuin avaimen pituus sallii. Ohjelma sisältää isojen alkulukujen etsimiseen ja avaimen muodostamiseen tarvittavat metodit, kuten Miller-Rabin algoritmin. 

Käynnistät ohjelman: 

Ensin asenna riippuvuudet

```
poetry install
```

Mene src valikkoon (cd src) ja käynnistä salausohjelma

```
poetry run python3 app.py
```

Suorita testit 

```
poetry run pytest
```
