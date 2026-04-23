"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None

        cur = head
        cur_new = Node(cur.val)
        nodes = {}
        dummy = Node(0, cur_new)
        indx = 0
        while cur:
            nodes[cur] = cur_new
            cur = cur.next
            if cur:
                cur_new.next = Node(cur.val, None, None)
                cur_new = cur_new.next
            indx += 1 

        
        cur_new = dummy.next
        cur = head
    
        while cur_new:
            if cur.random is not None: cur_new.random = nodes[cur.random]
            cur = cur.next 
            cur_new = cur_new.next
        

        return dummy.next
    
            
