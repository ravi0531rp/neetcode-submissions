class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        idx = 1
        while idx <= amount:
            for coin in coins:
                if coin <= idx:
                    dp[idx] = min(dp[idx], 1 + dp[idx - coin])
            idx += 1
        return dp[amount] if dp[amount] != float('inf') else -1