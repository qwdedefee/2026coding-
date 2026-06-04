##week15-1a.py leetcode 62
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def h(i,j):
            if i==m-1 and j==n-1: return 1
            if i==m or j==n: return 0
            return h(i+1,j)+h(i,j+1)
        return h(0,0)
