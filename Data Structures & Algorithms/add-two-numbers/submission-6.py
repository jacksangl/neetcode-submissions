# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # naive

        l1_list = []
        l2_list = []
        cur = l1
        while cur: 
            l1_list.append(cur.val)
            cur = cur.next
        cur = l2
        while cur: 
            l2_list.append(cur.val)
            cur = cur.next
        cur = ListNode()
        dummy = ListNode(0, cur)
        length1, length2 = len(l1_list), len(l2_list)
        carry = 0
        for i in range(max(length1, length2)):
            val = carry
            if i < length1: val += l1_list[i]
            if i < length2: val += l2_list[i]
            if val > 9:
                carry = 1
                val %= 10 
            else:
                carry = 0
            cur.next = ListNode(val, None)
            cur = cur.next
        if carry:
            cur.next = ListNode(1, None)

        return dummy.next.next
            
        
