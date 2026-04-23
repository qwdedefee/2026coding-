##week09-7.py leetcode 2130
## Definition for singly-linked list.
## class ListNode:
##     def __init__(self, val=0, next=None):
##         self.val = val
##         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans=0
        a=[]
        while head!=None:
            a.append(head.val)
            head=head.next
        for i in range(len(a)):
            ans=max(ans,a[i]+a[len(a)-1-i])
        return ans
