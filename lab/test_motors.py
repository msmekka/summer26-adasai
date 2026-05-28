import sys
sys.path.insert(0, '/home/pi/lab')
import motors
import time
import signal

def cleanup(sig=None, frame=None):
    motors.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)

print("Setting up...")
motors.setup()

print("Forward 2 seconds...")
motors.forward(40)
time.sleep(2)

print("Brake...")
motors.brake()
time.sleep(1)

print("Turn left 1 second...")
motors.turn_left(40)
time.sleep(1)

print("Brake...")
motors.brake()
time.sleep(1)

print("Turn right 1 second...")
motors.turn_right(40)
time.sleep(1)

print("Brake...")
motors.brake()
time.sleep(1)

print("Done.")
motors.cleanup()
