##week12-1.py leetcode 841
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack=[0]
        visit=set()
        visit.add(0)
        while stack:
            now=stack.pop()
            for k in rooms[now]:
                if k in visit: continue
                stack.append(k)
                visit.add(k)
        return len(rooms)==len(visit)
