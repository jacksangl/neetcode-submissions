# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        prev = None
        node = head
        next_node = node.next 

        while node:
            
            node.next = prev
            prev = node
            node = next_node
            if next_node:
                next_node = node.next
        
        return prev