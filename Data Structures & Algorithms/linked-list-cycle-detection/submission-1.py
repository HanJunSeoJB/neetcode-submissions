# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first, fast = head, head
        while fast is not None and fast.next is not None:
            first = first.next
            fast = fast.next.next

            if first == fast:
                return True

        return False
