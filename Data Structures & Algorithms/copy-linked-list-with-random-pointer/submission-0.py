"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nw = {None:None}
        cur = head

        while cur:
            nw[cur] = Node(cur.val)
            cur = cur.next
        
        fst = head

        while fst:
            copied = nw[fst]
            copied.next = nw[fst.next]
            copied.random = nw[fst.random]
            fst = fst.next

        return nw[head]