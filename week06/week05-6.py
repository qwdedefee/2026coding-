##week05-6.py leetcode 2352
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c=Counter()
        for r in grid:
            c[tuple(r)]+=1
        ans=0
        for f in zip(*grid):
            ans+=c[tuple(f)]
        return ans
