##week04-4b.py leetcode 3866
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        n=len(nums)
        ans=-1
        h=[0]*101
        for i in nums:
            h[i]+=1
        for i in nums:
            if i%2==0 and h[i]==1:
                return i

        return -1
