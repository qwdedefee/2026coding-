#week01-2.py leetcode 1768
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        n1,n2=len(word1),len(word2)
        i,j=0,0
        while i<n1 or j<n2:
            if i<n1: ans+=word1[i]
            if j<n2: ans+=word2[j]
            i+=1
            j+=1
        return ans
