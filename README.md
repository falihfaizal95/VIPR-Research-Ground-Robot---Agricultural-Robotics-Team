# 🤖 UGV Ground Robot Project  
## **Autonomous Indoor Navigation Using Raspberry Pi + Marvelmind UWB**

---

## 📌 **Project Overview**

This project develops an **indoor autonomous ground rover** using:

- A **Waveshare UGV01** robotic base  
- A **Raspberry Pi** for computation + motor control  
- A **Marvelmind Indoor GPS (UWB)** positioning system for real-time indoor localization  
- Python scripts for motor control, beacon data parsing, and future autonomous navigation  

The goal is to create a rover that can:

- Receive **(X, Y, Z)** coordinates from a mobile UWB beacon  
- Compute motor decisions automatically  
- Navigate without human intervention  

---

# 🧰 **Hardware Used**

- Waveshare UGV01 Ground Rover  
- Raspberry Pi (UGV Compute Module)  
- Marvelmind Fixed Beacons #1, #2, #3  
- Marvelmind Mobile Beacon (mounted on rover)  
- Marvelmind Modem  
- Laptop (Marvelmind Dashboard + SSH into Pi)  
- MicroSD card (16–32GB recommended)  
- USB power adapters  

---
System Setup (Full Documentation)
This section documents every step completed so far — required by your professor.
1️⃣ Flash Raspberry Pi OS
Using Raspberry Pi Imager:
Choose Raspberry Pi OS (32-bit)
Enable SSH
Set Pi username/password
Add WiFi credentials
Flash SD → insert into UGV
LED Indicators on Rover:
Red LED = power
Green LED = OS successfully loaded

2️⃣ Connect to UGV WiFi + Use Control Panel
UGV generates its own WiFi network:
UGV-XXXX
Once connected, open control dashboard:
👉 http://192.168.4.1
This allows basic motion (Forward, Backward, Left, Right).
3️⃣ SSH Into the Raspberry Pi
First find Pi IP using:
ping 192.168.4.2
ping 192.168.4.3
Whichever replies → SSH into it:
ssh pi@192.168.4.x
4️⃣ Install Required Packages on Pi
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
5️⃣ Create Rover Project Directory
mkdir rover
cd rover
mkdir motor_control marvelmind autonomous
touch motor_control/motor.py
touch marvelmind/beacon_reader.py
touch autonomous/navigation.py
Final directory structure:
/rover
   /motor_control
        motor.py
   /marvelmind
        beacon_reader.py
   /autonomous
        navigation.py
🧩 Code Files
These were developed during the setup phase.
motor_control/motor.py
Handles sending movement commands to Waveshare UGV motor server.
import socket
import time

HOST = "192.168.4.1"
PORT = 5001

def send_command(cmd):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send(cmd.encode())
        s.close()
    except Exception as e:
        print("Error sending command:", e)

def test_motors():
    print("Testing forward...")
    send_command("forward")
    time.sleep(1)

    print("Testing backward...")
    send_command("backward")
    time.sleep(1)

    print("Testing left...")
    send_command("left")
    time.sleep(1)

    print("Testing right...")
    send_command("right")
    time.sleep(1)

if __name__ == "__main__":
    test_motors()
marvelmind/beacon_reader.py
Placeholder for reading UWB position data.
# Placeholder for Marvelmind UWB beacon integration

def read_position():
    # TODO: Extract X/Y/Z from Marvelmind hedgehog
    return {"x": None, "y": None, "z": None}
autonomous/navigation.py
Future navigation logic.
# Placeholder for navigation logic

def navigate_to(x_target, y_target):
    # TODO: Compute motion commands using position data
    pass
📡 Marvelmind System Setup
Completed steps:
Installed Marvelmind SW Pack + Firmware
Reviewed entire Marvelmind manual
Understood the system components:
Fixed beacons form positioning grid
Modem sends data to dashboard
Mobile beacon returns real-time position
Planned beacon layout:
Corners of a room / barn
Planned modem location:
Connected to laptop first
Later connected directly to Pi
⚠️ Problems Encountered
1. UGV Firmware / Motor API Issues
UGV disconnects from WiFi during sharp right turns
Official UGV01 Pi image is missing
Motor server sometimes rejects commands
2. Raspberry Pi Integration Challenges
SSH occasionally fails until IP is confirmed
Must manually configure filesystem since UGV image missing
3. Marvelmind Uncertainties
Unsure whether Pi or laptop should serve as modem host
Need to test USB serial communication
Must integrate NIA API for position streaming
📊 Results So Far
✔ Flashed Raspberry Pi OS
✔ Enabled SSH + connected via UGV WiFi
✔ Successfully accessed rover control panel
✔ Created full project file structure
✔ Wrote initial motor-control Python file
✔ Installed Marvelmind software + read full manual
✔ Planned integration of UWB → Pi → Motor logic
🎯 Future Goals
Implement reliable motor control using correct Waveshare API
Connect Marvelmind modem → Pi directly
Parse X/Y/Z coordinates through Python
Combine localization + movement → autonomous navigation
Deploy multiple beacons + multiple rovers
Add drone subsystem for aerial mapping
📎 Appendix (Documentation Required by Instructor)
A. Terminal Logs Included
ping results (Pi discovery)
SSH login logs
apt installation logs
motor.py test logs (“connection refused”)
B. Images Documented
UGV control panel screenshot
LED indicators
Folder structure outputs
Failed connection attempts
C. Software Installed
Raspberry Pi Imager
Marvelmind SW Pack v8.101
Python3, pip, venv, git
Marvelmind Dashboard
NIA tools
D. System Requirements
Laptop with WiFi
16GB+ microSD card
UGV01 powered + stable WiFi hotspot
Marvelmind Modem + 3 fixed beacons
👤 Author
Falih Faizal
UGA VIPR Agricultural Robotics Research
Fall 2025
---
# 🛠 **Software Used**


- Marvelmind SW Pack (v8.101 – Jan 2025)  
- NIA Positioning Engine  
- Marvelmind Dashboard + API tools  
- Raspberry Pi Imager  
- macOS Terminal + Windows CMD/PowerShell  
- Required Pi Packages:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y



Fixed Beacons  →  UWB Modem  →  Laptop (Marvelmind Dashboard)
                                     ↓ (future)
                            Raspberry Pi on Rover
                                     ↓
                              Motor Controller
                                     ↓
                                 UGV Movement


