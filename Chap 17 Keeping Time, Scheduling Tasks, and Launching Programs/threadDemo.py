import threading, time

print('Start of program!')

def takeNap():
    time.sleep(2)
    print('Wake Up!')

threadObj = threading.Thread(target=takeNap)
threadObj.start()

print('End of Program')