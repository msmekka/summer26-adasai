import RPi.GPIO as GPIO
import time

# ── Pin definitions (BCM numbering) ──────────────────────────
LEFT_GO   = 20   # wiringPi 28 ✓
LEFT_BACK = 21   # wiringPi 29 ✓
LEFT_PWM  = 16   # wiringPi 27 ✓

RIGHT_GO   = 19  # wiringPi 24 ✓
RIGHT_BACK = 6   # wiringPi 25 
RIGHT_PWM  = 13  # wiringPi 23 ✓
# ── Default speed (0-100) ─────────────────────────────────────
DEFAULT_SPEED = 40

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in [LEFT_GO, LEFT_BACK, LEFT_PWM, RIGHT_GO, RIGHT_BACK, RIGHT_PWM]:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    global pwm_left, pwm_right
    pwm_left  = GPIO.PWM(LEFT_PWM,  100)
    pwm_right = GPIO.PWM(RIGHT_PWM, 100)
    pwm_left.start(0)
    pwm_right.start(0)

def forward(speed=DEFAULT_SPEED):
    GPIO.output(LEFT_GO,   GPIO.HIGH)
    GPIO.output(LEFT_BACK, GPIO.LOW)
    GPIO.output(RIGHT_GO,  GPIO.HIGH)
    GPIO.output(RIGHT_BACK,GPIO.LOW)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(speed)

def brake():
    GPIO.output(LEFT_GO,    GPIO.LOW)
    GPIO.output(LEFT_BACK,  GPIO.LOW)
    GPIO.output(RIGHT_GO,   GPIO.LOW)
    GPIO.output(RIGHT_BACK, GPIO.LOW)
    pwm_left.ChangeDutyCycle(0)
    pwm_right.ChangeDutyCycle(0)

def turn_left(speed=DEFAULT_SPEED):
    GPIO.output(LEFT_GO,    GPIO.LOW)
    GPIO.output(LEFT_BACK,  GPIO.LOW)
    GPIO.output(RIGHT_GO,   GPIO.HIGH)
    GPIO.output(RIGHT_BACK, GPIO.LOW)
    pwm_left.ChangeDutyCycle(0)
    pwm_right.ChangeDutyCycle(speed)

def turn_right(speed=DEFAULT_SPEED):
    GPIO.output(LEFT_GO,   GPIO.HIGH)
    GPIO.output(LEFT_BACK, GPIO.LOW)
    GPIO.output(RIGHT_GO,  GPIO.LOW)
    GPIO.output(RIGHT_BACK,GPIO.LOW)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(0)

def spin_left(speed=DEFAULT_SPEED):
    GPIO.output(LEFT_GO,    GPIO.LOW)
    GPIO.output(LEFT_BACK,  GPIO.HIGH)
    GPIO.output(RIGHT_GO,   GPIO.HIGH)
    GPIO.output(RIGHT_BACK, GPIO.LOW)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(speed)

def spin_right(speed=DEFAULT_SPEED):
    GPIO.output(LEFT_GO,   GPIO.HIGH)
    GPIO.output(LEFT_BACK, GPIO.LOW)
    GPIO.output(RIGHT_GO,  GPIO.LOW)
    GPIO.output(RIGHT_BACK,GPIO.HIGH)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(speed)

def cleanup():
    brake()
    pwm_left.stop()
    pwm_right.stop()
    GPIO.cleanup()
