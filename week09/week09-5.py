##week09-5.py leetcode 2095
## Definition for singly-linked list.
## class ListNode:
##     def __init__(self, val=0, next=None):
##         self.val = val
##         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None: return None
        p=f=s=head
        while f!=None and f.next!=None:
            f=f.next.next
            p=s
            s=s.next
        p.next=s.next
        return head
