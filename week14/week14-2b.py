##week14-2b.py leetcode 1137
class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def h(i):
            if i==0: return 0
            if i==1 or i==2: return 1
            return h(i-1)+h(i-2)+h(i-3)
        return h(n)
