"""
Autonomous Navigation Logic
Uses:
- Motor controller (motor.py)
- UWB position data (beacon_reader.py)
"""

from rover.motor_control.motor import forward, backward, left, right, stop
from marvelmind.beacon_reader import get_position
import time

def goto_target(x_target, y_target):
    """
    Placeholder navigation loop.
    Will eventually:
    - Compare current beacon coordinates to target
    - Compute direction + send motor commands
    """
    print(f"Navigating to ({x_target}, {y_target})...")

    for _ in range(5):
        pos = get_position()
        print("Current position:", pos)
        forward(0.3)
        time.sleep(0.5)

    stop()
    print("Arrived.")

if __name__ == "__main__":
    goto_target(1.0, 1.0)
