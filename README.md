🚗 UGV Ground Robot Project
Autonomous Indoor Navigation Using Raspberry Pi + Marvelmind UWB
📌 Project Overview
This project develops an indoor autonomous rover that uses:
A Waveshare UGV01 ground robot base
A Raspberry Pi for motor logic and computation
A Marvelmind Indoor GPS (UWB) system for precise localization
Python scripts for motor control and future autonomous navigation
Eventually, the rover will:
Receive real-time position data (X, Y, Z) from a mobile beacon
Compute how to reach a target coordinate
Drive autonomously without human input
🧰 Hardware Used
Waveshare UGV01
Raspberry Pi (UGV Compute Module)
Marvelmind stationary beacons (fixed beacons #1, #2, #3)
Marvelmind mobile beacon (mounted on rover)
Marvelmind modem
Laptop (for Marvelmind Dashboard + SSH into Pi)
MicroSD card
Power adapters
🧪 Software Used
Marvelmind SW Pack (v8.101 – Jan 2025)
Firmware for all beacons
NIA positioning engine
Marvelmind Dashboard + API tools
Raspberry Pi Imager
Used to install Raspberry Pi OS
Used to enable SSH + preconfigure WiFi
macOS Terminal / Windows CMD
SSH access
Debugging & networking tools
Pi Development Packages Installed
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
⚙️ System Setup Summary
### 1. Flash Raspberry Pi OS
Using Raspberry Pi Imager:
Selected Raspberry Pi OS (32-bit recommended for compatibility)
Enabled SSH
Set username/password
Added WiFi credentials
Flashed SD card → inserted into rover
(After boot, Pi LED turned RED + GREEN = OS loaded)
### 2. Connect to UGV WiFi + Access Control Panel
UGV creates its own WiFi hotspot:
Connect laptop → network UGV-XXXX
Open the control panel:
http://192.168.4.1
This dashboard allows basic manual movement (Forward, Left, Right, etc.).
### 3. SSH into the Raspberry Pi
Once connected to UGV WiFi:
ssh pi@192.168.4.2
Default password:
12345678
After login → Confirmed Pi is accessible.
### 4. File Structure Created on Raspberry Pi
mkdir rover
cd rover
mkdir motor_control marvelmind autonomous
touch motor_control/motor.py
touch marvelmind/beacon_reader.py
touch autonomous/navigation.py
🧩 Code Files
### motor_control/motor.py
Purpose: future control of rover motors programmatically
(Placeholder – hardware API not functional yet under generic Pi OS)
print("Testing forward...")
print("Testing backward...")
print("Testing left turn...")
print("Testing right turn...")
### marvelmind/beacon_reader.py
Purpose:
Will receive X, Y, Z coordinates from the Marvelmind modem
Parse data and forward it to navigation logic
(Placeholder)
# To be implemented: Interface with Marvelmind serial/USB stream
### autonomous/navigation.py
Purpose:
Will compute motor commands based on target coordinates
Will integrate beacon_reader outputs
(Placeholder)
# Future path planning algorithm:
# Move rover toward (x_target, y_target)
🛰️ Marvelmind System Setup
What Has Been Done
✔ Downloaded latest NIA + firmware pack
✔ Read complete Marvelmind documentation
✔ Understood modem–beacon–mobile beacon relationships
✔ Decided system layout:
Fixed beacons at room corners
Modem connected to laptop (for debugging)
Mobile beacon mounted on rover
Next Step
Integrate modem → Raspberry Pi via USB or UART.
⚠️ Problems Encountered
1. Waveshare Firmware Issues
Rover disconnects from WiFi when steering hard right
Movement commands sometimes cause system to freeze
The UGV01 motor API is unavailable under standard Raspberry Pi OS
(because Waveshare’s custom OS image is missing)
2. UGV01 Pi Image Missing
The official Waveshare UGV01 Pi image no longer exists online
Website currently shows: "Resources under urgent production"
Control panel works but no motor controller backend on Pi
Can’t send motor PWM commands through Linux API yet
3. Marvelmind Integration Hurdles
Modem ↔ Pi connection method undecided (USB? UART?)
Need to confirm serial port visibility on Pi
Must parse hedgehog (mobile beacon) position packets
Multi-beacon scalability needs testing
📈 Results So Far
Raspberry Pi OS successfully flashed
Full SSH access working
UGV WiFi + control panel accessible
File structure + placeholder control scripts created
Marvelmind manual read and system designed
Networking tests confirm:
192.168.4.1 = UGV control
192.168.4.2 = Raspberry Pi
192.168.4.3 = Your laptop
🚀 Future Steps
Implement correct motor-control interface using Waveshare’s actual API
Flash official UGV01 OS once Waveshare releases it
Get Marvelmind modem streaming coordinates to Pi
Integrate navigation algorithm based on (X, Y) targets
Scale to multi-beacon + multi-rover environment
Add drone subsystem for aerial mapping
📎 Appendix
A. Terminal Logs
Update & Install Packages:
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
Directory Tree:
/rover
  ├── motor_control/
  │    └── motor.py
  ├── marvelmind/
  │    └── beacon_reader.py
  └── autonomous/
       └── navigation.py
Ping tests:
ping 192.168.4.1   # UGV control
ping 192.168.4.2   # Raspberry Pi
ping 192.168.4.3   # Laptop (self-check)
Motor script test:
python3 motor_control/motor.py
Output:
Error sending command: [Errno 111] Connection refused
B. Images You Should Add to GitHub
(Place in a /docs folder if needed)
UGV control panel screenshot
Rover interior with Raspberry Pi
Marvelmind dashboard screenshot
Pi boot LED indicators (red+green)
C. SSH Log
The authenticity of host '192.168.4.2' can't be established.
Are you sure you want to continue connecting (yes/no)? yes
pi@192.168.4.2's password:
Linux ugv-pi 6.1.12 ... aarch64
