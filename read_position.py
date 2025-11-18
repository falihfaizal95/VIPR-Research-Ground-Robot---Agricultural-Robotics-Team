from marvelmind import MarvelmindHedge
import time
from config import MODEM_PORT

hedge = MarvelmindHedge(tty=MODEM_PORT, adr=1, debug=False)
hedge.start()

print("Reading Marvelmind X,Y,Z...")

try:
    while True:
        pos = hedge.position()
        if pos:
            x, y, z = pos[1], pos[2], pos[3]
            print(f"X={x:.2f},  Y={y:.2f},  Z={z:.2f}")
        time.sleep(0.05)

except KeyboardInterrupt:
    hedge.stop()
