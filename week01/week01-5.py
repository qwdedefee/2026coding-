#week01-5.py leetcode 238
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        psum=[1]
        osum=[1]
        for i in range(n):
            psum.append(psum[-1]*nums[i])
            osum.append(osum[-1]*nums[n-1-i])
        ans=[]
        for i in range(n):
            ans.append(psum[i]*osum[n-1-i])
        return ans
