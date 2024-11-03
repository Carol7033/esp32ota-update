from machine import Pin
import time

# Definimos el LED integrado (en el pin 2 en la mayoría de los ESP32)
led = Pin(2, Pin.OUT)

# Encendemos y apagamos el LED con una pausa de 1 segundo
while True:
    led.on()
    time.sleep(2)
    led.off()
    time.sleep(2)
