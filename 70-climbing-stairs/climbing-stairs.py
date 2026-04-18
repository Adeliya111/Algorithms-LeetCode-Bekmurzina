class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev2, prev1 = 1, 2  # dp[1] = 1, dp[2] = 2
        
        for i in range(3, n + 1):
            curr = prev1 + prev2  # dp[i] = dp[i-1] + dp[i-2]
            prev2, prev1 = prev1, curr
        
        return prev1