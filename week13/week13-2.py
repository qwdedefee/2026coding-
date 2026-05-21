##week13-2.py leetcode 994
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visit=set()
        queue=deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                    visit.add((i,j))
                if grid[i][j]==1: fresh+=1
        ans=0
        while queue:
            i,j,t=queue.popleft()
            ans=t
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if ii<0 or jj<0 or ii>=m or jj>=n: continue
                if (ii,jj) in visit: continue
                if grid[ii][jj]==1:
                    fresh-=1
                    visit.add((ii,jj))
                    queue.append((ii,jj,t+1))
        if fresh>0: return -1
        return ans
