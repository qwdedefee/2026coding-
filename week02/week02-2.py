##week02-2.py leetcode 283
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        k=0
        for i in range(n):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range(k,n):
            nums[i]=0
