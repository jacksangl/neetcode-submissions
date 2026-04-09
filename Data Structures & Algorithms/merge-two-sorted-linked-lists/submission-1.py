# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        node = ListNode()
        start = node

        while list1 or list2:
            list1_val = float('inf')
            list2_val = float('inf')

            if list1:
                list1_val = list1.val
            if list2:
                list2_val = list2.val
            if list1_val < list2_val:
                node.next = list1
                list1 = list1.next
            else: 
                node.next = list2
                list2 = list2.next
            node = node.next
        return start.next


        