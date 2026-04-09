# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast != None:
            fast = fast.next
            if fast == head:
                return True
            if fast:
                fast = fast.next
            else:
                return False
            head = head.next
            

        return False


        