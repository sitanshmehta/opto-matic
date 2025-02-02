import serial
import time
from eyeTracking import eyeTracker

ARDUINO_PORT = "COM5"  
BAUD_RATE = 9600

measurement = eyeTracker()
print(measurement,"FROM TEST")
# measurement = 30.62

try:
    arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Allow time for connection

    while True:
        command = input("Enter 'START' to start process: ").strip().upper()
        
        if command in ["START"]:
            arduino.write(f"{str(measurement)}\n".encode())  # Send command to Arduino
            print(f"Sent: {command}")
            break
        else:
            print("Invalid command. Type 'START'")
    while True:
        command = input("Enter 'LEFT' or 'RIGHT' to adjust: ").strip().upper()
        
        if command in ["LEFT","RIGHT"]:
            arduino.write(f"{command}\n".encode())  # Send command to Arduino
            print(f"Sent: {command}")
        else:
            print("Invalid command.")


except serial.SerialException as e:
    print(f"Error connecting to Arduino: {e}")

finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
