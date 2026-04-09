# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
        nextNode = slow.next
        slow.next, prev = None, None
        while nextNode:
            tempNode = nextNode.next
            nextNode.next = prev
            prev = nextNode
            nextNode = tempNode
        firstHalf, secondHalf = head, prev

        while secondHalf:
            tempFirst, tempSecond = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = tempFirst
            firstHalf = tempFirst
            secondHalf = tempSecond
        return
