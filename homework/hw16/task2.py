# Task 2

# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss. 
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss. 
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, 
# use getters and setters instead! You can refactor the existing code.


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []
        
    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker, setting_from_worker=False):
        if isinstance(worker, Worker) and worker not in self._workers:
            self._workers.append(worker)
            if not setting_from_worker:
                worker.boss = self

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            if self._boss and self in self._boss.workers:
                self._boss.workers.remove(self)

            self._boss = boss
            if self not in boss.workers:
                boss.add_worker(self, setting_from_worker=True)
        else:
            raise ValueError("boss must be an instance of Boss class")

big_boss = Boss(1, "John Doe", "Google")
w1 = Worker(1, "David Warner", "Google", big_boss)
w2 = Worker(2, "Christian Smith", "Google", big_boss)
w3 = Worker(3, "Michael Jordan", "Google", big_boss)


print([worker.name for worker in big_boss.workers])