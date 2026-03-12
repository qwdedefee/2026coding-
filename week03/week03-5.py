##week03-5.py leetcode 1493
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        t,ans,zero=0,0,0
        for h in range(len(nums)):
            if nums[h]==0: zero+=1
            while zero>1:
                if nums[t]==0: zero-=1
                t+=1
            ans=max(ans,h-t+1)
        return ans-1
