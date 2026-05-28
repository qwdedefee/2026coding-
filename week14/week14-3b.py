##week14-3b.py leetcode 746
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        a=[0]*(n+1)
        a[0],a[1]=cost[0],cost[1]
        for i in range(2,n+1):
            a[i]=min(a[i-1],a[i-2])
            if i<n: a[i]+=cost[i]
        return a[n]
