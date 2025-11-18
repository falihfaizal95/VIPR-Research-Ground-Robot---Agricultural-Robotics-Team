🐔 Autonomous Indoor Navigation Rover
Raspberry Pi • Marvelmind Beacons • ROS/Gazebo • VIPR Agricultural Robotics Lab
📌 Overview
This project focuses on developing an autonomous indoor navigation rover for agricultural environments, specifically poultry houses. The goal is to build a system that can localize, navigate, and eventually perform automated tasks (monitoring, data collection, welfare checks) in low-visibility indoor settings where GPS is unreliable.
The rover uses:
Raspberry Pi (primary onboard computer)
Marvelmind Indoor GPS beacons for high-precision positioning
Waveshare UGV Rover platform
ROS + Gazebo for simulation, visualization, and testing
Custom Python scripts for reading positions, controlling motors, and executing navigation tasks
This README outlines the system design, setup process, file structure, and ongoing development roadmap.
🧠 Project Goals
Achieve real-time local positioning using Marvelmind’s ultrasonic beacon system.
Stream X/Y/Z coordinate data to the Raspberry Pi.
Control the rover through Python and ROS nodes.
Run simulated navigation in Gazebo before deploying onto the physical rover.
Build a modular framework for future add-ons (environment monitoring, vision, path planning, etc.).
