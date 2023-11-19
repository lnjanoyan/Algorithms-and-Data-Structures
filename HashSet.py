import math
import SinglyLinkedList


class HashSet:
    def __init__(self, capacity=10, load_factor=0.7):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity
        self.load_factor = load_factor
        # self.curr_load_factor = self.size / self.capacity

    def _hash_function(self, key):
        # random logic
        hash_value = key
        hash_value += self.capacity
        hash_value = (hash_value ** 2) % self.capacity

        return hash_value

    def insert(self, key):
        if self.size > self.capacity * self.load_factor:
            new_capacity = self._get_next_prime(2 * self.size)
            self.rehash(new_capacity)

        index = self._hash_function(key)
        if not self.buckets[index]:
            self.buckets[index] = SinglyLinkedList.Node(key)
        else:
            current = self.buckets[index]
            while current:
                if current.data == key:
                    return
                if current.next is None:
                    break
                current = current.next
            # key-n chka verjum em avelacnum listi
            current.next = SinglyLinkedList.Node(key)
        self.size += 1

    def rehash(self, new_capacity):
        new_buckets = [None] * new_capacity

        for bucket in self.buckets:
            current = bucket
            while current:
                index = self._hash_function(current.data)
                if not new_buckets[index]:
                    new_buckets[index] = SinglyLinkedList.Node(current.data)
                else:
                    new_node = SinglyLinkedList.Node(current.data)
                    new_node.next = new_buckets[index]
                    new_buckets[index] = new_node
                current = current.next

        self.capacity = new_capacity
        self.buckets = new_buckets

    def _get_next_prime(self, n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        while not is_prime(n):
            n += 1
        return n

    def search(self, key):
        index = self._hash_function(key)
        current = self.buckets[index]
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def delete(self, key):
        index = self._hash_function(key)
        current = self.buckets[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def __contains__(self, key):
        return self.search(key)

    def __len__(self):
        return self.size


hs = HashSet(10)
hs.insert(5)
hs.insert(10)
hs.insert(12)
hs.insert(15)
hs.insert(4)
hs.insert(8)

print(f'{10} found in HS: ', hs.search(10))
print(f'{12} found in HS: ', 10 in hs)
print("Before rehashing:", hs.capacity)
for i in range(20, 30):
    hs.insert(i)
print("After rehashing:", hs.capacity)
