# Obiettivo del progetto

Il dispositivo M5stickC ogni mezzora legge umidità e temperatura rilevati attraverso il sensore ht11. I valori di temperatura e umidità rilevati e il livello di tensione corrente della batteria dell'm5stickc vengono memorizzati localmente.
Premendo il tasto m5, si visualizzano i valori. 


Tenendo premuto il tasto m5 per tre secondi, il servo ruota di 90 gradi; ripremendolo per altri tre secondi, il servo ruota di -90 gradi. 
Se la temperatura supera i 60°C o l'umidità il 70%, il servo ruota di 90 gradi.

# PASSO 1 - Collegamento del sensore e lettura dei valori
#### M5stickc - DHT11
La connessione tra m5stickc e il sensore di temparatura è molto semplice

m5stickc | dht11 (con restistenza di pullup)
------------ | -------------
G26 | HT11 pin 1 
3v3 | DHT11 pin 2 (VCC) 
GND | DHT11 pin 3 (GND) 
