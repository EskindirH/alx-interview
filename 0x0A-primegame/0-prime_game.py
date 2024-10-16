#!/usr/bin/python3
"""
Determines the winner of a prime picking game between Maria and Ben.
"""


def is_winner(x, nums):
    """
    Determines the winner of a prime picking game between Maria and Ben.

    Args:
        x (int): The number of rounds to be played.
        nums (list of int): List of n values representing the size of the set (1 to n) for each round.

    Returns:
        str: "Maria" if Maria wins the most rounds, "Ben" if Ben wins the most rounds, or None if there's no clear winner.

    Raises:
        ValueError: If x is not a positive integer or nums is empty.
    """
    if not nums or x <= 0:
        return None

    def sieve(n):
        """
        Helper function to generate prime numbers up to n using the Sieve of Eratosthenes.

        Args:
            n (int): The upper limit of numbers to check for primes.

        Returns:
            list: List of prime numbers up to and including n.
        """
        sieve = [True] * (n + 1)
        sieve[0], sieve[1] = False, False  # 0 and 1 are not primes
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        primes = [i for i in range(2, n + 1) if sieve[i]]
        return primes

    # Get the largest number in nums to optimize the sieve
    max_n = max(nums)

    # Get all primes up to the maximum n in any round
    primes_up_to_max_n = sieve(max_n)

    # Initialize win counters for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        # Filter primes up to the current value of n
        primes = [p for p in primes_up_to_max_n if p <= n]
        moves = len(primes)  # The number of possible moves (primes)

        # Determine the winner based on the number of moves
        if moves % 2 == 1:  # Maria wins if the number of moves is odd
            maria_wins += 1
        else:  # Ben wins if the number of moves is even
            ben_wins += 1

    # Determine and return the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
