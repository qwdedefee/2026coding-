#week01-4.cpp leetcode 1431
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        b=max(candies)
        for candie in candies:
            if candie+extraCandies>=b: ans.append(True)
            else: ans.append(False)
        return ans
