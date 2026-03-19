##week04-3.py leetcode 3866
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        n=len(nums)
        ans=-1
        h=[0]*101
        for i in range(n):
            h[nums[i]]+=1
        for i in range(n):
            if nums[i]%2==0 and h[nums[i]]==1:
                return nums[i]

        return -1
