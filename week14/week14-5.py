##week14-5.py leetcode 790
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n<=2:
            return n
        dp=[0]*(n+1)
        gap=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        dp[2]=2
        gap[2]=1
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+dp[i-2]+2*gap[i-1])%MOD
            gap[i]=(gap[i-1]+dp[i-2])%MOD
        return dp[n]
