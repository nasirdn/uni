import time
import threading

event = threading.Event()

def setter():
    time.sleep(3)
    event.set()


def waiter():
    event.wait()
    print("Event occurred")


def watcher():
    while not event.is_set():
        print("Event did not occur")
        time.sleep(1)


threads = [
    threading.Thread(target=setter),
    threading.Thread(target=waiter),
    threading.Thread(target=watcher),
]

for t in threads:
    t.start()
for t in threads:
    t.join()