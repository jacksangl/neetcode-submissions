# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        seen[head] = 1
        while head:
            head = head.next
            if head in seen:
                return True
            seen[head] = 1
        return False
            
