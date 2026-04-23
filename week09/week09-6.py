##week09-6.py leetcode 328
## Definition for singly-linked list.
## class ListNode:
##     def __init__(self, val=0, next=None):
##         self.val = val
##         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        now=ans=ListNode()
        for i in range(0,len(a),2):
            now.next=ListNode(a[i])
            now=now.next
        for i in range(1,len(a),2):
            now.next=ListNode(a[i])
            now=now.next
        return ans.next
