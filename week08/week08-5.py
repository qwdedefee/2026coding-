##week08-5.py leetcode 162
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        if nums[0]>nums [1]: return 0 #最左邊「剛好」是local max
        def helper(i):
            return nums[i-1]-nums[i]
        return bisect_left(range(len(nums)), 0, key=helper)-1
