##week04-4c.py leetcode 3866
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        h=Counter(nums)
        for i in nums:
            if i%2==0 and h[i]==1:
                return i
        return -1
