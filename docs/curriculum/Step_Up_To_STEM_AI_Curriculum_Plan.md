# Step Up to STEM Lab — AI in Autonomous Driving

Summer Camp Curriculum Plan
June 15-19 2026 | Yahboom G1 Tank + Raspberry Pi 4B

## Program Overview

This five-day camp introduces students aged 14-15 to Artificial Intelligence through the lens of Autonomous Driving (AD) and Advanced Driver Assistance Systems (ADAS). Students work in teams of 3-4 to build, program, and race AI-powered tank robots, culminating in a timed obstacle course competition and parent showcase.

The curriculum is designed around a hands-on tweak-test-iterate loop. Students are not expected to write code from scratch. Instead they modify clearly marked parameters in pre-built Jupyter Lab notebooks and observe the physical results on their robot. This approach keeps the focus on AI concepts and systems thinking rather than syntax.

> **Note:** Announce winners in the presentations on Friday — give them some award.

| | |
|---|---|
| Teams | 5 teams of 3 |
| Duration | 5 days, M-F |
| Daily Hours | 2hr AM + 1.5hr PM |
| Hardware | Yahboom G1 Tank |

## Team Structure

Each team of 3 students chooses a role.

| Role | Real-World Equivalent | Responsibilities |
|---|---|---|
| Manager | Product Manager | Keeps the team on track. Reads the notebook concept section aloud. Decides which tweaks to try. Reports results during debrief. |
| Developer | Software Engineer | Makes the code changes in Jupyter Lab. Types the parameter values. Runs the cells. Iterates based on tester feedback. |
| Tester | QA Engineer / Safety Driver | Observes the robot. Documents what happened. Compares actual behavior to expected behavior. Calls out safety issues. |

## Competition & Games

Teams accumulate points throughout the week through daily games and challenges. Final race day run order is determined by total points — the team with the most points chooses to go last, giving them the strategic advantage of knowing the target time to beat.

### Daily Games (points toward run order)

- ADAS Family Feud — name a car feature that uses AI, name a sensor in a self-driving car
- ADAS/AD Pictionary — ADAS/AD and AI terms
- Telestration
- Jeopardy
- Codenames
- Chameleon/Imposter
- Name That Sensor — identify sensor and its ADAS use case
- Distance Estimation — closest guess to ultrasonic reading wins
- Color Challenge — fastest team to configure and run color detection
- Debug Race — first team to fix a broken notebook wins

### Materials

- Small balls (smaller than a tennis ball) — follow the color: yellow, blue, green, red, orange, purple (see if it can pick up purple)
- Legos for obstacles
- Items to simulate people
- Stop sign
- Electrical tape (confirm quantity before build-out)

### Race Day Scoring

| Challenge | Points | Penalty | ADAS Connection |
|---|---|---|---|
| S-Curve Navigation | Time-based | +5 sec per marker hit | Lane keeping |
| U-Turn Precision | Time + stop accuracy | +10 sec missed stop zone | Automated parking |
| Pedestrian Avoidance | 100 pts per Lego person spared | -100 pts per hit | Pedestrian detection |
| Color Waypoint Sequence | Time-based | +15 sec wrong color | Stop sign recognition |
| Bonus: Find the Object | 50 bonus pts, first team wins | N/A | Object search + navigation |

## Daily Schedule

*Subject to change — need to confirm.*

### Monday — Foundation Day

*What is a self-driving car and how does it work? Today we meet our robot and learn what it can do.*

| Session | Time | Activities |
|---|---|---|
| AM (2hr) | 8:45 - 11:30 | Concepts, Jupyter notebook intro, kit intro • Game 1: Terms Game • Start notebooks 01-03 |
| PM (1.5hr) | 12:45 - 2:30 | Game 2: ADAS Family Feud • Notebook 02: Motor Control — drive it • Notebook 03: Pan/Tilt Control — move the camera • Record team colors, topics and roles |

### Tuesday — The Car Sees

*How does a car see the world? Today we give our robot eyes and teach it to recognize what it sees.*

| Session | Time | Activities |
|---|---|---|
| AM (2hr) | 8:45 - 11:30 | How the camera sees • Game 3: Color Challenge • Start Notebooks 4-5 |
| PM (1.5hr) | 12:45 - 2:15 | Concept: What is a model? What is inference? • Notebook 06: Color Following — car chases the color • Notebook 07: Intro to AI Models — first Ollama prompt • Game 4: ADAS/AD Pictionary |

### Wednesday — The Car Thinks

*How does a car make decisions? Today we connect what the robot sees to what it does — and add an AI brain.*

| Session | Time | Activities |
|---|---|---|
| AM (2hr) | 9:00 - 11:00 | Concept: How does ADAS make decisions? Sensor fusion, decision trees, neural networks • Notebook 08: Vision to Decision — color detected triggers action • Notebook 09: AI Driver — full pipeline, camera to model to motors • Game 5: Distance Estimation |
| PM (1.5hr) | 1:00 - 2:30 | Introduce the challenge and video • First practice runs • Teams tune their AI driver • Slideware intro — what goes in a good presentation • Game 6: Imposter |

### Thursday — Challenge + Presentations

*Show us what your AI can do. Today we compete and tell our story.*

| Session | Time | Activities |
|---|---|---|
| AM (2hr) | 9:00 - 11:00 | Final tuning runs (30 min) • Timed obstacle course competition — run order by game points (recording) • Bonus round: Find the Object • Award ceremony (need some swag) |
| PM (1.5hr) | 1:00 - 2:30 | Slideware work — what did we build, how does it work, what would we change • Video footage review and selection • Dry run presentations • Feedback and polish |

### Friday — Parent Showcase

*Tell your story. Show what you built. Inspire the next generation.*

| Session | Time | Activities |
|---|---|---|
| AM (2hr) | 9:00 - 11:00 | Team presentations to parents (10 min per team) • Live robot demo for parents — color following + obstacle avoidance • Video showcase • Certificate ceremony |

## Jupyter Lab Notebook Curriculum

All notebooks follow the same structure: Concept, How It Works, The Code, Your Turn (marked tweak zones), What Happened (reflection), and an optional Challenge for advanced students. Notebooks are pre-written and working. Students modify clearly marked parameters and observe results on the robot.

### Directory Structure

See the current notebook layout in the repo: [`lab/`](https://github.com/msmekka/summer26-adasai/tree/main/lab)

### Notebook Details

| Notebook | ADAS Connection | Student Tweaks |
|---|---|---|
| 00 - What is ADAS | SAE L0-L5, real examples | None — concepts and discussion only |
| 01 - LED Control | Status indicators, brake lights | Color values (R/G/B), blink patterns, timing |
| 02 - Motor Control | Drive-by-wire, throttle control | Speed (0-255), direction, duration |
| 03 - Pan/Tilt Control | Adaptive headlights, camera gimbals | Angles (0-180), sweep speed, center position |
| 04 - Camera Basics | Computer vision pipeline | Brightness, contrast, resolution, frame rate |
| 05 - Color Detection | Traffic light recognition, lane markings | TARGET_COLOR variable, HSV threshold values |
| 06 - Color Following | Object tracking, follow-the-leader | Speed response, turn sensitivity, minimum blob size |
| 07 - Intro to Models | AI decision engines | Prompt text, model parameters, response parsing |
| 08 - Vision to Decision | Sensor fusion, action triggers | Detection threshold, action mapping, confidence cutoff |
| 09 - AI Driver | Full autonomous pipeline | Waypoint sequence, speed profile, avoidance behavior |
| ADV - PID Tuning | Cruise control, lane centering | P, I, D values — observe tracking smoothness vs oscillation |
| ADV - Waypoint Sequence | Route planning, nav systems | Custom color sequence, dwell time, transition behavior |
| ADV - Search Pattern | Parking assist, object search | Search algorithm, area coverage, target recognition |

## Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| Hardware | Yahboom G1 Tank + Raspberry Pi 4B | Robot platform with motors, servos, camera, ultrasonic, RGB LED, line tracking |
| OS | Yahboom custom Raspbian image | Pre-configured with all drivers, OpenCV, and Jupyter Lab |
| Dev Environment | Jupyter Lab (browser-based) | Students write and run code in the browser, no terminal needed |
| Computer Vision | OpenCV (pre-installed) | Color detection, object tracking, camera feed processing |
| AI Model | Ollama + Phi-3 Mini (pending approval) | Lightweight on-device LLM for decision making, no internet required |
| Language | Python 3 + RPi.GPIO | Primary student language, readable and beginner friendly |

## Obstacle Course Design

One shared course. Teams run sequentially, timed. Three runs per team, best time counts. Run order determined by game points accumulated Monday through Wednesday — highest points chooses last (strategic advantage).

### Course Elements

- **S-Curve** — colored tape or cones, tests motor control and turning precision. ADAS connection: lane keeping.
- **U-Turn with Stop Zone** — colored marker at the end, car must stop within 6 inches. ADAS connection: automated parking.
- **Pedestrian Zone** — Lego figures and small toys as obstacles, ultrasonic avoidance active. ADAS connection: pedestrian detection.
- **Color Waypoint Sequence** — 3 colored markers in sequence (team color order). Car must follow correct sequence. ADAS connection: traffic light and sign recognition.
- **Finish Line** — bright colored tape, timer stops on crossing.

### Course Materials Needed

- Colored tape or electrical tape — at least 3 colors (red, blue, green minimum)
- Small cones or paper cups as lane markers
- Lego figures or small toy people as pedestrians (6-10)
- Colored cardstock or foam board for waypoint markers
- Timer — phone or stopwatch
- Leaderboard — whiteboard with team names and scores

## Bonus Round: Find the Object

After the main competition a colored object is placed somewhere in the open space. Teams have 90 seconds to program their car to find and drive to it. First team to reach the object wins 50 bonus points. Tests the full AI pipeline — search pattern, color detection, navigation.

---

STEMINIST Lab — AI in Autonomous Driving — Confidential Draft
