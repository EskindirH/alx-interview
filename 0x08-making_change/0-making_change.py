#!/usr/bin/python3

def make_change(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with a large number (infinity equivalent)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make total of 0

    # Loop through each coin and update dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be reached
    return dp[total] if dp[total] != float('inf') else -1
