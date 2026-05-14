##week12-1b.py leetcode 841
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit=set()
        def helper(now):
            for k in rooms[now]:
                if k not in visit:
                    visit.add(k)
                    helper(k)
        visit.add(0)
        helper(0)
        return len(rooms)==len(visit)
