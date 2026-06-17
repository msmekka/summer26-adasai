# summer26-adasai

Teaching AI for ADAS/AD using the Yahboom G1 Tank on a Raspberry Pi.

This repo is intended to be used alongside the Yahboom-provided Raspberry Pi image and software. See the official Yahboom G1 Tank resource page for the image, original software, and documentation: [...]

```
              ┌──────[camera]──────┐
              │     pan / tilt     │
┌─────────────┴────────────────────┴─────────────┐
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
│▓ ┌─────────────────────────────────────────┐  ▓│
│▓ │             Raspberry Pi                │  ▓│
│▓ │  ┌────────────┐     ┌────────────┐      │  ▓│
│▓ │  │  motor L   │     │  motor R   │      │  ▓│
│▓ │  └────────────┘     └────────────┘      │  ▓│
│▓ └─────────────────────────────────────────┘  ▓│
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
└──────────────┬──────────────────┬──────────────┘
               │    [RGB LED]     │
               │  ))) ultrasonic  │
               └──────────────────┘
                ▲   ▲          ▲   ▲
               IR1  IR2       IR3  IR4
           ── infrared line sensors (4×) ──
```

## Repository layout

```
lab/              Python motor library and lab notebooks
  00_concepts/    Conceptual intro to ADAS/AD
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

### `ai_driver.py`
Thin client for an instructor-hosted [Ollama](https://ollama.com) server running `phi3:mini`. Provides two functions used in the AI decision labs:

| Function | Description |
|---|---|
| `ask(prompt)` | POST a raw prompt to the Ollama `/api/generate` endpoint and return the response text |
| `decide(observation)` | Wraps `ask` with a robot-brain system prompt; given a natural-language observation, returns one of `FORWARD`, `LEFT`, `RIGHT`, or `STOP` |

Configure `OLLAMA_HOST` at the top of the file to the IP address provided by the instructor before use.

### `00_concepts/` notebooks
- `00_what_is_adas.ipynb` — Conceptual introduction to Advanced Driver-Assistance Systems (ADAS) and autonomous driving. Covers the sensor stack (cameras, radar, lidar, ultrasonic), the percepti[...]

### `01_hardware/` notebooks
Guided Jupyter labs covering:
- `01_led_control.ipynb` — GPIO LED control
- `02_motor_control.ipynb` — Motor control using `motors.py`
- `03_pantilt_control.ipynb` — Pan-tilt servo control

### `02_vision/` notebooks
- `04_camera_basics.ipynb` — Introduction to camera perception for ADAS. Covers opening a camera with OpenCV, inspecting individual pixel BGR values, streaming a live feed with an FPS counter, a[...]
- `05_color_detection.ipynb` — HSV-based color detection. Students define per-color lower/upper HSV bounds, build a binary mask via `cv2.inRange`, extract contours to find the largest matching b[...]
- `06_color_following.ipynb` — Closes the full perception → decision → action loop. Combines the color detector from Notebook 05 with `motors.py` to drive the tank toward a colored target in[...]

---

## `mypython/` — Standalone Python scripts

> Adapted from Yahboom's original G1 Tank software and tweaked for the camp curriculum.

### `pantilt_test.py`
Sweeps the pan-tilt camera mount through a sequence (center → left → right → center → up → down → center) using 50 Hz PWM on BCM pins 11 (vertical) and 9 (horizontal). Handles `SIGINT`[...]

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

### Raspberry Pi 4B GPIO Pin Map

```
 +-----+-----+---------+------+---+---Pi 4B--+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |  OUT | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT0 | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | ALT0 | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 1 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |  OUT | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |  OUT | 0 | 15 || 16 | 0 | OUT  | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | OUT  | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |  OUT | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |  OUT | 0 | 23 || 24 | 1 | OUT  | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 0 | 27 || 28 | 0 | OUT  | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |  OUT | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |  OUT | 0 | 35 || 36 | 0 | OUT  | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | OUT  | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | OUT  | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 4B--+---+------+---------+-----+-----+
```

**Legend:**
- **BCM**: Broadcom (GPIO) pin number
- **wPi**: wiringPi pin number
- **Mode**: GPIO function (IN = input, OUT = output, ALT0 = alternate function)
- **V**: Voltage state
- **Physical**: Physical pin number on the header

## Requirements

- Raspberry Pi with `wiringPi` installed (C programs)
- `RPi.GPIO` and `jupyter` (Python lab)
- Yahboom G1 Tank hardware

## Running the C programs

```bash
gcc -o CarRun CarRun.c -lwiringPi && sudo ./CarRun
```
