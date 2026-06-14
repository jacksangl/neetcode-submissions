# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        dummy = ListNode()
        cur = dummy
        heap = []
        for i, llist in enumerate(lists):
            heapq.heappush(heap, (llist.val, i, llist))
        
        while heap:
            _, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        
        return dummy.next