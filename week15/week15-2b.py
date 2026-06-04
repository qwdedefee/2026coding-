##week15-2b.py leetcode 1143
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        t=[[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]: t[i+1][j+1]=t[i][j]+1
                t[i+1][j+1]=max(t[i+1][j+1],t[i][j+1],t[i+1][j])
        return t[m][n]
