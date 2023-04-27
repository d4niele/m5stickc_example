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

## Limitazione consumo di corrente
La lettura cadenzata può essere fatta gestendo il deep sleep. Es. https://community.m5stack.com/topic/2874/deep-sleep-with-micropython

Per mettere l'M5StickC in deep sleep puoi utilizzare la seguente istruzione:

```python
machine.deepsleep()
```

Questa istruzione metterà il dispositivo in sleep mode, riducendo il consumo di energia. Per impostare il tempo di sleep puoi utilizzare il parametro `time` della funzione `deepsleep`. Ad esempio, per impostare il sleep per 30 minuti (1800 secondi), puoi utilizzare la seguente istruzione:

```python
machine.deepsleep(1800000)
```

Per far risvegliare il dispositivo dopo il tempo impostato o dopo aver premuto il tasto M5, puoi utilizzare la funzione `deepsleep_wake_trigger` del modulo `esp`. Questa funzione accetta come parametro una maschera di bit che specifica il trigger per il risveglio. Ad esempio, per far risvegliare il dispositivo sia dopo il tempo impostato che dopo aver premuto il tasto M5, puoi utilizzare la seguente istruzione:


```python
import esp
esp.deepsleep_wake_trigger(esp.DEEPSLEEP_WAKEUP_ALL_LOW |esp.DEEPSLEEP_WAKEUP_EXT0)
```

In questo modo il dispositivo si sveglierà sia quando il pin di trigger sarà basso (ovvero dopo il tempo impostato) che quando il pin `EXT0` (corrispondente al tasto M5) sarà premuto.

Ecco un esempio di codice che mette l'M5StickC in deep sleep e lo fa risvegliare dopo 30 minuti:

```python
import machine
import esp
from m5stack import btnA
from m5stack import axp192

# Imposta il tempo di sleep a 30 minuti
sleep_time = 1800000

# Imposta i trigger per il risveglio
esp.deepsleep_wake_trigger(esp.DEEPSLEEP_WAKEUP_ALL_LOW | esp.DEEPSLEEP_WAKEUP_EXT0)

# Funzione per gestire la pressione del tasto M5
def buttonA_wasPressed():
    pass

# Imposta la callback per la pressione del tasto M5
btnA.wasPressed(buttonA_wasPressed)

# Stampa un messaggio di debug
print('Entering deep sleep')

# Disabilita i regolatori di tensione LDO2 e LDO3
axp192.setLDO2State(False)
axp192.setLDO3State(False)
# Mette l'M5StickC in sleep mode per il tempo impostato
machine.deepsleep(sleep_time)
```

Questo codice farà entrare l'M5StickC in deep sleep e lo farà risvegliare dopo 30 minuti o dopo aver premuto il tasto M5. Quando il tasto M5 viene premuto, il trigger di risveglio viene resettato e il dispositivo viene messo in sleep mode.
Le istruzioni `axp.setLDO2State(False)` e `axp.setLDO3State(False)` consentono di disabilitare i regolatori di tensione LDO2 e LDO3 dell'AXP192, il chip di gestione dell'alimentazione presente sull'M5StickC. Questo può ridurre il consumo di corrente del dispositivo quando questi regolatori non sono necessari.

Tuttavia, è importante notare che disabilitare questi regolatori di tensione potrebbe causare problemi con alcuni componenti dell'M5StickC, come ad esempio il display LCD o la fotocamera. Inoltre, se si disabilitano questi regolatori, il dispositivo potrebbe non funzionare correttamente se viene alimentato con una tensione inferiore a quella necessaria per alimentare direttamente i componenti.

Quindi, se si decide di disabilitare i regolatori di tensione LDO2 e LDO3, è importante prestare attenzione alle specifiche dei componenti dell'M5StickC e alle condizioni di alimentazione per assicurarsi che il dispositivo funzioni correttamente. In alternativa, si potrebbe considerare l'utilizzo di altre tecniche per ridurre il consumo di corrente, come ad esempio la messa in sleep mode dei componenti non utilizzati o la riduzione della frequenza di clock del microcontrollore.

Seguono tre esempi di codice che utilizzano le tecniche descritte in precedenza per ridurre il consumo di corrente dell'M5StickC:

1. Utilizzo della modalità sleep:

```python
import machine

# Inserire qui il codice principale

# Mette l'M5StickC in modalità sleep per 30 secondi
machine.sleep(30000)

# Riprende l'esecuzione del codice
print('Wake up!')
```

In questo esempio, l'M5StickC entra in modalità sleep per 30 secondi utilizzando l'istruzione `machine.sleep(30000)`. Successivamente, l'esecuzione del codice riprende e viene stampato il messaggio "Wake up!".

2. Disattivazione di componenti non utilizzati:

```python
from m5stack import lcd, imu

# Inizializza il display LCD e il sensore di movimento
lcd.init()
imu.init()

# Disattiva il sensore di movimento
imu.power(False)

# Inserire qui il codice principale

# Disattiva il display LCD
lcd.clear()
lcd.poweroff()
```

In questo esempio, viene inizializzato il display LCD e il sensore di movimento utilizzando le istruzioni `lcd.init()` e `imu.init()`. Successivamente, viene disattivato il sensore di movimento utilizzando l'istruzione `imu.power(False)`, per poi disattivare il display LCD utilizzando l'istruzione `lcd.poweroff()`.

3. Riduzione della frequenza di clock:

```python
import machine

# Riduce la frequenza di clock a 80 MHz
machine.freq(80000000)

# Inserire qui il codice principale

# Ripristina la frequenza di clock originale
machine.freq(240000000)
```

In questo esempio, viene ridotta la frequenza di clock del microcontrollore a 80 MHz utilizzando l'istruzione `machine.freq(80000000)`. Successivamente, viene eseguito il codice principale, per poi ripristinare la frequenza di clock originale utilizzando l'istruzione `machine.freq(240000000)`.


Di seguito è riportato un esempio di codice per leggere il contatore di corrente dell'M5StickC utilizzando la libreria AXP:
```python
import axp202x

# Crea un oggetto axp202x
axp = axp202x.AXP202X()

# Inizializza l'oggetto axp
axp.init()

# Leggi il contatore di corrente
current = axp.read_current_cnt()

# Stampa il valore del contatore di corrente
print('Current = {}'.format(current))
```
Per sapere il valore corrente di carica della batteria, utilizza la funzione get_battery_charge_current() della libreria AXP. Di seguito è riportato un esempio di codice per leggere il valore corrente di carica della batteria:
```python
import axp202x

# Crea un oggetto axp202x
axp = axp202x.AXP202X()

# Inizializza l'oggetto axp
axp.init()

# Leggi il valore corrente di carica della batteria
charge_current = axp.get_battery_charge_current()

# Stampa il valore corrente di carica della batteria
print('Charge current = {} mA'.format(charge_current))
```
## Logging dei dati

Ecco un esempio di come utilizzare il modulo logging per il rotate logging in Micropython:

```python
import logging
import logging.handlers

# Configurazione del logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Rotazione del registro ogni giorno
handler = logging.handlers.TimedRotatingFileHandler('example.log', when='midnight', backupCount=7)
handler.setLevel(logging.DEBUG)

# Impostazione del formato di logging
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Aggiunta del gestore al logger
logger.addHandler(handler)

# Esempio di messaggio di logging
logger.debug('Questo è un messaggio di debug')
```

In questo esempio, utilizziamo la classe `TimedRotatingFileHandler` per ruotare il registro ogni mezzanotte e mantenere un massimo di 7 file di backup. Il resto della configurazione del logger è simile a quello che si farebbe in Python standard.
