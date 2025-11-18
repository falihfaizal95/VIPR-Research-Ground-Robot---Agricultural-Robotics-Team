import socket 
import json 
from config import PI_IP, PORT 

# choose your target coordinate here
target_x = 2.5
target_y = 1.75

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((PI_IP, PORT))

msg = json.dumps({"x": target_x, "y": target_y})
sock.sendall(msg.encode())

print(f"Sent target: X={target_x}, Y={target_y}")
sock.close()


