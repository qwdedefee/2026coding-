##week04-2.py leetcode 1732
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=h=0
        for i in range(len(gain)):
            h+=gain[i]
            ans=max(ans,h)
        return ans
