🚙 UGV Ground Robot Project
Autonomous Indoor Navigation Using Raspberry Pi + Marvelmind UWB

--------- 

System Architecture Overview
  ┌──────────────────────────┐
                    │    Marvelmind Dashboard   │
                    │     (Laptop Host PC)     │
                    └──────────────┬───────────┘
                                   │ USB
                                   ▼
                         ┌───────────────────┐
                         │  Marvelmind Modem │
                         └───────────────────┘
                                   │ RF/UWB
        ┌──────────────────────────┼──────────────────────────┐
        ▼                          ▼                          ▼
┌──────────────┐        ┌────────────────┐         ┌─────────────────┐
│ Fixed Beacon │        │ Fixed Beacon   │         │  Fixed Beacon   │
│     #1       │        │      #2        │         │       #3        │
└──────────────┘        └────────────────┘         └─────────────────┘
                                   │
                                   ▼
                           ┌─────────────┐
                           │ Mobile UWB  │
                           │  Beacon     │
                           └──────┬──────┘
                                  │
                                  ▼
                       ┌────────────────────┐
                       │ Waveshare UGV01    │
                       │  (Raspberry Pi)    │
                       └────────────────────┘

This diagram shows the full information flow:
Beacons → Modem → Laptop
Laptop (future: Pi) → Rover
Rover uses nav + localization to drive
📌 Project Overview
This project develops an indoor autonomous ground rover that uses:
A Waveshare UGV01 mobile robot base
A Raspberry Pi for motor logic & computation
A Marvelmind Indoor GPS UWB system for precise localization
Eventually, the rover will:
Receive real-time (X, Y, Z) coordinates
Compute how to reach target coordinates
Drive autonomously without human input
🧰 Hardware Used
Waveshare UGV01 base
Raspberry Pi
Marvelmind stationary beacons
Marvelmind mobile beacon
Marvelmind modem
Laptop
MicroSD card
Power adapters
🛠 Software Used
✔ Marvelmind SW Pack (v8.101 – Jan 2025)
Contains:
Firmware for all beacons
NIA positioning engine
Dashboard tools
API
✔ Raspberry Pi Imager
Used to:
Install Raspberry Pi OS
Enable SSH
Preconfigure WiFi
✔ SSH Tools
Windows CMD
macOS Terminal
✔ Pi Development Packages
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
🔧 System Setup
1. Flashing Raspberry Pi OS
Selected RPi OS (32-bit)
Enabled SSH
Enabled WiFi (UGV network)
Flashed SD card
Inserted into rover
2. Connecting to UGV Network
UGV broadcasted WiFi AP:
UGV-XXXX
Tested connectivity:
ping 192.168.4.1   # UGV Controller Board
ping 192.168.4.2   # Raspberry Pi
ping 192.168.4.3   # Laptop
SSH into Pi:
ssh pi@192.168.4.2
📁 3. Project Folder Structure on Pi
~/rover
│
├── motor_control/
│   └── motor.py
│
├── marvelmind/
│   └── beacon_reader.py
│
└── autonomous/
    └── navigation.py
🚦 Motor Control (motor.py)
This script attempts to send commands to UGV to move forward/backward/turn.
However, running it produced:
[Errno 111] Connection refused
This confirms:
UGV01 does not provide a Raspberry Pi motor-control API
No documentation
No TCP/serial API exposed
Movement firmware is missing
Therefore motor.py is a placeholder.
📡 Marvelmind Setup
✔ Completed
Downloaded full NIA pack
Read entire manual
Understood modem ↔ beacon ↔ mobile beacon system
Determined that modem on laptop is best
Placed fixed beacons in corners of room
Mounted mobile beacon on rover
❗ Pending
Connect modem to Pi
Implement beacon_reader.py
Stream coordinates into navigation logic
🧭 Navigation Logic (navigation.py)
Will perform:
Read current coordinates
Calculate heading/distance error
Send appropriate motor commands
Stop at destination
Currently a placeholder pending motor-control firmware.
⚠️ Problems Encountered
1. Waveshare Firmware Issues
Rover disconnects from WiFi during certain turns
Motor system freezes with directional commands
No downloadable UGV01 Pi image
Backend motor-control API missing
2. Missing Motor-Control API
TCP commands rejected
No listening port for motor control
UGV01 appears incomplete or unreleased
3. Marvelmind Challenges
Modem not yet mapped to Pi
Unsure whether Pi or laptop should serve as host
Need to map serial (/dev/ttyACM0) for modem
✅ Results Achieved
Pi flashed and functional
SSH communication fully working
UGV network tested & verified
Installed Python tools
Created project directory structure
Attempted motor testing (properly documented)
Completed Marvelmind research + system mapping
🔮 Future Work
Acquire UGV01 motor-control firmware/API
Enable low-level motor commands
Receive Marvelmind (X, Y, Z) on Pi
Complete navigation algorithm
Use 10+ beacons for full-range mapping
Add drone subsystem for overhead mapping
🗂 Appendix
A. System Screenshots (Add When Uploading)
You should insert:
UGV control dashboard
Pi SSH login
Folder tree (ls -R)
Motor test logs
Pi Imager configuration
Rover internals
Marvelmind dashboard
B. Terminal Logs
Ping to Pi
Reply from 192.168.4.2: bytes=32 time=7ms TTL=64
System Update Logs
Temporary failure resolving 'raspbian.raspberrypi.com'
Python Install Confirmation
python3-pip is already the newest version.
C. Code Snippets
motor_control/motor.py
import socket, time

HOST = "192.168.4.1"
PORT = 2001

def send_command(cmd):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(cmd.encode())
    except Exception as e:
        print("Error sending command:", e)

print("Testing forward...")
send_command("forward")
time.sleep(1)
marvelmind/beacon_reader.py
# Placeholder for reading Marvelmind UWB position (X, Y, Z)
def read_position():
    pass
autonomous/navigation.py
# Placeholder for navigation logic based on beacon coordinates
def navigate_to_target(x_target, y_target):
    pass
D. Hardware Notes
Raspberry Pi LEDs
Red solid: power OK
Green blinking: SD card activity
UGV Internal Layout
Pi mounted on top
Motor driver board beneath
Beacons tracked via UWB
