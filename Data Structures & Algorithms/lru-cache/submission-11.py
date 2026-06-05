class ListNode:
    def __init__(self, val = -1, left = None, right = None, key = -1):
        self.val = val
        self.left = left
        self.right = right
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.lru = ListNode()
        self.mru = ListNode()
        self.lru.left, self.mru.right = self.mru, self.lru

    def remove(self, node):
        left, right = node.left, node.right
        node.left = node.right = None
        left.right, right.left = right, left
    
    def add(self, node):
        oldmru = self.mru.right
        oldmru.left = self.mru.right = node
        node.left, node.right = self.mru, oldmru

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self.remove(self.nodes[key])
        self.add(self.nodes[key])
        return self.nodes[key].val
    
    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key].val = value
            self.remove(self.nodes[key])
            self.add(self.nodes[key])
            return

        self.nodes[key] = ListNode(value, None, None, key)
        self.add(self.nodes[key])
        if len(self.nodes) > self.capacity:
            least = self.lru.left
            self.remove(least)
            del self.nodes[least.key]
        
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)