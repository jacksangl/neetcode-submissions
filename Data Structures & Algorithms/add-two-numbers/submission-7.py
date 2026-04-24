# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # naive

        length1 = length2 =  0 
        cur = l1
        while cur: 
            length1 += 1
            cur = cur.next
        cur = l2
        while cur: 
            length2 += 1
            cur = cur.next

        cur = ListNode()
        dummy = ListNode(0, cur)
        carry = 0
        for i in range(max(length1, length2)):
            val = carry
            if i < length1: 
                val += l1.val
                l1 = l1.next
            if i < length2: 
                val += l2.val
                l2 = l2.next
                print(val)
            if val > 9:
                carry = 1
                val %= 10 
            else:
                carry = 0
            print(val)
            cur.next = ListNode(val, None)
            cur = cur.next
        if carry:
            cur.next = ListNode(1, None)

        return dummy.next.next
            
        
