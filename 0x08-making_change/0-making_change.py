#!/usr/bin/python3
"""
A module to determine the fewest number of coins needed
to meet a given total using an optimized dynamic programming approach.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of integers representing coin denominations.
        total (int): The total amount to meet with the fewest coins.

    Returns:
        int: The fewest number of coins needed to meet the total, or -1
             if it is not possible.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order (this may help in some cases)
    coins.sort(reverse=True)

    # Initialize dp array with a large number (infinity equivalent)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make total of 0

    # Loop through each coin and update dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

            # Early exit: if we have found an exact match for the total
            if amount == total and dp[amount] != float('inf'):
                return dp[total]

    # If dp[total] is still infinity, it means the total cannot be reached
    return dp[total] if dp[total] != float('inf') else -1
