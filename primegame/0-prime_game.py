#!/usr/bin/python3
"""Module that determines the winner of the prime game."""


def isWinner(x, nums):
    """Return the name of the player that won the most rounds.

    Maria and Ben take turns picking a prime number from the set 1..n and
    removing it with all of its multiples. Maria goes first and the player
    that cannot make a move loses.

    Every move removes exactly one prime, so the winner of a round only
    depends on the parity of the number of primes up to n: if it is odd
    Maria wins, otherwise Ben wins.

    Args:
        x: the number of rounds.
        nums: list with the value of n for each round.

    Returns:
        "Maria" or "Ben", or None if the winner cannot be determined.
    """
    if x is None or x < 1 or not nums:
        return None

    rounds = nums[:x]
    biggest = max(rounds)

    sieve = [True] * (biggest + 1)
    for i in range(2, biggest + 1):
        if sieve[i]:
            for j in range(i * i, biggest + 1, i):
                sieve[j] = False

    primes_up_to = [0] * (biggest + 1)
    count = 0
    for i in range(biggest + 1):
        if i >= 2 and sieve[i]:
            count += 1
        primes_up_to[i] = count

    maria = 0
    ben = 0
    for n in rounds:
        if primes_up_to[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
