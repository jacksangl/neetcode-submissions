# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        
        cur = head
        arr = []
        length = 0
        while cur is not None:
            arr.append(cur)
            length += 1
            cur = cur.next

        l = 0
        r = length - 1
        while l < r:
            arr[l].next = arr[r]
            l += 1
            arr[r].next = arr[l]
            r -= 1
        if length % 2 == 0: arr[r+1].next = None
        else: arr[r].next = None