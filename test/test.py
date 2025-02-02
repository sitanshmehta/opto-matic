import serial
import time

ARDUINO_PORT = "/dev/cu.usbmodem11401"  
BAUD_RATE = 9600

try:
    arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Allow time for connection

    while True:
        command = input("Enter 'START' to run motor, 'STOP' to stop motor: ").strip().upper()
        
        if command in ["START", "STOP"]:
            arduino.write(f"{command}\n".encode())  # Send command to Arduino
            print(f"Sent: {command}")
        else:
            print("Invalid command. Type 'START' or 'STOP'.")

except serial.SerialException as e:
    print(f"Error connecting to Arduino: {e}")

finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
