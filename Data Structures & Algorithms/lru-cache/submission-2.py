class Node:
    def __init__(self, val = -1, key = -1, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self._remove(node)
        self._add(node)

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(self.cache[key])
            return
            
        node = Node(value, key)
        self.cache[key] = node
        self._add(node)

        if len(self.cache) > self.capacity:
            delete = self.head.next 
            self._remove(delete)
            del self.cache[delete.key]

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end

        self.tail.prev = node
        node.next = self.tail
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)