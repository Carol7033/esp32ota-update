import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # Ajusta el número de pin según tu conexión

while True:
    led.on()
    print("Caro, funciona OTA")  # Mensaje personalizado
    time.sleep(1)
    led.off()
    time.sleep(1)


