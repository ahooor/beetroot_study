# Implement a queue using a singly linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            removed = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed.data

    def front_element(self):
        if self.is_empty():
            return None
        else:
            return self.front.data

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            current = self.front
            queue_str = ""
            while current:
                queue_str += str(current.data) + " -> "
                current = current.next
            return queue_str[:-4]

if __name__ == "__main":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue:", queue)
    print("Front element:", queue.front_element())

    dequeued = queue.dequeue()
    print("Dequeued element:", dequeued)
    print("Queue after dequeue:", queue)
