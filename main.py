from m5stack import btnA,lcd
import machine,dht

sensor_dht = dht.DHT22(machine.Pin(26))
lcd.setRotation(1)
lcd.text(lcd.CENTER, 25, 'Premi M5')

def getValueDHT():
    sensor_dht.measure()
    return (sensor_dht.temperature(),sensor_dht.humidity())
    
def buttonA_wasPressed():
    global lcd
    print('press M5')
    v = getValueDHT()
    print(v)
    lcd.fill()
    lcd.text(lcd.CENTER, 25, 'TEMP: '+str(v[0]))
    lcd.text(lcd.CENTER, 45, 'UM: '+str(v[1]))
    return

btnA.wasPressed(buttonA_wasPressed)
print("start")
#while True:
#    pass