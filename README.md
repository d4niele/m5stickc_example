## Obiettivo: uso M5stickC per lettura valori temperatura/umidità e controllo servo

Il dispositivo M5stickC ogni mezzora legge umidità e temperatura rilevati attraverso il sensore ht11. I valori di temperatura e umidità rilevati e il livello di tensione corrente della batteria dell'm5stickc vengono memorizzati localmente.
Premendo il tasto m5, si visualizzano i valori. 


Tenendo premuto il tasto m5 per tre secondi, il servo ruota di 90 gradi; ripremendolo per altri tre secondi, il servo ruota di -90 gradi. 
Se la temperatura supera i 60°C o l'umidità il 70%, il servo ruota di 90 gradi.

## 1.Collegamento del sensore e lettura dei valori
La connessione tra m5stickc e sensore di temparatura è molto semplice. Si presume di usare il sensore dht11 già provvisto di resistanza di pull-up.

m5stickc | dht11 (con restistenza di pullup)
------------ | -------------
G26 | pin 1 
3v3 | pin 2 (VCC) 
GND | pin 3 (GND) 

Per la lettura dei valori di temperatura e umidità si può usare la libreria builtin dht: https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html
```python
import dht
import machine
d = dht.DHT11(machine.Pin(26))
d.measure()
d.temperature()
d.humidity()
```
La lettura cadenzata può essere fatta gestendo il deep sleep. Es. https://community.m5stack.com/topic/2874/deep-sleep-with-micropython
