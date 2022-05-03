"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        root2change = root
        root.next = None

        cur_level = []
        if root.left:
            cur_level.append(root.left)
        if root.right:
            cur_level.append(root.right)

        while len(cur_level):
            curs = []
            for i in range(len(cur_level)):
                if i + 1 != len(cur_level):
                    cur_level[i].next = cur_level[i + 1]
                else:
                    cur_level[i].next = None
                if cur_level[i].left:
                    curs.append(cur_level[i].left)
                if cur_level[i].right:
                    curs.append(cur_level[i].right)
            cur_level = curs
        return root2change
