import machine
import time

# Configura el LED incorporado (normalmente el GPIO 2 en muchos ESP32)
led = machine.Pin(2, machine.Pin.OUT)

def led_blink():
    while True:
        # Enciende el LED
        led.on()
        print("OTA FUNCIONA EQUIPO DE Caro,Luis y Fany")  # Mensaje en consola
        time.sleep(2)  # Mantiene el LED encendido durante 5 segundos

        # Apaga el LED
        led.off()
        time.sleep(2)  # Mantiene el LED apagado durante 3 segundos

# Llama a la función para comenzar el parpadeo del LED
led_blink()


