##week07-6.py leetcode 649
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue=deque(list(senate))
        R,D=senate.count('R'),senate.count('D')
        banR=banD=0
        while R > 0 and D > 0:
            now=queue.popleft()
            if now=='R':
                if banR>0:
                    R-=1
                    banR-=1
                else:
                    banD+=1
                    queue.append(now)
            else:
                if banD>0:
                    banD-=1
                    D-=1
                else:
                    banR+=1
                    queue.append(now)

        if R==0: return 'Dire'
        if D==0: return 'Radiant'
