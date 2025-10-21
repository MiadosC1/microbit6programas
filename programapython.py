import serial
import time

# 🔧 Cambia este puerto por el que use tu micro:bit
# En Windows suele ser COM3, COM4 o COM5
# En Linux/Mac suele ser /dev/ttyACM0 o /dev/ttyUSB0
puerto = "COM3"
baudrate = 115200

try:
    ser = serial.Serial(puerto, baudrate)
    print(f"Conectado a {puerto}")

    time.sleep(2)  # pequeña espera para estabilizar conexión

    while True:
        if ser.in_waiting > 0:
            linea = ser.readline().decode('utf-8').strip()
            print("Dato recibido:", linea)

except serial.SerialException:
    print("No se pudo conectar al micro:bit. Verifica el puerto.")
except KeyboardInterrupt:
    print("Conexión cerrada.")
    ser.close()
