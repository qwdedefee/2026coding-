##week12-3.py leetcode547
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visit=set()
        def helper(now):
            visit.add(now)
            for k in range(n):
                if k not in visit and isConnected[now][k]:
                    helper(k)
        ans=0
        for i in range(n):
            if i not in visit:
                ans+=1
                helper(i)
        return ans
