class ListNode:
    def __init__(self, val = 0, key = 0, left=None, right=None):
        self.val = val
        self.key = key
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.front = ListNode()
        self.back = ListNode()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(key)
        self.insert(key)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
            self.cache[key].val = value
            self.insert(key)
            return
        self.cache[key] = ListNode(value, key)
        self.insert(key)

        if len(self.cache) > self.capacity:
            lru = self.back.right
            self.remove(lru.key)

            del self.cache[lru.key]
        return 
        

    def remove(self, key):
        node = self.cache[key]
        if node.left and node.right:
            node.left.right = node.right
            node.right.left = node.left
        elif node.left:
            node.left.right = None
            self.front.left = node.left

        elif node.right:
            node.right.left = None
            self.back.right = node.right
            node.right = None
        elif not node.left and not node.right:
            self.back.right = None
            self.front.left = None
        return

    def insert(self, key):
        mru = self.cache[key]
        if not self.front.left:
            self.front.left = mru
            self.back.right = mru
            return
        second = self.front.left
        second.right = mru
        mru.right = None
        mru.left = second
        self.front.left = mru
        return


        