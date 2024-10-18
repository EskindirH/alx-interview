#!/usr/bin/python3
"""
Prime Picking Game Module.

This module defines a game between Maria and Ben. The game involves 
choosing prime numbers from a set and removing the primes and their 
multiples. The player who cannot make a valid move loses the round. 
The module includes functionality to determine the winner of multiple 
rounds of this game.

Functions:
    is_winner(x, nums): Determines the winner of x rounds based on 
    optimal play.
"""
__author__ = "Your Name"


def sieve(n):
    """
    Generates prime numbers up to a given number n using the Sieve of Eratosthenes algorithm.

    Args:
        n (int): The upper limit for prime number generation.

    Returns:
        list: A list of prime numbers up to and including n.
    """
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def isWinner(x, nums):
    """
    Determines the winner of the prime picking game between Maria and Ben for x rounds.

    Maria always plays first. The players take turns choosing a prime number from the 
    set {1, ..., n}, and then remove that prime and all of its multiples. The player 
    who cannot make a valid move loses.

    Args:
        x (int): The number of rounds to be played.
        nums (list of int): A list of n values, where each n represents the upper limit 
                            of the set for a given round.

    Returns:
        str: The name of the player who won the most rounds ("Maria" or "Ben").
        If both win an equal number of rounds, return None.

    Raises:
        ValueError: If x is not a positive integer or nums is empty.
    """
    if not nums or x <= 0:
        return None

    # Find the largest value in nums to optimize the sieve for all rounds
    max_n = max(nums)

    # Generate all prime numbers up to the maximum n using the sieve function
    primes_up_to_max_n = sieve(max_n)

    # Initialize counters for each player's wins
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        # Get the primes up to the current value of n
        primes = [p for p in primes_up_to_max_n if p <= n]
        moves = len(primes)  # The number of moves corresponds to the number of primes

        # If the number of moves is odd, Maria wins; if even, Ben wins
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine and return the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
