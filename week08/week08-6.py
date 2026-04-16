##week08-6.py leetcode 875
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            total = 0
            for pile in piles:
                total += ceil(pile/k)
            return total <= h
        return bisect_left(range(1,max (piles)), True, key=helper) +1
