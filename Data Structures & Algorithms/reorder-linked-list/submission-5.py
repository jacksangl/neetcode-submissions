# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find middle and reverse
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow is now our middle
        prev = None
        nnode = slow
        while slow:
            nnode = nnode.next
            slow.next = prev
            prev = slow
            slow = nnode
        first, second = head, prev
        while first and second:
            nnode = first.next
            first.next = second
            first = nnode
            nnode = second.next
            if second != first:
                second.next = first
            second = nnode
        


        
