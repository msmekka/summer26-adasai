# Yahboom G1 Tank — Kit Test Checklist

*NCSSM Summer 2026 — ADAS AI Lab*

| Field | Value |
|---|---|
| Kit Number | |
| Date | |
| MAC Address | |
| IP Address | |

## Step 1: Pre-Test Setup

Before running any component tests complete these steps in order.

> **WARNING:** All motor and servo tests require a fully charged battery. Do NOT run CarRun, servo, or ultrasonic tests on USB power only — the Pi will brownout.

- [ ] Battery charged and connected — expansion board power switch OFF until ready
- [ ] Pi seated on expansion board GPIO header — pins aligned, no bent pins
- [ ] All 6-pin sensor cables seated — ultrasonic and line tracking
- [ ] USB camera connected — USB cable plugged into Pi
- [ ] WiFi dongle inserted — USB port on Pi
- [ ] SSH connection confirmed — `ssh pi@<ip>` — password: `yahboom`
- [ ] MAC address recorded — `ip link show wlan0 | grep ether`
- [ ] `lab` folder present — `ls ~/lab`
- [ ] `ncssmSmartCar` folder present — `ls ~/ncssmSmartCar`
- [ ] `ncssmpython` folder present — `ls ~/ncssmpython`
- [ ] mjpg_streamer disabled — `grep mjpg /etc/rc.local` — should be commented out

## Step 2: Compile SmartCar Programs

Compile all C programs before running tests. Run these commands from the `ncssmSmartCar` directory.

```bash
cd ~/ncssmSmartCar
gcc -o ColorLED ColorLED.c -lwiringPi -lpthread
gcc -o CarRun CarRun.c -lwiringPi -lpthread
gcc -o ServoControlCorlor ServoControlCorlor.c -lwiringPi -lpthread
gcc -o servo_ultrasonic_avoid servo_ultrasonic_avoid.c -lwiringPi -lpthread
gcc -o tracking tracking.c -lwiringPi -lpthread
```

- [ ] All 5 programs compile with no errors — warnings are ok, errors are not

## Step 3: Component Tests

Run each test in order. Use two SSH sessions — one to run the test, one to kill it if it hangs.

> **TIP:** To kill a stuck program from your second SSH session: `sudo pkill -9 -f <program_name>`

### Test 1: RGB LED

Safest test — no moving parts. Confirms expansion board is communicating with the Pi.

```bash
cd ~/ncssmSmartCar
sudo ./ColorLED
```

- [ ] LED flashes RGB colors — should cycle through red, green, blue combinations
- [ ] Ctrl+C exits cleanly — returns to prompt without crashing Pi

### Test 2: Motors (CarRun)

Place tank on floor with room to move, or flip upside down so tracks spin freely.

> **WARNING:** Battery must be charged and connected. Do not run on USB power only.

```bash
sudo ./CarRun
```

- [ ] Both tracks move — forward, backward, turns all work
- [ ] Left and right directions correct — left track turns left, right track turns right
- [ ] Ctrl+C exits cleanly — motors stop, returns to prompt

### Test 3: Front Servo + LED (ServoControlCorlor)

Tests the ultrasonic sensor servo sweep and RGB LED together.

```bash
sudo ./ServoControlCorlor
```

- [ ] Servo sweeps left and right — should have full range of motion both directions
- [ ] No grinding or mechanical stop — if grinding, servo horn needs repositioning
- [ ] LED changes color during sweep — colors change as servo position changes
- [ ] Ctrl+C exits cleanly

### Test 4: Ultrasonic Avoidance (servo_ultrasonic_avoid)

Place tank on floor with open space. Press the KEY button on the expansion board to start.

> **WARNING:** Tank will drive autonomously. Keep hands clear and give it at least 3 feet of space.

```bash
sudo ./servo_ultrasonic_avoid
```
Then press the KEY button on the expansion board.

- [ ] Tank drives forward when path is clear — green LED
- [ ] Tank detects obstacle and stops — hold hand in front, should stop within 50cm
- [ ] Servo sweeps to check left and right — after stopping, sensor sweeps to find clear path
- [ ] Tank turns away from obstacle — turns toward side with more space
- [ ] Ctrl+C exits cleanly

> **TIP:** If tank crashes into everything, the distance threshold may need tuning. Check the distance values in the C file.

### Test 5: Line Tracking

Requires black tape on a light surface. Place tank so camera faces the tape line.

```bash
sudo ./tracking
```
Then press the KEY button on the expansion board.

- [ ] Tank follows black tape line — stays on line through curves
- [ ] Tank corrects when it drifts off line — turns back toward tape
- [ ] Ctrl+C exits cleanly
- [ ] DEFERRED — no tape available (mark as deferred, test before camp)

### Test 6: Pan/Tilt Camera (Python)

Tests both camera servos using the Python pan/tilt test script.

```bash
sudo python3 ~/ncssmpython/pantilt_test.py
```

- [ ] Horizontal servo sweeps left and right — full range, no grinding
- [ ] Vertical servo sweeps up and down — full range, no grinding
- [ ] Both servos return to center — 90 degrees, straight ahead
- [ ] Ctrl+C exits cleanly — GPIO cleaned up

### Test 7: Camera + Jupyter Lab

Open Jupyter Lab in browser and run notebook 04 to verify camera works.

Open browser and navigate to `http://<pi-ip>:8888` — password: `yahboom`

Navigate to: `lab/02_vision/04_camera_basics.ipynb`. Run the setup cell.

- [ ] Jupyter Lab loads in browser
- [ ] `lab` folder visible in file browser
- [ ] Camera ready message prints — shows frame size 640x480
- [ ] Pixel inspector cell works — shows pixel values and circle on frame
- [ ] Live feed cell works — video feed displays in browser
- [ ] Cleanup cell runs cleanly — camera released

### Test 8: Color Detection

Run notebook 05 to verify color detection works.

Navigate to: `lab/02_vision/05_color_detection.ipynb`. Have a colored object ready to hold in front of camera.

- [ ] Camera opens cleanly after warmup
- [ ] Color detection mask shows white on target color
- [ ] Blob detection draws circle around target
- [ ] Live detection feed works — circle follows object as it moves
- [ ] Cleanup cell runs cleanly

## Step 4: Final Sign-Off

| Item | Value | Status |
|---|---|---|
| Kit number | | |
| MAC address | | Submitted to IT |
| IP address | | |
| All components tested | | Pass / Fail / Deferred |
| Notebooks working | | Pass / Fail |
| Known issues | | |

---

NCSSM Summer 2026 — ADAS AI Lab — Kit Test Checklist
