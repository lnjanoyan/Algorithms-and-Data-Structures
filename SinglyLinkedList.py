class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def pop_back(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None

    def insert(self, pos, data):
        if pos > self.size():
            raise IndexError
        new_node = Node(data)
        curr = self.head
        if pos == 0:
            new_node.next = curr
            self.head = new_node
            return

        for i in range(pos - 1):
            if curr and curr.next:
                curr = curr.next
            else:
                raise ReferenceError
        tmp = curr.next
        curr.next = new_node
        new_node.next = tmp

    def erase(self, pos):
        if not self.head:
            return
        if pos >= self.size():
            raise ValueError
        else:
            curr = self.head
            if pos == 0:
                self.head = self.head.next
                return
            for i in range(pos - 1):
                if curr.next:
                    curr = curr.next
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = None

    def clear(self):
        self.head = None

    def size(self):
        if not self.head:
            return 0
        curr = self.head
        size = 1
        while curr.next:
            size += 1
            curr = curr.next
        return size

    def reverse_recursive(self, head):
        if not head or not head.next:
            return head
        tmp = self.reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return tmp

    def reverse_iterative(self):
        curr = self.head
        next_ind = None
        tmp = None
        while curr:
            next_ind = curr.next
            if curr == self.head:
                curr.next = None
            else:
                curr.next = tmp
            tmp = curr
            curr = next_ind
        return tmp

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
    if not list1:
        return list2
    if not list2:
        return list1
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


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print('\n')


ll = LinkedList()
ll2 = LinkedList()

ll.insert(0, 0)
ll.push_back(1)
ll.push_back(2)
ll.push_back(5)
ll.insert(1, 3)
ll.insert(4, 6)
ll.insert(2, 10)
ll.erase(2)
ll.pop_back()

print('List1 :')
print_list(ll.head)
print('Size:', ll.size())
# ll.clear()

ll2.push_back(9)
ll2.push_back(7)
ll2.push_back(4)

print('List2:')
print_list(ll2.head)

print('List1 - After sort method:')
print_list(ll.sort(ll.head))

print('\nList1 - After recursive reverse method:')
print_list(ll.reverse_recursive(ll.head))

print('List2 - After iterative reverse  method:')
print_list(ll2.reverse_iterative())


# def split_linked_list(self, head):
#     slow = head
#     fast = head.next
#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#     tmp = slow.next
#     slow.next = None
#     return [head, tmp]