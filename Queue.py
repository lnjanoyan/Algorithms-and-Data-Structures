# commented lines are implementation of just index changing method
class Queue:
    def __init__(self):
        self.members = []
        # self.index = -1

    def size(self):
        return len(self.members)

    def front(self):
        if self.size() == 0:
            return 'Empty queue'
        return self.members[0]

    def push(self, value):
        # self.members[self.size():] = [value]
        self.members.append(value)

    def pop(self):
        if not self.is_empty():
            # self.members = self.members[1:]
            self.members.pop(0)
            # self.index += 1

        else:
            raise IndexError

    def is_empty(self):
        return self.size() <= 0


queue = Queue()
print('Before pop and push methods.')
print('Queue = ', queue.members)
print(f'Size: {queue.size()}, Is empty: {queue.is_empty()}, Front: {queue.front()}')
print('----------------------------------')
print('After pop and push methods.')
# queue.pop()
queue.push(0)
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()
print('Queue = ', queue.members)
print(f'Size: {queue.size()}, Is empty: {queue.is_empty()}, Front: {queue.front()}')
