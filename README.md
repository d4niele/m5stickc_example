Il dispositivo M5stickC ogni mezzora legge umidità e temperatura rilevati attraverso il sensore ht11. I valori di temperatura e umidità rilevati e il livello di tensione corrente della batteria dell'm5stickc vengono memorizzati localmente.
Premendo il tasto m5, si visualizzano i valori. 
--

Tenendo premuto il tasto m5 per tre secondi, il servo ruota di 90 gradi; ripremendolo per altri tre secondi, il servo ruota di -90 gradi. 
Se la temperatura supera i 60°C o l'umidità il 70%, il servo ruota di 90 gradi.

# Connessione tra m5stickc e dht11 (con restistenza di pullup)
Le connessioni sono molto semplici
DHT11 pin 1 (signal pin) :  G26 m5stick-C
DHT11 pin 2 (VCC) : 3v3 pin m5stick-C
DHT11 pin 3 (GND) : GND pin m5stick-C
