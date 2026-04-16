##week08-4.py leetcode 2300
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(potions)
        return [n-bisect_left(potions,success,key=lambda x:x*s) for s in spells]
