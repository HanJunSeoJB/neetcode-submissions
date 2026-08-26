# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def classify():
            l,r = head, head

            while r is not None and r.next is not None:
                l = l.next
                r = r.next.next

            return l, r
        l, r = classify()
        # print(l.val)
        sl = l.next
        l.next = None

        def rev(n, flag=None):
            prev, cur = None, n
            while cur is not flag:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev

        rl = rev(sl)
        
        fst, sec = head, rl

        while sec:
            tmp1, tmp2 = fst.next, sec.next

            fst.next = sec
            sec.next = tmp1
            fst = tmp1
            sec = tmp2
        

    