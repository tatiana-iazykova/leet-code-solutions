from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return
        vals = [head.val]
        cur_val = head
        while cur_val:
            if cur_val.val != vals[-1]:
                vals.append(cur_val.val)
            cur_val = cur_val.next

        return self.add_new_node(vals)

    @staticmethod
    def add_new_node(node_list):

        tail = ListNode(node_list[-1])

        if len(node_list) > 1:
            for node in node_list[::-1][1:]:
                new_node = ListNode(node, tail)
                tail = new_node
        return tail
