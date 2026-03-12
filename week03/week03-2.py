##week03-2.py leetcode 643
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c=sum(nums[:k])
        ans=c
        a=len(nums)
        for i in range(k, a):
            c=c+nums[i]-nums[i-k]
            ans=max(ans,c)

        return ans/k
