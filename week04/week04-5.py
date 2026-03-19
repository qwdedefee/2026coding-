##week04-5.py leetcode 724
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        p=[0]*(n+1)
        for i in range(n):
            p[i+1]=p[i]+nums[i]
        for i in range(n):
            left=p[i]
            right=p[n]-p[i+1]
            if left==right:
                return i
        return -1
