# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = ListNode()
        dummy.next = cur
        carry = 0
        
        while l1 or l2:
            val = carry
            if l1: val += l1.val
            if l2: val += l2.val
            carry = 0
            if val > 9: 
                carry = 1
                val %= 10
            cur.val = val
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2: 
                cur.next = ListNode()
                cur = cur.next
        if carry == 1:
            cur.next = ListNode(1)
        return dummy.next