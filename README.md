# 🐔 Autonomous Indoor Navigation Rover  
### Raspberry Pi • Marvelmind Beacons • UGV Platform

## Overview
This project develops an **autonomous indoor navigation rover** for agricultural environments (specifically poultry houses). Since GPS does not work indoors, the rover uses a **Marvelmind Indoor GPS** system for centimeter-level localization, a **Raspberry Pi** as the onboard computer, and a **Waveshare UGV** platform for mobility.  
The system combines **real-time localization**, **motor control**, and **ROS-based navigation**, with Gazebo used for simulation and testing.

---

## Project Goals
- Stream accurate **X/Y/Z** positions from Marvelmind beacons to the Raspberry Pi  
- Control rover movement using Python (GPIO/serial)  
- Build a ROS/Gazebo simulation environment  
- Implement autonomous waypoint navigation  
- Develop a modular codebase for future robotics research

---

## System Architecture

Marvelmind Beacons → Modem → Raspberry Pi → Python/ROS Navigation Scripts
↓
Waveshare UGV Rover



**Marvelmind System**  
- Stationary beacons map the environment  
- Mobile beacon on rover provides real-time coordinates  
- Modem sends location data via USB → Pi

**Raspberry Pi**  
- Reads Marvelmind serial packets  
- Publishes position data to ROS topics  
- Sends motor commands to the UGV

---

## Repository Structure

poultry-rover/
│
├── marvelmind/
│ ├── hedgehog.py # Parse Marvelmind packets
│ ├── beacon_listener.py # Streams coordinates to terminal or ROS topic
│ └── README.md
│
├── navigation/
│ ├── controller.py # Controls rover movement
│ ├── path_planning.py # Waypoint following logic
│ ├── utils.py
│
├── rover/
│ ├── ugv_driver.py # Low-level motor driver
│ ├── manual_control.py # For testing motor responses
│ └── hardware_tests/
│
├── simulation/
│ ├── launch/
│ │ └── gazebo.launch # Starts Gazebo simulation
│ ├── models/
│ └── worlds/
│
└── README.md




---

## Setup Instructions

### 1. Flash Raspberry Pi OS
Use Raspberry Pi Imager. Enable:
- SSH  
- Wi-Fi  
- Username/password  

Insert SD → Boot the Pi.

---

### 2. Install Dependencies

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip python3-serial git ros-humble-desktop-full
pip3 install pyserial


Clone this repository:
git clone https://github.com/<your-username>/poultry-rover.git
cd poultry-rover
3. Connect Marvelmind Modem
Check if detected:
ls /dev/ttyACM*
Run listener:
python3 marvelmind/beacon_listener.py
You should see streaming position data.
4. Test Rover Controls
python3 rover/manual_control.py
Common keys:
w → forward
s → stop
a / d → turn
x → reverse
5. Autonomous Navigation
Run Gazebo simulation:
ros2 launch simulation gazebo.launch
Start navigation node:
ros2 run navigation controller.py
Example waypoint list:
waypoints = [(1.2, 0.5), (3.0, -1.0), (4.2, 2.4)]
Current Progress
✔ Marvelmind beacon mapping
✔ Coordinate streaming to Raspberry Pi
✔ Manual UGV control
⬜ Integration with ROS navigation stack
⬜ Autonomous waypoint execution
⬜ Full Gazebo simulation
Troubleshooting Notes
Solid red LED on Pi = power OK.
No green LED = SD card missing or OS not installed.
Some SD cards shipped with corrupted files — reflash with Raspberry Pi Imager.
Marvelmind modem may appear as /dev/ttyUSB0 instead of /dev/ttyACM0.
Future Work
Add obstacle detection sensors (camera, lidar, ultrasonic)
Implement SLAM / Nav2
Add data logging and environmental monitoring
Deploy long-duration autonomous runs in poultry houses
Contributors
Muhammed Falih Faizal — Robotics & Navigation
VIPR Agricultural Robotics Lab

---

