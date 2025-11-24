# 🤖 UGV Ground Robot Project  
### **Autonomous Indoor Navigation Using Raspberry Pi + Marvelmind UWB**

---

## 📌 Overview  
This project develops an **indoor autonomous rover** that combines:

- A **Waveshare UGV01** ground robot base  
- A **Raspberry Pi** used for motor control + computation  
- A **Marvelmind Indoor GPS (UWB)** localization system  
- Python scripts for motor control + future autonomous navigation  

Eventually, the rover will:  
- Receive **real-time (X, Y, Z)** coordinates from a mobile beacon  
- Compute how to reach a target location  
- Drive **autonomously** without human input  

---

## 🧰 Hardware Used  
- Waveshare UGV01 Robot Base  
- Raspberry Pi (UGV Compute Module)  
- Marvelmind **Fixed Beacons** (#1, #2, #3)  
- Marvelmind **Mobile Beacon** (mounted on rover)  
- Marvelmind **Modem**  
- Laptop (Marvelmind Dashboard + SSH to Pi)  
- MicroSD card  
- Power adapters  

---

## 🛠 Software Used  
- Marvelmind SW Pack (v8.101 — Jan 2025)  
- NIA Positioning Engine  
- Marvelmind Dashboard + API Tools  
- Raspberry Pi Imager  
- Terminal (macOS) / CMD (Windows)  
- Pi development packages:  
  ```bash
  sudo apt update && sudo apt upgrade -y
  sudo apt install python3-pip python3-venv git -y
