import threading

class SafeQueue:
    def __init__(self):
        self.data = []
        self.lock = threading.RLock()

    def push(self, item):
        with self.lock:
            self.data.append(item)

    def pop(self):
        with self.lock:
            if self.data:
                return self.data.pop(0)


queue = SafeQueue()

def producer():
    for i in range(5):
        queue.push(i)


def consumer():
    for _ in range(5):
        print("Получено:", queue.pop())


t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()
t1.join()
t2.join()