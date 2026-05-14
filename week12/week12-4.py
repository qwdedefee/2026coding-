##week12-4.py leetcode 1466
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visit=set()
        path=defaultdict(list)
        for a,b in connections:
            path[a].append((b,+1))
            path[b].append((a,-1))
        def helper(now):
            ans=0
            visit.add(now)
            for k,d in path[now]:
                if k not in visit:
                    if d==+1: ans+=1
                    ans+=helper(k)
            return ans
        return helper(0)
