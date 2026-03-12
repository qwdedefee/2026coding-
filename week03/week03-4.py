##week03-4.py leetcode 1004
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero=0
        t=0
        ans=0
        for h in range(len(nums)):
            if nums[h]==0:
                zero+=1
                while zero>k:
                    if nums[t]==0:
                        zero-=1
                    t+=1
            ans=max(ans,h-t+1)
        return ans
