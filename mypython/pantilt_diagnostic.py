#!/usr/bin/env python3
"""
Pan/Tilt Diagnostic Script
NCSSM AI in Autonomous Driving Camp -- Summer 2026

Run this script on each kit before camp to determine which
pan/tilt notebook version to use.

Usage:
    python3 pantilt_diagnostic.py

Follow the prompts and answer y/n for each movement.
The script will tell you which notebook version to use.
"""

import RPi.GPIO as GPIO
import time
import sys

# ── Pin definitions ───────────────────────────────────────────
HORIZONTAL = 11   # original
VERTICAL   = 9    # original
# ─────────────────────────────────────────────────────────────

def angle_to_duty(angle):
    return 2.5 + (angle / 180.0) * 10.0

def move_to(pwm, angle, delay=0.8):
    angle = max(0, min(180, angle))
    pwm.ChangeDutyCycle(angle_to_duty(angle))
    time.sleep(delay)
    pwm.ChangeDutyCycle(0)

def pan(angle, delay=0.8):
    move_to(pwm_horizontal, angle, delay)

def tilt(angle, delay=0.8):
    move_to(pwm_vertical, angle, delay)

def center():
    pan(90)
    tilt(90)

def ask(question):
    while True:
        answer = input(f'\n  {question} (y/n): ').strip().lower()
        if answer in ('y', 'n'):
            return answer == 'y'
        print('  Please enter y or n.')

def cleanup():
    center()
    time.sleep(0.5)
    pwm_horizontal.stop()
    pwm_vertical.stop()
    GPIO.cleanup()

# ── Setup ─────────────────────────────────────────────────────
print()
print('=' * 50)
print('  Pan/Tilt Diagnostic -- NCSSM ADAS Camp 2026')
print('=' * 50)
print()
print('Setting up GPIO...')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(HORIZONTAL, GPIO.OUT)
GPIO.setup(VERTICAL,   GPIO.OUT)

pwm_horizontal = GPIO.PWM(HORIZONTAL, 50)
pwm_vertical   = GPIO.PWM(VERTICAL,   50)
pwm_horizontal.start(0)
pwm_vertical.start(0)
time.sleep(1.0)

print('Centering camera -- watch for smooth movement to center.')
center()

centered_ok = ask('Did the camera move smoothly to center (forward-facing)?')
if not centered_ok:
    print()
    print('  WARNING: Camera did not center cleanly.')
    print('  Check servo connectors and power before continuing.')
    cleanup()
    sys.exit(1)

# ── Test 1: Pan direction ─────────────────────────────────────
print()
print('-' * 50)
print('  TEST 1: Pan Direction')
print('-' * 50)

print('  Moving LEFT (pan 30)...')
pan(30)
time.sleep(0.3)
went_left = ask('Did the camera go LEFT?')

print('  Moving RIGHT (pan 150)...')
pan(150)
time.sleep(0.3)
went_right = ask('Did the camera go RIGHT?')

print('  Returning to center...')
pan(90)

pan_correct = went_left and went_right

# ── Test 2: Tilt direction ────────────────────────────────────
print()
print('-' * 50)
print('  TEST 2: Tilt Direction')
print('-' * 50)

print('  Moving UP (tilt 120)...')
tilt(120)
time.sleep(0.3)
went_up = ask('Did the camera go UP?')

print('  Moving DOWN (tilt 60)...')
tilt(60)
time.sleep(0.3)
went_down = ask('Did the camera go DOWN?')

print('  Returning to center...')
tilt(90)

tilt_correct = went_up and went_down

# ── Result ────────────────────────────────────────────────────
print()
print('=' * 50)
print('  RESULT')
print('=' * 50)

if pan_correct and tilt_correct:
    print()
    print('  All movements correct!')
    print()
    print('  >> Use: 03_pantilt_control.ipynb (original)')
    print()
elif not pan_correct and not tilt_correct:
    print()
    print('  Pan and tilt are both swapped.')
    print()
    print('  >> Use: 03_pantilt_control_swapped.ipynb')
    print()
elif not pan_correct:
    print()
    print('  Pan direction is wrong but tilt is correct.')
    print('  This is an unusual configuration -- flag for instructor.')
    print()
elif not tilt_correct:
    print()
    print('  Tilt direction is wrong but pan is correct.')
    print('  This is an unusual configuration -- flag for instructor.')
    print()

print('=' * 50)
print()

cleanup()
print('GPIO cleaned up. Done!')
print()
