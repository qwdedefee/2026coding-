##week05-4.py leetcode 3546
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        t=sum([sum(i) for i in grid])
        p=0
        for r in grid:
            p+=sum(r)
            if p*2==t:
                return True
        p=0
        for c in zip(*grid):
            p+=sum(c)
            if p*2==t:
                return True
        return False
