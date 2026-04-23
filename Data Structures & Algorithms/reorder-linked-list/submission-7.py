# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None: return
        # find middle and reverse
        fast = slow = head
        prevslow = None
        while fast and fast.next:
            fast = fast.next.next
            prevslow = slow
            slow = slow.next
        # slow is now our middle
        prevslow.next = None
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
            if not first and second.next != None: break
            nnode = second.next
            second.next = first
            second = nnode
        


        
