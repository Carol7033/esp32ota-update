import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # Ajusta el número de pin según tu conexión

while True:
    led.on()
    print("¡Actualización recibida Caro puedes editarme desde Github!")  # Mensaje que indica que se ha actualizado
    time.sleep(1)
    led.off()
    time.sleep(1)

