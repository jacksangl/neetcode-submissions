class ListNode:
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
        self.left.right = self.right
        self.right.left = self.left

    # adds to front
    def add(self, node):
        oldmru = self.right.left
        oldmru.right = node
        node.left = oldmru
        node.right = self.right
        self.right.left = node
    
    # removes from list
    def remove(self, node):
        left, right = node.left, node.right
        left.right = right
        right.left = left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.add(self.cache[key])
    
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return
        
        self.cache[key] = ListNode(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.right
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)