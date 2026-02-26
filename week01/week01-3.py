#week01-3.py leetcode 1071
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1,n2=len(str1),len(str2)
        n=gcd(n1,n2)
        ans=str1[:n]
        if ans*(n1//n)!=str1: return ""
        if ans*(n2//n)!=str2: return ""
        return ans
