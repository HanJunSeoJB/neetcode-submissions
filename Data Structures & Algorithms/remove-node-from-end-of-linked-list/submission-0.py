# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first, target = dummy, dummy
        
        for i in range(n):
            target = target.next

        while target.next is not None:
            first = first.next
            target = target.next

        first.next = first.next.next
        return dummy.next