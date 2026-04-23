# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        # naive sltn

        # find length

        length = 0
        check = head
        while check:
            check = check.next
            length += 1
        # nnode is +1 , cur is the delete node and prev will 
        # point to nnode
        if length == n:
            return head.next
        nnode = head.next
        cur = head
        prev = None
    
        for i in range(length, n, -1):
            prev = cur
            cur = cur.next
            nnode = nnode.next
        # 1, 2 ,3 4
        # prev = None
        prev.next = nnode
        return head


