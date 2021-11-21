import time
import sys

space = " "
try:
    while True:
        for i in range(0, 4, 1):
            print(space * int(i) + "********")
            time.sleep(0.1)
        for i in range(4, 0, -1):
            print(space * int(i) + "********")
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
