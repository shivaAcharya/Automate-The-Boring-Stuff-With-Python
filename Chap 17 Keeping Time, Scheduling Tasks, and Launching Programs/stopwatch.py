#! python3
# stopwatch.py - A simple stopwatch program

import time

#Provide User Guidance

print('Press ENTER to begin stopwatch. Press ENTER again to mark a lap. Ctrl+C to quit')
input()
print('Started')
startTime = time.time()
lastTime = startTime
numLap = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap#%s, Laptime: %s, Total Time: %s' %(numLap, lapTime, totalTime))
        lastTime = time.time() #reset lastTime
        numLap += 1
except KeyboardInterrupt:
    print('\nDone')
