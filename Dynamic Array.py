class DynamicArray:
    def __init__(self, cap):
        self.space = [None for i in range(cap)]

    def get_size(self):
        size = 0
        for i in self.space:
            if i is not None:
                size += 1
        return size

    def get_capacity(self):
        return len(self.space)

    def push_back(self, elem):
        if self.get_size() >= self.get_capacity():
            self.resize()
        self.space[self.get_size()] = elem

    def pop_back(self):
        if self.get_size() != 0:
            self.space[self.get_size() - 1] = None
        else:
            print('No element for push back!')

    def insert_pos(self, pos, value):
        if pos <= self.get_size():
            if self.get_size() == self.get_capacity():
                self.resize()
            tmp = self.space[pos]
            self.space[pos] = value
            self.space[pos + 1] = tmp
            for i in range(self.get_size() + 1, pos + 3, -1):
                self.space[i] = self.space[i + 1]

        else:
            raise IndexError

    def insert_pos_count(self, pos, value, count):
        if pos <= self.get_size():
            if self.get_size() + count > self.get_capacity():
                self.resize()
            tail = self.space[pos:self.get_size()]
            for i in range(count):
                self.space[pos + i] = value
            for i in range(len(tail)):
                self.space[pos + count + i] = tail[i]
        else:
            raise IndexError

    def clear(self):
        for i in range(self.get_capacity()):
            self.space[i] = None

    def is_empty(self):
        return self.get_size() == 0

    def remove(self, pos):
        if pos == self.get_size():
            self.pop_back()
        elif pos < self.get_size():
            for i in range(pos, self.get_size()):
                self.space[i] = self.space[i + 1]
        else:
            print('No such position')

    def remove_with_count(self, pos, count):
        if pos < self.get_size() and pos + count < self.get_size():
            for i in range(pos, self.get_size()):
                self.space[i] = self.space[i + count]
        else:
            print('Invalid arguments')

    def insert_array(self, pos, array):
        count = len(array)
        if pos <= self.get_size():
            if self.get_size() + count > self.get_capacity():
                self.resize()
            tail = self.space[pos:self.get_size()]
            for i in range(count):
                self.space[pos + i] = array[i]
            for i in range(len(tail)):
                self.space[pos + count + i] = tail[i]
        else:
            raise IndexError

    def shrink_to_fit(self, percentage=2):
        if self.get_capacity() / self.get_size() > 3:
            new = [None] * (self.get_size() * percentage)
            for i in range(self.get_size()):
                new[i] = self.space[i]
            self.space = new

    def resize(self):
        new_space = [None] * len(self.space)
        for i in range(len(self.space)):
            new_space[i] = self.space[i]
        self.space = new_space

    def resize_count_val(self, count, val):
        if count < len(self.space):
            print('Size is less than previous array size')
            return
        new = [None for i in range(count)]
        for i in range(self.get_size()):
            new[i] = self.space[i]
        for i in range(self.get_size(), len(new)):
            new[i] = val
        self.space = new


arr = DynamicArray(15)
arr.push_back(1)
arr.push_back(2)
arr.push_back(4)
arr.insert_pos(2, 3)
arr.push_back(5)
arr.push_back(6)
arr.push_back(7)
print(arr.space)
print('size:', arr.get_size())
print('cap:', arr.get_capacity())
arr.remove(2)
# arr.clear()
arr.insert_pos_count(2, 6, 2)
# arr.resize_count_val(15,0)
arr.remove_with_count(1, 2)
arr.insert_pos_count(1, 0, 2)
arr.insert_array(1,[8,8,8])
arr.insert_pos(2, 0)
arr.shrink_to_fit()
print(arr.space)
print('size:', arr.get_size())
print(arr.is_empty())
print('cap:', arr.get_capacity())

