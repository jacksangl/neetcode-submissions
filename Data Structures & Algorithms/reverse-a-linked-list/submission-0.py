# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None

        if head.next is None: return head

        prev = head
        nex = head.next
        cur = head.next
        i = 1
        prev.next = None

        while (nex != None):
            i += 1
            nex = nex.next
            cur.next = prev 
            prev = cur
            cur = nex

        return prev
            


