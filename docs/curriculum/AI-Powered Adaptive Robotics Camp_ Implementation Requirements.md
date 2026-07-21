# AI-Powered Adaptive Robotics Camp: Implementation Requirements

## Document Purpose

This document outlines all equipment, technology infrastructure, physical space, and personnel requirements needed to successfully implement the AI-Powered Adaptive Robotics Camp for high school students. It is designed to help school program leaders budget, plan, and prepare for camp delivery.

## Executive Summary

- **Total Estimated Budget:** $2,000 - $2,500 (one-time equipment purchase)
- **Prep Time Required:** 20-25 hours (pre-camp setup by curriculum team)
- **Facility Requirements:** One large classroom/lab space (accommodates 20-24 students)
- **Technology Infrastructure:** Reliable WiFi, electrical outlets, internet access

## 1. Robotics Hardware

### Primary Equipment: Robot Platforms

**Requirement:** 5-6 complete robot kits

**Recommended Option:** Raspberry Pi-Based Robot Kits

Specific product recommendations:
- **Option A: Yahboom G1 Tank Robot Kit** (Raspberry Pi 4 included)
  - Cost: ~$220-250 per unit
  - Includes: Tank chassis, Raspberry Pi 4 (4GB), camera module, ultrasonic sensors, IMU
  - Source: Amazon, Yahboom direct
- **Option B: Freenove 4WD Smart Car Kit** + Raspberry Pi 4
  - Cost: ~$120 (kit) + $75 (Raspberry Pi 4) = $195 per unit
  - Requires more assembly but well-documented
  - Source: Amazon, Freenove website

**Quantity:** 5 robots minimum (supports 20 students in teams of 4); 6 robots recommended (provides backup unit + supports up to 24 students)

**Total Hardware Cost:** $1,000 - $1,500 (depending on configuration and quantity)

### Required Hardware Components (if not included in kit)

Per robot, ensure the following are included or purchased separately:
- Raspberry Pi 4 (4GB RAM minimum, 8GB preferred)
- MicroSD card (64GB minimum, Class 10 or better)
- Wide-angle camera module compatible with Raspberry Pi
- 3-5 ultrasonic distance sensors (HC-SR04 or equivalent)
- IMU sensor (accelerometer/gyroscope)
- Motor driver board
- Rechargeable battery pack with sufficient capacity (7.4V LiPo or 18650 cell configuration)
- Battery charger
- Power cables and connectors

### Additional Hardware & Supplies

**Essential:**
- 5-6 USB power adapters for Raspberry Pi charging/programming (if not battery-powered during setup)
- 5-6 MicroSD card readers (for programming SD cards)
- Extension cords and power strips (minimum 3-4 multi-outlet strips)
- Basic hand tools for minor adjustments (small screwdriver set, hex keys)
- Spare batteries (2-3 additional battery packs)

**Recommended Spares:**
- 2-3 spare ultrasonic sensors
- 1 spare camera module
- Assorted jumper wires and connectors
- Electrical tape, zip ties, velcro straps

**Cost:** $150-200

## 2. Computing Equipment

### Student Laptops

**Requirement:** Students need laptops for data analysis, model training, and robot interaction

Options:
- **Students bring their own devices (BYOD)**
  - Minimum specs: 4GB RAM, modern web browser, WiFi capability
  - Platforms: Windows, macOS, Linux, Chromebook (with Linux enabled)
  - Most cost-effective option
- **School-provided laptops**
  - Needed if BYOD is not feasible
  - Quantity: 20-24 laptops (1 per student) OR 10-12 laptops (shared 2 per laptop)
  - Shared laptops work well given role rotation model

**Minimum Specifications:**
- 4GB RAM (8GB preferred)
- Modern web browser (Chrome, Firefox, Edge, Safari)
- WiFi capability
- USB ports for peripherals
- Ability to SSH into robots (terminal access or SSH client)

### Instructor/Support Equipment

**Required:**
- 2 instructor laptops/computers for demo and troubleshooting
- 1 large display monitor or projector for group instruction
- Document camera or webcam for showing physical robot demos (optional but helpful)

**Cost:** $0 if BYOD + existing school equipment used; $3,000-6,000 if purchasing student laptops

## 3. Technology Infrastructure

### Network Requirements

**Critical:**
- Reliable WiFi network accessible throughout classroom
- Bandwidth: Minimum 50 Mbps download, 10 Mbps upload (for class of 20-24)
- Network must support:
  - Multiple device connections (30-35 simultaneous devices: student laptops + robots + instructor devices)
  - SSH connections to robot IP addresses
  - Web-based interfaces (robot control panels)
  - Cloud services access (Google Colab, model training platforms)

**Configuration Needs:**
- Robots need static IP addresses or reliable DHCP with hostname resolution
- Firewall must allow SSH (port 22) within local network
- No overly restrictive content filtering that blocks educational ML platforms

**Alternative:** If school WiFi is problematic, a dedicated wireless router can be purchased ($50-100) to create an isolated network for camp.

### Internet Access

Required for:
- Google Colab (free cloud-based model training)
- Edge Impulse or similar ML platforms (optional)
- Software updates and package installations
- Documentation and tutorial access
- Backup resources

**Minimum:** 25 Mbps shared bandwidth for classroom

### Software & Platform Access

All free/open source — no licensing costs:
- Raspberry Pi OS (Linux-based, free)
- Python and scientific computing libraries (NumPy, OpenCV, TensorFlow Lite — all free)
- Google Colab (free tier sufficient)
- Web browsers
- SSH clients (built into macOS/Linux, free options for Windows like PuTTY)
- Code editors (VS Code, free)

**Firewall/Content Filter Considerations:**
- Ensure access to: colab.research.google.com, github.com, pypi.org, npm.org
- Allow SSH protocol within local network
- Allow file downloads (.py, .tflite, .csv file types)

No software purchases required — the entire stack is open source.

## 4. Physical Space Requirements

### Classroom/Lab Space

**Size:** Minimum 800-1000 sq ft for 20-24 students

**Testing Area (40-50% of space):**
- Open floor space for obstacle course (minimum 10' x 15' area)
- Hard, flat floor surface (tile, wood, laminate preferred over carpet)
- Space for multiple teams to test without interference
- Good lighting (robots use cameras — overhead fluorescent fine, avoid excessive shadows)

**Worktable Area (50-60% of space):**
- Tables/desks for 20-24 students
- Configuration: cluster tables for team collaboration (4 students per cluster)
- 5-6 team work zones with adequate space for laptops, notebooks, robot parking

**Power Requirements:**
- Electrical outlets accessible at each team work zone
- Minimum 2 outlets per team (for laptop charging, robot charging)
- Total: 10-15 available outlets across room

**Storage:**
- Lockable cabinet or closet for robot storage overnight
- Shelf space for charging stations

### Obstacle Course Materials

Required materials (build your own course):
- Cardboard boxes (various sizes) — FREE from shipping/recycling
- Foam core boards (4-6 sheets, 20"x30") — $30
- PVC pipes (optional for creating tunnels/gates) — $20
- Colored paper/cardstock (for goal markers) — $10
- Painter's tape or floor marking tape (for boundaries) — $15
- Wooden boards or foam blocks (for ramps/inclines) — $30

Course features to build:
- Narrow corridor (2x robot width)
- Scattered obstacles (boxes, blocks)
- Ramp or incline
- Goal markers (colored targets)
- Boundary lines

**Design consideration:** Course should be modular and reconfigurable.

**Total Cost:** $50-100 (mostly FREE using recycled materials)

## 5. Personnel Requirements

### Instructional Team

**Lead Instructor (Curriculum Developer):**
- Responsibilities: Overall curriculum delivery, technical troubleshooting, ML instruction
- Time commitment: Full camp week + 20-25 hours prep

**Co-Instructor/Teaching Assistant:**
- Responsibilities: Student support, robot troubleshooting, logistics
- Technical background helpful but not required
- Can be teacher, advanced student, or volunteer with tech interest
- Time commitment: Full camp week + 5-10 hours prep

**Optimal ratio:** 1 instructor per 10-12 students (2 instructors for 20-24 students)

### Pre-Camp Preparation Time

**Lead Instructor:**
- Robot assembly and testing: 10-12 hours
- Software setup and imaging: 6-8 hours
- Curriculum materials preparation: 4-6 hours
- Obstacle course construction: 3-4 hours
- **Total:** 23-30 hours over 2-3 weeks before camp

**Co-Instructor:**
- Orientation and training: 3-4 hours
- Materials preparation support: 2-3 hours
- **Total:** 5-7 hours

## 6. Consumables & Miscellaneous

### Student Materials

Per student:
- Notebook or journal for logging — $2
- Folder for handouts — $1
- Name badge — $0.50

**Total for 24 students:** $85

### Classroom Supplies

- Whiteboard markers (multiple colors) — $15
- Large sticky notes/poster paper for brainstorming — $20
- Printer paper for handouts — $10
- USB flash drives for data backup (optional, 5-6 units) — $50

**Total:** $95

### Emergency Supplies

- Basic first aid kit — $25
- Cable ties, duct tape, electrical tape — $15
- Spare AA/AAA batteries for remotes — $10

**Total:** $50

## 7. Technology Support Requirements

### IT Department Coordination

**Pre-Camp (2-3 weeks before):**

Network Setup:
- Work with IT to configure WiFi access for robots (MAC address registration if required)
- Set up static IPs or reserved DHCP addresses for 5-6 robots
- Test SSH connectivity from student devices to robot IPs
- Verify firewall rules allow necessary traffic

Software/Platform Access:
- Confirm Google Colab is not blocked
- Verify file download capabilities
- Test that cloud ML platforms are accessible
- Ensure SSH clients can be installed on school laptops if needed

**Day-Of Support:**
- IT contact available for network troubleshooting (phone/email)
- Backup WiFi solution if primary network fails

**Recommended:** IT Support Contact Sheet — create a document with:
- WiFi network name and password
- IT help desk contact info
- Robot IP addresses
- Network troubleshooting steps

## 8. Optional Enhancements

Upgrades that improve experience (not required):

**Additional Sensors for Robots:**
- Line following sensors — $30 per robot
- Additional cameras for stereo vision — $40 per robot
- Better quality sensors — $50 per robot

**Enhanced Obstacle Course:**
- Programmable LED targets — $60
- Moving obstacles (motorized) — $100
- Professional course barriers — $150

**Presentation Equipment:**
- Wireless presentation remote — $25
- Additional monitors for team presentations — $200-300 each

**Cost:** $200-500 if pursuing enhancements

## 9. Budget Summary

### Core Required Investment

| Category | Cost Range |
|---|---|
| Robot Kits (5-6 units) | $1,000 - $1,500 |
| Additional Hardware & Spares | $150 - $200 |
| Obstacle Course Materials | $50 - $100 |
| Student Materials & Supplies | $230 |
| **TOTAL EQUIPMENT** | **$1,430 - $2,030** |

### Additional Costs (If Applicable)

| Category | Cost Range |
|---|---|
| Student Laptops (if not BYOD) | $0 - $6,000 |
| Dedicated WiFi Router (if needed) | $0 - $100 |
| Optional Enhancements | $0 - $500 |

### Recurring Costs (Annual)

- Battery replacements: $50-100
- Consumable supplies: $200
- **Annual recurring:** $250-300

## 10. Space & Facility Checklist

Before approving venue, confirm:

- [ ] Room is 800+ sq ft
- [ ] Hard, flat flooring in at least 40% of space
- [ ] 10-15 accessible electrical outlets
- [ ] Strong WiFi signal throughout room
- [ ] Tables/desks for 20-24 students in collaborative arrangement
- [ ] Projector or large display for instruction
- [ ] Lockable storage for equipment
- [ ] Good overhead lighting
- [ ] Climate controlled (robots and laptops need moderate temperatures)
- [ ] Accessible during prep week for setup

## 11. Pre-Camp Preparation Timeline

*4-6 weeks before camp*

**Week 1-2: Procurement**
- [ ] Order robot kits
- [ ] Order additional components and supplies
- [ ] Secure laptop availability (BYOD communication or school device reservation)
- [ ] Reserve classroom/lab space

**Week 3-4: Technical Setup**
- [ ] Assemble robots
- [ ] Set up Raspberry Pi software environment
- [ ] Create master SD card image
- [ ] Clone image to all robot SD cards
- [ ] Test all robots thoroughly
- [ ] Configure network with IT department

**Week 5: Curriculum Prep**
- [ ] Build obstacle course
- [ ] Create data collection web interfaces
- [ ] Prepare training notebooks (Colab)
- [ ] Create deployment scripts
- [ ] Print student materials
- [ ] Test complete workflow end-to-end

**Week 6: Final Checks**
- [ ] Run full rehearsal of Day 1
- [ ] Verify all robot systems operational
- [ ] Confirm classroom setup
- [ ] Train co-instructor/teaching assistant
- [ ] Prepare backup materials

## 12. Equipment Longevity & Reusability

### Multi-Year Use

**Expected Lifespan:**
- Robot chassis and motors: 3-5 years with proper care
- Raspberry Pi computers: 3-5 years
- Sensors: 2-3 years (ultrasonic sensors most prone to damage)
- Batteries: 1-2 years (500-1000 charge cycles)
- Cameras: 3-5 years

**Reusability Across Camps:**
- Same equipment can be used for multiple camp sessions per year
- Robots can support other STEM programs (basic robotics, programming courses)
- Platform is expandable for advanced projects in future years

**Investment Justification:**
- One-time purchase of ~$2,000 supports multiple years of camps
- Equipment supports 20-24 students per session
- Can run 2-3 sessions per summer (60-72 students annually)
- Cost per student over 3 years: ~$10-15

## 13. Vendor & Purchasing Information

### Where to Purchase

**Robot Kits:**
- Amazon (fastest shipping, easy returns)
- Yahboom official website (direct from manufacturer)
- Freenove official website
- Adafruit, SparkFun (component suppliers)

**General Supplies:**
- Amazon (most one-stop shopping)
- Local office supply stores
- Hardware stores (for obstacle course materials)

**Recommended:** Purchase from Amazon for consolidated shipping and easier returns/exchanges.

### Purchase Account Requirements

- School purchase order system or credit card
- Amazon Business account (often provides educational discounts)
- Ability to receive shipments 4-6 weeks before camp

### Tax Exemption

- Most schools have tax-exempt status for educational purchases
- Provide tax-exempt certificate when ordering to reduce costs by 5-10%

## 14. Risk Mitigation & Contingencies

### Equipment Failure Plans

**During Camp:**
- 6th backup robot addresses individual robot failures
- Spare sensors/components for quick repairs
- Can consolidate to 4 robots (5 teams → 4 teams) if necessary

**Before Camp:**
- Order equipment 6 weeks early to allow time for returns/replacements
- Test all equipment 2 weeks before camp
- Have expedited shipping option for emergency parts

### Network Failure Plans

- **Backup Option 1:** Dedicated WiFi router creates isolated network independent of school infrastructure
- **Backup Option 2:** Robots can be controlled via direct Ethernet connection or USB in emergency
- **Backup Option 3:** Model training can happen on instructor laptop if cloud access fails

### Space Unavailability Plans

- Identify 2-3 backup spaces that meet requirements
- Obstacle course is portable (can set up in different location)
- Outdoor space can work if weather permits (covered area preferred)

## 15. Success Metrics & Evaluation

To demonstrate program value, track:

**Quantitative:**
- Number of students served
- Equipment utilization rate
- Student attendance/completion rate
- Pre/post assessment scores (ML concept understanding)

**Qualitative:**
- Student feedback surveys
- Parent testimonials
- Demonstration day attendance
- Student project outcomes (% of robots successfully navigating course)

**Return on Investment:**
- Cost per student
- Equipment reusability across years
- Potential for expanding program

## 16. Contact & Support

**Curriculum Developer**

Pre-Camp Questions:
- Technical specifications clarification
- Equipment alternatives
- Budget optimization
- Curriculum customization

Setup Support:
- Available for consultation during prep phase
- Can provide remote troubleshooting
- Video calls for complex setup questions

**Vendor Technical Support**

Yahboom/Freenove:
- Documentation and assembly guides available online
- Email support for defective units
- Community forums for troubleshooting

Raspberry Pi Foundation:
- Extensive online documentation
- Community support forums
- Educational resources

## Appendix A: Detailed Equipment List

### Robot Kit Components (Per Unit)

| Component | Specification | Quantity per Robot |
|---|---|---|
| Raspberry Pi 4 | 4GB or 8GB RAM | 1 |
| MicroSD Card | 64GB, Class 10 | 1 |
| Robot Chassis | Tank or 4WD car style | 1 |
| DC Motors | Suitable for chassis | 2-4 |
| Motor Driver | L298N or equivalent | 1 |
| Camera Module | Wide-angle, Raspberry Pi compatible | 1 |
| Ultrasonic Sensors | HC-SR04 or equivalent | 3-5 |
| IMU Sensor | MPU6050 or equivalent | 1 |
| Battery Pack | 7.4V LiPo or 18650 cells | 1 |
| Battery Charger | Compatible with battery type | 1 |
| Power Cables | Various | As needed |
| Mounting Hardware | Screws, standoffs, brackets | As included |

### Classroom Supply List

| Item | Quantity | Estimated Cost |
|---|---|---|
| Robot Kits | 5-6 | $1,000-1,500 |
| Spare Sensors | 5-10 | $30-50 |
| Power Strips | 4-6 | $60-90 |
| Extension Cords | 3-4 | $30-40 |
| USB Power Adapters | 5-6 | $50-75 |
| MicroSD Card Readers | 5-6 | $30-40 |
| Hand Tools Set | 1 | $25-40 |
| Obstacle Course Materials | Bulk | $50-100 |
| Student Notebooks | 24 | $50 |
| Whiteboard Markers | 2 sets | $15 |
| Poster Paper | 1 pad | $20 |
| First Aid Kit | 1 | $25 |
| Misc. Supplies | Various | $50 |

## Appendix B: Software Configuration Requirements

### Raspberry Pi SD Card Image Contents

**Operating System:**
- Raspberry Pi OS (formerly Raspbian) — Lite or Desktop version
- Python 3.9 or higher

**Python Libraries:**
- opencv-python (computer vision)
- numpy (numerical computing)
- tflite-runtime (TensorFlow Lite inference)
- RPi.GPIO (hardware control)
- picamera (camera interface)
- flask (web interface framework)
- pandas (data manipulation)

**System Configuration:**
- SSH enabled
- VNC enabled (optional, for remote desktop)
- Camera interface enabled
- GPIO interfaces enabled
- Static IP or hostname configured
- WiFi credentials pre-configured

**Custom Software:**
- Robot control library (provided by curriculum developer)
- Data collection web interface
- Model deployment scripts
- Testing utilities

## Appendix C: Sample Purchase Order Template

**Vendor:** Amazon Business / Yahboom / Freenove
**Ship To:** [School Address]
**Billing:** [School Billing Information]
**Tax Exempt Certificate:** [Attach]

**Items:**
- Yahboom G1 Tank Robot Kit (Qty: 6) — $1,350
- SanDisk 64GB MicroSD Cards (Qty: 10) — $80
- Anker USB Power Adapters (Qty: 6) — $75
- Ultrasonic Sensors HC-SR04 (Qty: 10) — $40
- Power Strips (Qty: 6) — $90
- Extension Cords 15ft (Qty: 4) — $40
- MicroSD Card Readers (Qty: 6) — $35
- Tool Kit — $30
- Foam Core Boards (Qty: 6) — $30
- Student Supplies (notebooks, folders, etc.) — $85

**Subtotal:** $1,855
**Shipping:** $50-100
**Tax:** $0 (exempt)
**Total:** $1,905-1,955

**Budget Code:** [Educational Programs / STEM Initiatives]
**Approval Required:** [Program Director Signature]

## Questions for School Program Leaders

Before finalizing implementation, please confirm:

- **Budget:** Is the $2,000-2,500 one-time equipment investment approved?
- **Space:** Can you provide dedicated classroom space meeting requirements for full week?
- **IT Support:** Can IT department provide pre-camp network configuration support?
- **Laptops:** Will students bring own devices (BYOD) or does school need to provide?
- **Staffing:** Is co-instructor/teaching assistant available for full camp week?
- **Timeline:** Is 4-6 weeks lead time available for equipment ordering and setup?
- **Storage:** Is secure equipment storage available between camp sessions if running multiple weeks?

---

**Document Prepared By:** Mekka — AI-Powered Robotics Camp Curriculum Developer & Lead Instructor
