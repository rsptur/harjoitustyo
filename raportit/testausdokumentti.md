Testausdokumenttti

Yksikkötestaus:  

Testataan jokaista moduulia erikseen eri syötteillä

Testprimetlista testaa primetlista.py:ssä generoitavan lista pienistä alkuluvuista
Testprimet testaa primet.py:n Miller Rabinin algoritmin testaamalla tunnistaako se suuria alkulukuja
Testgenerator testaa generator.py:ssä generoitavat alkuluvut p & q:n Miller Rabin testillä
Testikeys testaa että keys.py:ssä generoitava julkinen avain on prime ja testaa että yksityinen x julkinen avain/ totientilla antaa vastaukseksi 1. 
Testiencrypt testaa salauksen toimivuutta annetuilla yksityisella ja julkisella avaimella sekä alkulukujen tulolla. 
Testidecrypt testaa salauksen toimivuutta annetuilla yksityisella ja julkisella avaimella sekä alkulukujen tulolla. 

Testikattavuus: 

![coverage](https://github.com/rsptur/harjoitustyo/tree/main/raportit/images/test_coverage.png)

Järjestelmätestaus: 

Sovellusta on testattu manuaalisesti. 