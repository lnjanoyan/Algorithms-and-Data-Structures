import math


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self, capacity=10, load_factor=0.7):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity
        self.load_factor = load_factor

    def _hash(self, key):
        hash_value = 31  # random prime value

        # 2. Multiply the hash value by another prime number.
        for char in key:
            hash_value = (hash_value * 37) + ord(char)
        hash_value %= self.capacity
        return hash_value

    def put(self, key, value):
        if self.size > self.capacity * 0.7:
            new_capacity = self._next_prime(2 * self.size)
            self.rehash(new_capacity)

        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key, value)
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = ListNode(key, value)
        self.size += 1

    def rehash(self, new_capacity):
        new_buckets = [None] * new_capacity

        for bucket in self.buckets:
            current = bucket
            while current:
                index = self._hash(current.key)
                if not new_buckets[index]:
                    new_buckets[index] = ListNode(current.key, current.value)
                else:
                    new_node = ListNode(current.key, current.value)
                    new_node.next = new_buckets[index]
                    new_buckets[index] = new_node
                current = current.next

        self.capacity = new_capacity
        self.buckets = new_buckets

    def _next_prime(self, n):
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

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key '{key}' not found in the map")

    def delete(self, key):
        index = self._hash(key)
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

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        return self.size


string_map = HashMap(10)
string_map["a"] = 5
string_map["b"] = 8
string_map.put('key1','value1')
string_map.delete('key1')
string_map["c"] = 12
print("'c' : ", string_map.get('c'))
print("After insertions:", string_map.capacity)

for i in range(20):
    string_map[f"item_{i}"] = i

print("After rehashing:", string_map.capacity)
