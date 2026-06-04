##week15-3.py leetcode 714
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def h(i,has):
            if i==len(prices): return 0
            if(has): ans=prices[i]+h(i+1,False)-fee
            else: ans=-prices[i]+h(i+1,True)
            return max(ans,h(i+1,has))
        return h(0,False)
