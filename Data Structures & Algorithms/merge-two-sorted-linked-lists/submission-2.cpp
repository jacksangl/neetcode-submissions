/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1 && !list2) return nullptr;
        if (!list1) return list2;
        if (!list2) return list1;

        ListNode start;
        ListNode* node = &start;

        while (list1 && list2) {
       
            int list1_val = list1->val;
            int list2_val = list2->val;

            if (list1_val < list2_val) {
                node->next = list1;
                list1 = list1->next;
            }

            else {
                node->next = list2;
                list2 = list2->next;
            }

            node = node->next;
        }

        node->next = list1 ? list1 : list2;
        return start.next;
    }
};
