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
        
            nodes = {None: None}

            # these are for the second list
            # this is to iterate through the nodes
            node = head
            # assign values and hash
            while node:
                copy = Node(node.val)
                nodes[node] = copy
                node = node.next
            
            new_list = head
            # assign next and random
            while new_list:
                copy = nodes[new_list]
                copy.next = nodes[new_list.next] 
                copy.random = nodes[new_list.random]
                new_list = new_list.next

            return nodes[head]