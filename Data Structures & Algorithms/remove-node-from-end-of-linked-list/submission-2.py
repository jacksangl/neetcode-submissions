# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length, counter = 1, 0
        lastNode = head.next
        while lastNode:
            length += 1
            lastNode = lastNode.next
        
        if length == 1:
            head = head.next
            return head
        elif length == n:
            tmp = head.next
            lastNode 
            return tmp
            
        copy = head
        while counter != length - n - 1:
            copy = copy.next
            counter += 1
        copy.next = copy.next.next
        return head
            
