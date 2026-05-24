# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        heap = []

        stk = [root]

        while stk:
            node = stk.pop()
            heapq.heappush(heap, node.val)

            if node.left: stk.append(node.left)
            if node.right: stk.append(node.right)

        for _ in range(k-1):
            heapq.heappop(heap)
        return heap[0]