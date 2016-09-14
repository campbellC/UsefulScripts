import threading
import time
lock = threading.Lock()
lock.acquire()
def func():
    global lock
    with lock:
        print "hi"

timer = threading.Timer(1,func)
timer.daemon = True
timer.start()

time.sleep(2)
print "hi"
timer.cancel()
