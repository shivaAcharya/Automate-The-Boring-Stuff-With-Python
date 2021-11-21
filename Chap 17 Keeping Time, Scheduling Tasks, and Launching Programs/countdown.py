#! python 3
# Program to countdown and play alarm after the time is up.

import time, subprocess

timeleft = 5

while timeleft > 0:
    print(timeleft, end='')
    time.sleep(1)
    timeleft -= 1
    

subprocess.Popen(['start', 'alarm.wav'], shell = True)