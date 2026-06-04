##week15-2a.py leetcode 1143
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        @cache
        def h(i,j):
            if i==m or j==n: return 0
            if text1[i]==text2[j]: return 1+h(i+1,j+1)
            else: return max(h(i,j+1),h(i+1,j))
        return h(0,0)
