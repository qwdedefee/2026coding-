##week15-4.py leetcode 72
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1,N2=len(word1),len(word2)
        @cache
        def helper(i,j):
            if i==N1 and j==N2: return 0
            if i==N1: return N2-j
            if j==N2: return N1-i
            ans=min(helper(i+1,j)+1,helper(i,j+1)+1)
            if word1[i]==word2[j]:
                return min(ans,helper(i+1,j+1))
            return min(ans,helper(i+1,j+1)+1)
        return helper(0,0)
