# summer26-adasai

Teaching AI for ADAS/AD using the Yahboom G1 Tank on a Raspberry Pi.

This repo is intended to be used alongside the Yahboom-provided Raspberry Pi image and software. See the official Yahboom G1 Tank resource page for the image, original software, and documentation: https://www.yahboom.net/study/G1-T-PI

## Repository layout

```
lab/              Python motor library and lab notebooks
  01_hardware/    GPIO, motors, and pan-tilt labs
  02_vision/      Camera and computer-vision labs
mypython/         Standalone Python scripts for hardware testing
mySmartCar/       C programs (wiringPi) from the Yahboom G1 kit
```

---

## `lab/` — Python hardware library and Jupyter labs

### `motors.py`
A reusable Python module for controlling the tank's drive motors via `RPi.GPIO` (BCM numbering).

| Function | Description |
|---|---|
| `setup()` | Configures GPIO pins and starts PWM on both motors |
| `forward(speed)` | Both motors forward at `speed` (0–100, default 40) |
| `brake()` | Stops both motors |
| `turn_left(speed)` | Right motor only — gentle left pivot |
| `turn_right(speed)` | Left motor only — gentle right pivot |
| `spin_left(speed)` | Left motor reverse, right forward — in-place left spin |
| `spin_right(speed)` | Left motor forward, right reverse — in-place right spin |
| `cleanup()` | Brakes and releases all GPIO resources |

Pin assignments (BCM): LEFT_GO=20, LEFT_BACK=21, LEFT_PWM=16, RIGHT_GO=19, RIGHT_BACK=6, RIGHT_PWM=13.

### `test_motors.py`
Smoke test for `motors.py`: drives forward 2 s, brakes, turns left 1 s, turns right 1 s, then cleans up. Handles `SIGINT` for safe Ctrl-C exit.

### `01_hardware/` notebooks
Guided Jupyter labs covering:
- `01_led_control.ipynb` — GPIO LED control
- `02_motor_control.ipynb` — Motor control using `motors.py`
- `03_pantilt_control.ipynb` — Pan-tilt servo control

### `02_vision/` notebooks
- `04_camera_basics.ipynb` — Introduction to camera perception for ADAS. Covers opening a camera with OpenCV, inspecting individual pixel BGR values, streaming a live feed with an FPS counter, and comparing color spaces (BGR, HSV, grayscale). Includes guided "Tweak Zone" experiments and an advanced challenge to locate the brightest pixel in a frame.

---

## `mypython/` — Standalone Python scripts

> Adapted from Yahboom's original G1 Tank software and tweaked for the camp curriculum.

### `pantilt_test.py`
Sweeps the pan-tilt camera mount through a sequence (center → left → right → center → up → down → center) using 50 Hz PWM on BCM pins 11 (vertical) and 9 (horizontal). Handles `SIGINT`/`SIGTERM` for clean shutdown.

---

## `mySmartCar/` — C programs (Yahboom G1 kit, wiringPi)

> Adapted from Yahboom's original G1 Tank software and tweaked for the camp curriculum.

All programs use `wiringPi` pin numbering and `softPwm` for motor speed control. Each compiles to a standalone binary. Pre-built binaries are included alongside the `.c` sources.

| File | Description |
|---|---|
| `advance.c` | Drive forward only |
| `CarRun.c` | Forward, reverse, left, right, spin — timed sequence demo |
| `KeyScanStart.c` | Press onboard button to start the motor sequence |
| `ColorLED.c` | Cycle through 7 RGB LED colors |
| `ServoControlCorlor.c` | Sweep front servo while cycling the RGB LED |
| `avoid_ultrasonic.c` | Ultrasonic obstacle avoidance — slows and spins away when an obstacle is detected within 55 cm |
| `servo_ultrasonic_avoid.c` | Obstacle avoidance with servo-mounted ultrasonic — scans left/right to pick the clearer direction |
| `tracking.c` | Line-following using 4 infrared track sensors |
| `bluetooth_control_tank.c` | Full-featured Bluetooth (serial) control: drive, servos, RGB LED, line-follow mode, obstacle-avoidance mode, LED color mode |
| `TCP_control_Route.c` | Same feature set as Bluetooth control but over a TCP socket (port 8888, IP 192.168.50.1) using pthreads for concurrent recv/send/servo threads |

### Pin map (wiringPi numbering)

| Signal | wiringPi pin |
|---|---|
| Left motor forward (AIN2) | 28 |
| Left motor reverse (AIN1) | 29 |
| Left motor PWM | 27 |
| Right motor forward (BIN2) | 24 |
| Right motor reverse (BIN1) | 25 |
| Right motor PWM | 23 |
| Ultrasonic Trig | 31 |
| Ultrasonic Echo | 30 |
| Track sensors (L1, L2, R1, R2) | 9, 21, 7, 1 |
| Front servo | 4 |
| Camera pan servo | 14 |
| Camera tilt servo | 13 |
| RGB LED (R, G, B) | 3, 2, 5 |
| Buzzer / button | 10 |

## Requirements

- Raspberry Pi with `wiringPi` installed (C programs)
- `RPi.GPIO` and `jupyter` (Python lab)
- Yahboom G1 Tank hardware

## Running the C programs

```bash
gcc -o CarRun CarRun.c -lwiringPi && sudo ./CarRun
```
