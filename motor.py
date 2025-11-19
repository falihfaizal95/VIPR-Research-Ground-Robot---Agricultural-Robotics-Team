import socket
import json
import time

HOST = "127.0.0.1"
PORT = 8888

def send_cmd(cmd):
    """Send a JSON command to the UGV base."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(json.dumps(cmd).encode())
    except Exception as e:
        print("Error sending command:", e)

def forward(speed=0.5):
    send_cmd({"T": 1, "L": speed, "R": speed})

def backward(speed=0.5):
    send_cmd({"T": 1, "L": -speed, "R": -speed})

def left(speed=0.5):
    send_cmd({"T": 1, "L": -speed, "R": speed})

def right(speed=0.5):
    send_cmd({"T": 1, "L": speed, "R": -speed})

def stop():
    send_cmd({"T": 1, "L": 0, "R": 0})

def test_movement():
    print("Testing forward...")
    forward(0.4)
    time.sleep(1)
    stop()

    print("Testing backward...")
    backward(0.4)
    time.sleep(1)
    stop()

    print("Testing left turn...")
    left(0.4)
    time.sleep(1)
    stop()

    print("Testing right turn...")
    right(0.4)
    time.sleep(1)
    stop()

if __name__ == "__main__":
    test_movement()
