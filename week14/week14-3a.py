##week14-3a.py leetcode 746
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def h(i):
            if i>=len(cost): return 0
            return cost[i]+min(h(i+1),h(i+2))
        return min(h(0),h(1))
