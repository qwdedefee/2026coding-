##week13-1.py leetcode 1926
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue=deque()
        queue.append((entrance[0],entrance[1],0))
        visit=set()
        visit.add(tuple(entrance))
        m,n=len(maze),len(maze[0])
        while queue:
            i,j,step=queue.popleft()
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if ii<0 or jj<0 or ii>=m or jj>=n: continue
                if maze[ii][jj]=='+': continue
                if (ii,jj) not in visit:
                    if ii==0 or jj==0 or ii==m-1 or jj==n-1: return step+1
                    visit.add((ii,jj))
                    queue.append((ii,jj,step+1))
        return -1
