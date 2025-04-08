class MyDeque:
    """
    Deque has the ability to behave like both stack and queue.
    It has features if LIFO and FIFO

    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeRear(self):
        self.items.pop(0)

    def removeFront(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)


dq = MyDeque()
dq.addFront("Hello")
dq.addFront("World")
dq.addRear("Od")
dq.show()
