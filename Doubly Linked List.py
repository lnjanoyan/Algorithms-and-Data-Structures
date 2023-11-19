class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop_back(self):
        if not self.tail:
            return
        tmp = self.tail.prev
        tmp.next = None
        self.tail = tmp

    def size(self):
        size = 1
        curr = self.head
        if not self.head:
            return 0
        while curr != self.tail:
            size += 1
            curr = curr.next
        return size

    def push_front(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            self.tail = new
        else:
            self.head.prev = new
            new.next = self.head
            self.head = new

    def pop_front(self):
        if not self.tail:
            return
        self.head.next.prev = None
        self.head = self.head.next
        self.head.prev = None

    def insert(self, pos, data):
        new = Node(data)
        if pos > self.size():
            raise ValueError
        if pos == 0:
            self.push_front(data)
        elif pos == self.size():
            self.push_back(data)
        else:
            curr = self.head
            for i in range(pos - 1):
                curr = curr.next
            tmp = curr.next
            curr.next = new
            new.prev = curr
            new.next = tmp
            tmp.prev = new

    def erase(self, pos):
        if pos >= self.size():
            raise ValueError
        if not self.head:
            return
        if pos == self.size() - 1:
            self.pop_back()
        elif pos == 0:
            self.pop_front()
        else:
            curr = self.head
            for i in range(pos):
                curr = curr.next
            tmp = curr.next
            tmp.prev = curr.prev
            curr.prev.next = tmp
            curr.next = None
            curr.prev = None

    def clear(self):
        self.head, self.tail = None, None

    def is_empty(self):
        return self.head is None

    def reverse(self):
        curr = self.head
        while curr:
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev
        return self.tail

    def sort(self, head):
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tmp = slow.next
        slow.next = None

        left = self.sort(head)
        right = self.sort(tmp)

        return merge(left, right)


def merge(list1, list2):
    new = Node(None)
    res = new
    while list1 and list2:
        if list1.data < list2.data:
            new.next = list1
            list1 = list1.next
        else:
            new.next = list2
            list2 = list2.next
        new = new.next

    new.next = list1 if list1 else list2

    return res.next


def print_dll_from_start(head):
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print('\n')


def print_dll_from_end(tail):
    curr = tail
    while curr:
        print(curr.data, end=' ')
        curr = curr.prev
    print('\n')


dll = DLL()
dll1 = DLL()

dll.push_back(1)
dll.push_back(4)
dll.push_back(2)
dll.push_back(8)
dll1.push_back(6)

dll1.push_front(5)

dll.pop_back()
dll.insert(2, 3)
dll.insert(4, 5)
dll.erase(2)
dll.push_back(7)

print('List 1 size:', dll.size())
print_dll_from_start(dll.head)
print_dll_from_start(dll1.head)
print('Sorted:')
print_dll_from_start(dll.sort(dll.head))

print('Merged:')
m = merge(dll.head, dll1.head)
print_dll_from_start(m)

print('Reversed:')
print_dll_from_start(dll.reverse())
