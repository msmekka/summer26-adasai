import RPi.GPIO as GPIO
import time
import signal
import sys

# Pin definitions (BCM numbering)
VERTICAL = 11       # wiringPi 14 - up/down
HORIZONTAL = 9    # wiringPi 13 - left/right

# Servo center position
CENTER = 90

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(VERTICAL, GPIO.OUT)
    GPIO.setup(HORIZONTAL, GPIO.OUT)
    
    global pwm_vertical, pwm_horizontal
    pwm_vertical = GPIO.PWM(VERTICAL, 50)      # 50Hz PWM
    pwm_horizontal = GPIO.PWM(HORIZONTAL, 50)  # 50Hz PWM
    pwm_vertical.start(0)
    pwm_horizontal.start(0)

def angle_to_duty(angle):
    # Convert angle (0-180) to duty cycle (2.5-12.5)
    return 2.5 + (angle / 180.0) * 10.0

def move_to(pwm, angle):
    duty = angle_to_duty(angle)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.8)
    pwm.ChangeDutyCycle(0)  # stop signal to prevent jitter

def cleanup(sig=None, frame=None):
    print("\nCleaning up...")
    pwm_vertical.stop()
    pwm_horizontal.stop()
    GPIO.cleanup()
    sys.exit(0)

def main():
    setup()
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    print("Centering servos...")
    move_to(pwm_vertical, CENTER)
    move_to(pwm_horizontal, CENTER)
    time.sleep(1)

    print("Sweeping horizontal left...")
    move_to(pwm_horizontal, 160)
    time.sleep(0.5)

    print("Sweeping horizontal right...")
    move_to(pwm_horizontal, 20)
    time.sleep(0.5)

    print("Centering horizontal...")
    move_to(pwm_horizontal, CENTER)
    time.sleep(0.5)

    print("Sweeping vertical up...")
    move_to(pwm_vertical, 150)
    time.sleep(0.5)

    print("Sweeping vertical down...")
    move_to(pwm_vertical, 60)
    time.sleep(0.5)

    print("Centering vertical...")
    move_to(pwm_vertical, CENTER)
    time.sleep(0.5)

    print("Done. Ctrl+C to exit.")
    signal.pause()

if __name__ == "__main__":
    main()
