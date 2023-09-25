import threading

class Counter(threading.Thread):
    counter = 0
    rounds = 100000
    lock = threading.Lock()

    def run(self):
        for _ in range(self.rounds):
            with self.lock:
                self.counter += 1

def main():
    thread1 = Counter()
    thread2 = Counter()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    total_counter = thread1.counter + thread2.counter
    print("Total counter:", total_counter)

main()

# I get the 200000 value every time I run this code, never got another result.