import machine
import time

# Configura el LED incorporado (normalmente el GPIO 2 en muchos ESP32)
led = machine.Pin(2, machine.Pin.OUT)

def led_blink():
    for i in range(5):  # Parpadeo del LED 5 veces
        led.on()
        print("Funciona OTA vers 65 EQUIPO DE Caro, Luis y Fany")
        time.sleep(2)
        led.off()
        time.sleep(2)

# Llama a la función para comenzar el parpadeo del LED
led_blink()



