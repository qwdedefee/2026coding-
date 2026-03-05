##week02-3.py leetcode 392
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1,n2=len(s),len(t)
        if n1==0: return True
        i=0
        for k in range(n2):
            if s[i]==t[k]:
                i+=1
        if i==n1: return True
        return False
