# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        prev = None

        def find_length(node):
            count = 0
            while node:
                node = node.next
                count += 1
            return count
        
        length = find_length(head)
        node = head
        next_node = node.next

        while node and length > n:
            length -= 1
            prev = node
            node = node.next
            if node:
                next_node = node.next
       
        if prev:
            prev.next = next_node
        else:
            head = next_node
        return head