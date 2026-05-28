##week14-4.py leetcode 198
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def h(i):
            if i>=len(nums): return 0
            return nums[i]+max(h(i+2),h(i+3))
        return max(h(0),h(1))
