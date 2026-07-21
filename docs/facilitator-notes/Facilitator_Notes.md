# AI in Autonomous Driving — Facilitator Notes

*NCSSM Summer 2026 | June 15-19, 2026*

## How to Read These Notes

These notes are for facilitators and helpers. Each day includes session notes, notebook guidance, suggested discussion questions, video recommendations, and student-facing material you can share or display.

- **FACILITATOR:** facilitator-only notes — tips, timing, things to watch for.
- **STUDENT MATERIAL:** student-facing material — can be projected, printed, or read aloud.
- **VIDEO:** suggested YouTube videos to find and cue up before the session.
- **WATCH FOR:** things to watch for — common student struggles or teachable moments.

## Notebook Color Key

Every notebook follows the same structure. Remind students of this at the start of each session:

- **ADAS Connection** — why this matters in a real car
- **How It Works** — the concept explained simply
- **The Code** — pre-written, working, do not delete
- **YOUR TURN** (═══ borders) — the only cells students should change
- **What Happened** — reflection questions, discuss as a team
- **CHALLENGE** — optional, for students who finish early

> **FACILITATOR:** The most common mistake: students edit code outside the tweak zones and break the notebook. Remind them at the start of every session: only change values inside the ═══ borders.

---

## MONDAY — Foundation Day

*What is a self-driving car and how does it work? Today we meet our robot and learn what it can do.*

### Morning Session | 9:00 - 11:00 AM | 2 hours

**Welcome and Introductions (20 min)**

> **FACILITATOR:** Keep this energetic and fast. Students are excited. Don't let admin drag.

- Welcome students, introduce yourself and helpers
- Quick icebreaker — ask each student: what car feature do you wish existed?
- Make teams and team names
- Explain the week's arc — Monday hardware, Tuesday vision, Wednesday AI, Thursday race, Friday parents
- Explain roles: Manager, Developer, Tester — rotate every session
- Show the leaderboard — explain game points determine race day run order

> **STUDENT MATERIAL:** This week you will build and program an AI-powered robot car. By Friday your robot will drive itself using computer vision and an AI model — the same technologies used in real self-driving cars.

**ADAS/AD Concepts Presentation (40 min)**

> **FACILITATOR:** This is the most important session of the week. Get students excited about what they are about to build. Use questions to drive discussion rather than lecturing.

*What is ADAS?*
- ADAS = Advanced Driver Assistance Systems
- Features already in most new cars: lane keeping, automatic braking, adaptive cruise control, parking assist
- Ask students: how many of you have been in a car with any of these features?

> **STUDENT MATERIAL:** ADAS features are already in most new cars. They help drivers stay safe by taking over small tasks automatically. Self-driving cars take this further — they handle everything.

> **VIDEO:** Search YouTube: "Tesla FSD full self driving compilation" — show 2-3 minutes. Ask students: what is the car seeing? How is it deciding what to do?

*SAE Levels of Autonomy*
- Level 0: No automation — human does everything
- Level 1: Driver assistance — one feature (cruise control)
- Level 2: Partial automation — multiple features (Tesla Autopilot)
- Level 3: Conditional automation — car drives, human must be ready to take over
- Level 4: High automation — car handles most situations
- Level 5: Full automation — no human needed, ever

> **STUDENT MATERIAL:** SAE (Society of Automotive Engineers) defined 6 levels of driving automation. Most cars today are Level 1-2. True Level 5 does not exist yet — it is the goal the entire industry is working toward.

> **VIDEO:** Search YouTube: "SAE levels of driving automation explained" — 2-3 minute explainer video

*How Does a Self-Driving Car See?*
- Cameras — like your robot's USB camera
- Radar — measures distance and speed of objects
- Lidar — laser pulses that build a 3D map
- Ultrasonic — short range distance sensing (like your robot's front sensor)
- GPS — location

> **FACILITATOR:** Point to the robot: "Your robot has a camera and an ultrasonic sensor. That is two of these five sensor types. Real cars combine all five."

> **STUDENT MATERIAL:** Self-driving cars are covered in sensors. Each one sees the world differently. The car combines all of them to build a complete picture — this is called sensor fusion.

> **VIDEO:** Search YouTube: "How Waymo self driving car sees the world lidar camera radar" — shows the sensor visualization

*Hardware Tour*
- Hold up or display one of the assembled tank kits
- Point out each component: motors, tracks, camera, pan/tilt, ultrasonic sensor, RGB LED, expansion board, Pi
- Explain what each one does and which SAE sense it corresponds to
- "This week you will program every single one of these"

> **FACILITATOR:** Let students touch and handle the kit if possible. Physical familiarity matters.

**Game 1: Terms Game (15 min)**

> **FACILITATOR:** Keep it fast and fun. Teams earn points toward race day run order.

- Show images or descriptions of ADAS sensors
- First team to correctly identify the sensor AND name one ADAS feature that uses it wins the round
- 5 rounds, 2 points per correct answer
- Record scores on the leaderboard

> **STUDENT MATERIAL:** Sensors to know: Camera, Radar, Lidar, Ultrasonic, GPS. What ADAS feature uses each one?

### Afternoon Session | 1:00 - 2:30 PM | 1.5 hours

**SSH In and Jupyter Lab Orientation (15 min)**

> **FACILITATOR:** Helpers should circulate to troubleshoot connection issues. Have the Connect to Pi guide ready. Most students will not have used SSH before.

- Each team opens a terminal and SSHs into their assigned Pi
- Walk through the Jupyter Lab interface — file browser, notebook structure, run cell shortcut (Shift+Enter)
- Show the `lab/` folder structure
- Remind students: only edit inside the ═══ tweak zones

> **WATCH FOR:** Students who have never used a terminal will struggle. Pair them with a teammate who is more comfortable. Do not let one student do all the typing — rotate.

**Notebooks 01-03 (60 min)**

> **FACILITATOR:** Move fast through these. They are warm-up exercises not deep dives. The goal is to get the robot moving and build confidence.

| Notebook | Time | Notes |
|---|---|---|
| 01 | 15 min | LED Control. Students change True/False values to set their team color. First physical result of the week. Make it celebratory — "that color is YOUR team." |
| 02 | 20 min | Motor Control. Students change SPEED and DURATION. Tank moves. Big moment. Make sure tanks are on the floor. The square challenge is optional — skip if running behind. |
| 03 | 20 min | Pan/Tilt Control. Students move the camera with code. Connect to ADAS: adaptive headlights, camera gimbals in real cars. Smooth scan challenge is optional. |

> **FACILITATOR:** If teams finish all three with time left, have them go back to Notebook 02 and try the square challenge. If teams are struggling, skip Notebook 03 — it is the least critical of the three.

> **WATCH FOR:** Battery levels. If a tank behaves erratically or motors are weak, battery is low. Swap to a charged battery before continuing.

**Game 2: ADAS Family Feud (15 min)**

- Questions like: "Name a car feature that uses AI", "Name a sensor in a self-driving car", "Name a company making self-driving cars"
- Survey-style — most popular answers score highest
- Record scores on leaderboard

---

## TUESDAY — The Car Sees

*How does a car see the world? Today we give our robot eyes and teach it to recognize what it sees.*

### Morning Session | 9:00 - 11:00 AM | 2 hours

**Concept: How Computers See (15 min)**

> **FACILITATOR:** This is the bridge from hardware to AI. Students need to understand that the camera does not see a picture — it sees numbers. This unlocks why everything we do with OpenCV works.

- A digital image is a grid of pixels
- Each pixel has 3 numbers: Red, Green, Blue (0-255 each)
- A 640x480 image has 307,200 pixels = 921,600 numbers
- At 30 frames per second: 27 million numbers per second just to see

> **STUDENT MATERIAL:** Your robot's camera does not see a picture. It sees a giant grid of numbers. Every pixel is three numbers: how much red, how much green, how much blue. The computer has to find patterns in those numbers to understand what it is looking at.

> **VIDEO:** Search YouTube: "How computers see image recognition neural network" — 3Blue1Brown or similar visual explainer

*Why HSV?*
- RGB changes dramatically with lighting — a red object looks different in shadow vs sunlight
- HSV separates hue (the actual color) from brightness
- Hue stays consistent even when lighting changes
- Demo: hold a colored object in front of the camera, switch between BGR and HSV in Notebook 04
- Shine a phone flashlight on it — watch how BGR values jump but HSV hue stays consistent

> **FACILITATOR:** This demo is the most important moment of Tuesday morning. Do it yourself first, then have each team try it. The "aha" happens when they see the hue stay stable under the flashlight.

> **STUDENT MATERIAL:** HSV color space separates color from brightness. This is why self-driving cars use HSV for color detection — a red stop sign looks the same in HSV whether it is bright or in shadow.

**Notebooks 04-05 (75 min)**

| Notebook | Time | Notes |
|---|---|---|
| 04 | 30 min | Camera Basics. Students see what the robot sees. Key moments: the pixel value printout (921,600 numbers per frame), the live feed, and the color space comparison. Phone flashlight demo happens here in Tweak Zone 3. |
| 05 | 40 min | Color Detection. Students detect their team color. Key moments: the three-panel display (original, mask, result), the MIN_RADIUS dial-down exercise, and the live detection feed with the LEFT/RIGHT indicator. Have colored balls or objects ready for this notebook. |

> **FACILITATOR:** For the color space comparison, project yours on a screen if possible so the whole class can see the difference between BGR and HSV simultaneously.

> **WATCH FOR:** Students will try to detect clothing and get frustrated by noisy masks. Redirect them to a solid colored object held at arm's length. The detection quality difference is dramatic and teaches MIN_RADIUS naturally.

**Game 3: Color Challenge (10 min)**

- Facilitator holds up a colored object
- First team to change TARGET_COLOR in Notebook 05 and run detection successfully wins
- 3 rounds with different colors
- 2 points per round

### Afternoon Session | 1:00 - 2:30 PM | 1.5 hours

**Concept: What is a Model? (10 min)**

> **FACILITATOR:** Keep this brief — students have been sitting. Get them back to the robot quickly.

- A model is a mathematical function that takes input and produces output
- It was trained on lots of examples until it learned patterns
- Inference = running the model on new data to get a prediction or decision
- The model we are using: Phi-3 Mini by Microsoft, running on a dedicated server

> **STUDENT MATERIAL:** An AI model is like a very experienced advisor. It has seen millions of examples and learned patterns from them. When you give it new information, it uses those patterns to make a prediction or decision.

> **VIDEO:** Search YouTube: "How does machine learning work simple explanation" — pick a clean 3-5 minute explainer

**Notebooks 06-07 (65 min)**

| Notebook | Time | Notes |
|---|---|---|
| 06 | 35 min | Color Following. The robot chases a colored ball. This is the biggest physical moment of the week so far. Key parameters: TARGET_COLOR, FOLLOW_SPEED, TURN_SPEED, DEAD_ZONE. Start with low speeds (35/30). The dead zone visualization with green lines on the feed is a key teaching moment. |
| 07 | 25 min | Intro to Models. First conversation with the AI. Key moments: the response time (cold vs warm), the one-word decision test, and Zone 4 where students write their own prompt. No motors yet — this is purely AI exploration. |

> **FACILITATOR:** Make sure every team gets their robot successfully following before moving on. This is the emotional high point of Tuesday — do not rush past it. Let students celebrate.

> **WATCH FOR:** Students will crank up FOLLOW_SPEED immediately. Let them — watching the robot overshoot and lose the target teaches why lower speeds work better. Then ask: "how would you fix this?" That leads naturally to proportional control.

> **FACILITATOR:** The moment the model ignores the one-word constraint and gives a paragraph is a perfect teaching moment: "AI does not always do what you tell it. This is why we validate the output before acting on it."

**Game 4: ADAS/AD Pictionary (15 min)**

- Terms from the week: sensor fusion, inference, dead zone, HSV, contour, autonomous, LIDAR, waypoint
- Standard Pictionary rules — teams draw and guess
- 3 points per correct guess

---

## WEDNESDAY — The Car Thinks

*How does a car make decisions? Today we connect what the robot sees to what it does — and add an AI brain.*

### Morning Session | 9:00 - 11:00 AM | 2 hours

**Concept: How ADAS Makes Decisions (15 min)**

> **FACILITATOR:** This ties the whole week together. Students have built the eyes (camera), the reflexes (color following), and met the brain (Phi-3). Now they connect all three.

- Perception → Decision → Action: the autonomous driving loop
- Sensor fusion: combining multiple sensor inputs for better decisions
- The observation is the bridge: translating pixel data into language the AI can reason about
- Safety first: always validate AI output before acting on it

> **STUDENT MATERIAL:** Every self-driving car runs the same loop thousands of times per second: See → Think → Act. Today your robot runs this loop for real. The camera sees, the AI thinks, the motors act.

> **VIDEO:** Search YouTube: "Tesla neural network visualization autonomy day" — shows the actual perception pipeline

**Notebooks 08-09 (90 min)**

| Notebook | Time | Notes |
|---|---|---|
| 08 | 45 min | Vision to Decision. The full pipeline without motors first. Camera detects color → builds observation text → AI decides → decision printed. Key learning: the observation quality determines decision quality. Zone 3 adds simulated obstacle data — students set SIMULATED_DISTANCE and see the AI balance two competing inputs. |
| 09 | 45 min | AI Driver. The full pipeline with motors running. This is the capstone of the curriculum — camera to AI to motors, fully autonomous. Key parameters: all the color following parameters plus SYSTEM_PROMPT. Teams that finish early should start tuning for the obstacle course. |

> **FACILITATOR:** Spend time on Zone 1 — the `build_observation()` function. This is the perception summary concept. Ask: "what information did we include? What did we leave out? How would adding more information change the AI decision?"

> **WATCH FOR:** AI response times will vary. If the model is slow remind students this is because it is reasoning about a complex prompt. The tradeoff between prompt detail and response speed is a real engineering problem.

> **FACILITATOR:** Before starting Notebook 09 make sure every team has Notebook 08 working cleanly. Notebook 09 adds motors to an already complex pipeline — debugging it is much harder if 08 is not solid.

> **WATCH FOR:** This is the highest stakes notebook. GPIO conflicts, camera timeouts, and AI response delays can all cause issues. Have the kernel restart reminder ready. Keep a second SSH session open on each kit.

**Notebook 10: ultrasonic sensor obstacle avoidance — 15 minutes**

### Afternoon Session | 1:00 - 2:30 PM | 1.5 hours

**Introduce the Challenge (15 min)**

- The robot starts moving forward with a simple goal: travel from point A to point B. Along the way, the judge holds up colored cards in front of the camera — red means stop for 2 seconds and wait, green means go, and orange means the mission is complete. The robot has to correctly identify the color and respond in real time while still moving.
- While the robot is driving, it's also continuously measuring distance with its ultrasonic sensor. If something gets within 25cm of the front of the robot, it stops immediately and executes a multi-step avoidance sequence — turn right, drive past the obstacle, turn back, realign, and resume heading. The obstacle can be anything solid: a box, a book, your hand.
- Teams run the whole challenge twice. In CV Mode, every decision is instant and deterministic — the color map is hardcoded and the avoidance sequence never changes. In AI Mode, the robot stops moving every time it needs to make a decision and sends a description of the situation to Phi-3 Mini running on the instructor's MacBook over WiFi. The model reasons about what to do based on NC traffic rules and sends back either a single action word or a full timed sequence for obstacle avoidance.
- Everything the robot is thinking prints to the Jupyter screen in real time — what it detected, what mode it's in, what it decided, and what Phi-3 said. This makes the AI's reasoning visible and auditable, which is a big part of the lesson.
- The key comparison moment is watching CV Mode vs AI Mode side by side. CV is fast and reliable but rigid. AI is slower — the robot visibly pauses to think — but it's reasoning from knowledge rather than following rules someone else wrote. That tension is exactly what real autonomous vehicle engineers deal with every day.

> **FACILITATOR:** Walk students through the course physically. Explain each element and its ADAS connection. Make the race feel real — this is what Thursday is about.

> **STUDENT MATERIAL:** The obstacle course tests every skill you have built this week. The team with the best tuned AI driver wins. You have the rest of today and Thursday morning to tune.

**Practice Runs + Tuning (45 min)**

> **FACILITATOR:** Let teams run the course and identify where their robot struggles. This is free-form — facilitators circulate and coach. Focus coaching on: DEAD_ZONE, FOLLOW_SPEED, TURN_SPEED, and SYSTEM_PROMPT.

- Each team gets at least 2 practice runs
- After each run: what went wrong? Which parameter do we change?
- Helpers should be stationed at the course to time and observe

> **WATCH FOR:** Teams will want to make many changes at once. Coach them to change ONE parameter at a time. This is the scientific method — isolate the variable.

**Slideware Intro + Work (15 min)**

> **FACILITATOR:** Keep this brief — teams are eager to tune. Just give them the structure and let them start.

- Presentation structure: What did we build? How does it work? What would we change? What did you learn?
- 10 minutes per team on Friday
- Include a live demo or video
- Each team member should speak

**Game 6: Debug Race (15 min)**

- Facilitator intentionally breaks a notebook (change a variable to an invalid value, introduce a syntax error, swap pin numbers)
- First team to find and fix the bug wins
- 5 points — this is the highest value game

> **FACILITATOR:** Prepare 2-3 broken notebooks in advance. Good bugs to introduce: `TARGET_COLOR = 'purple'` (not in COLOR_RANGES), `FOLLOW_SPEED = -50` (negative), wrong IP for OLLAMA_HOST.

---

## THURSDAY — Race Day + Presentations

*Show us what your AI can do. Today we compete and tell our story.*

### Morning Session | 9:00 - 11:00 AM | 2 hours

**Final Tuning (30 min)**

> **FACILITATOR:** Teams get one last chance to tune. Keep it focused — no major changes. Small adjustments only.

- Announce run order based on final game point standings
- Each team gets one practice run before timed runs begin
- Remind teams: 3 timed runs, best time counts

> **WATCH FOR:** Nerves will cause students to make last-minute changes that break their tuned configuration. Coach them: "if it worked yesterday, trust it today."

**Timed Obstacle Course Competition (60 min)**

> **FACILITATOR:** Record every run on video — students will use this footage for Friday presentations and it is great for the parents. Announce each team dramatically. Keep energy high.

- Run order from lowest to highest game points
- Announce each team and their run number
- Timer starts when robot crosses start line
- Record time + penalties on leaderboard after each run
- Celebrate every run regardless of outcome

> **FACILITATOR:** Have a helper stationed at the course to enforce rules and spot penalties. You focus on the energy in the room.

**Bonus Round: Find the Object (15 min)**

- Place a colored object somewhere in the open space
- Teams have 90 seconds to program their robot to find and drive to it
- First robot to reach the object wins 50 bonus points
- Teams may modify their SYSTEM_PROMPT and TARGET_COLOR

**Award Ceremony (15 min)**

> **FACILITATOR:** Prepare awards in advance. Every team should receive something.

- Announce final standings
- Award fastest time
- Award most improved
- Award most creative driving behavior / best SYSTEM_PROMPT
- Consider: best team name, best presentation (announced Friday)

> **FACILITATOR:** Order some swag — t-shirts, certificates, stickers. Students remember the physical award long after they forget the code.

### Afternoon Session | 1:00 - 2:30 PM | 1.5 hours

**Presentation Work (90 min)**

- Teams finalize slides
- Review and select video footage from today's runs
- Each team does a dry run presentation (5 min max)
- Facilitators give feedback: speak up, explain the code simply, connect to real ADAS

> **FACILITATOR:** Presentation structure reminder: What did we build? How does it work? What would we change? What did you learn? Each team member speaks at least once.

> **WATCH FOR:** Students will want to show every line of code. Coach them: "your parents don't know Python. Explain what it does, not how it looks."

---

## FRIDAY — Parent Showcase

*Tell your story. Show what you built. Inspire the next generation.*

### Morning Session | 9:00 - 11:00 AM | 2 hours

Allow students to tweak presentations and do dry run work.

---

## Appendix: Quick Reference

### Key Commands

| Command | Purpose |
|---|---|
| `ssh pi@<ip>` | Connect to Pi from laptop |
| `jupyter notebook list` | Check if Jupyter is running |
| `sudo pkill -9 -f jupyter` | Kill all Jupyter instances |
| `sudo reboot` | Reboot the Pi |
| `df -h` | Check disk space |
| `ps aux \| grep mjpg` | Check if mjpg_streamer is running |
| `vcgencmd measure_temp` | Check Pi temperature |
| `ip link show wlan0 \| grep ether` | Get Pi MAC address |
| `ipconfig getifaddr en0` | Get Mac IP address |

### Common Issues and Fixes

| Issue | Fix |
|---|---|
| Robot behaves unexpectedly | Restart Jupyter kernel, run cells from top |
| Camera not opening | Check mjpg_streamer is disabled: `ps aux \| grep mjpg` |
| AI server timeout | Check Ollama is running on Mac, verify IP in `ai_driver.py` |
| Motors not responding | Check battery charge, verify GPIO cleanup ran |
| Servo grinding | Check servo horn position, run `pantilt_test.py` |
| Can't SSH in | Try Yahboom hotspot: `ssh pi@192.168.50.1` password: `12345678` |
| Jupyter won't load | Kill all instances: `sudo pkill -9 -f jupyter`, restart |
| No IP address | `wpa_cli -i wlan0 reconfigure`, then `ip addr show wlan0` |

### Kit IP Assignments

| Kit | Team Name | IP Address | Notes |
|---|---|---|---|
| Kit 1 | | | |
| Kit 2 | | | |
| Kit 3 | | | |
| Kit 4 | | | |
| Kit 5 | | | |

---

NCSSM Summer 2026 — AI in Autonomous Driving — Facilitator Notes
