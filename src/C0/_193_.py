# Parallel Computing

# Boot camp
# Semaphore

import threading


class Semaphore:
    def __init__(self, max_available):
        self.cv = threading.Condition()  # I think this can turn to either an acquire or release.
        self.MAX_AVAILABLE = max_available  # max_available = max_available
        self.taken = 0  # taken = 0

    def acquire(self):
        self.cv.acquire()  # so creates an acquire
        while self.taken == self.MAX_AVAILABLE:  # if all the permits are taken, wait
            self.cv.wait()
        self.taken += 1  # increase permits being tracked
        self.cv.release()  # release

    def release(self):
        self.cv.acquire()  # picks a thread
        self.taken -= 1  # adds a permit
        self.cv.notify()  # notifies a blocked acquire probably
        self.cv.release()  # releases it


# implement synchronization for two interleaving threads.
# t1 prints odd numbers from 1 to 100
# t2 prints even numbers from 1 to 100

# using threads, make them write the numbers from 1 to 100 in sequence
# brute force solution is to use a lock that is repeatedly captured by the threads
# but this causes a busy locking anti pattern


class MonitorODDEVEN(threading.Condition):
    EVEN_TURN = False
    ODD_TURN = True

    def __init__(self):
        super().__init__()
        self.turn = self.ODD_TURN  # :D

    def wait_turn(self, last_turn):
        with self:
            while self.turn != last_turn:
                self.wait()

    def toggle_turn(self):
        with self:
            self.turn ^= True
            self.notify()


class OddProducer(threading.Thread):
    def __init__(self, monitor):
        super().__init__()
        self.monitor = monitor

    def run(self) -> None:
        for i in range(1, 101, 2):
            self.monitor.wait_turn(MonitorODDEVEN.ODD_TURN)
            print(i)
            self.monitor.toggle_turn()


class EvenProducer(threading.Thread):
    def __init__(self, monitor):
        self.monitor = monitor

    def run(self) -> None:
        for i in range(2, 101, 2):
            self.monitor.wait_turn(MonitorODDEVEN.EVEN_TURN)
            print(i)
            self.monitor.toggle_turn()

# wait - > notify