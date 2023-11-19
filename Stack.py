class Stack:

    def __init__(self):
        self.members = []
        #self.index = -1

    def size(self):
        # return self.index + 1
        return len(self.members)

    def top(self):
        if self.size() == 0:
            return 'Empty stack'
        return self.members[-1]
        # return self.members[self.index]

    def push(self, value):
        # self.members[self.size():] = [value]
        self.members.append(value)
        #self.index += 1

    def pop(self):
        if not self.is_empty():
            # self.members = self.members[:-1]
            del self.members[-1]
            #self.index -= 1
        else:
            raise IndexError

    def is_empty(self):
        return self.size() <= 0


stack1 = Stack()
print('Before pop and push methods.')
print('Stack = ', stack1.members)
print(f'Size: {stack1.size()}, Is empty: {stack1.is_empty()}, Top: {stack1.top()}')
print('----------------------------------')
print('After pop and push methods.')
# stack1.pop()
stack1.push(0)
stack1.push(1)
stack1.push(2)
stack1.push(8)
stack1.push(55)
stack1.pop()
print('Stack = ', stack1.members)
print(f'Size: {stack1.size()}, Is empty: {stack1.is_empty()}, Top: {stack1.top()}')
