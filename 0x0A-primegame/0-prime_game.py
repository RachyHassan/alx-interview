#!/usr/bin/python3
"""
    Primegame
"""


# def isWinner(x, nums):
#     """ isWinner function
#         x- rounds
#         nums - numbers list
#     """
#     def sieve(n):
#         """ Helper function to generate list of prime numbers up to
#         n using Sieve of Eratosthenes """
#         is_prime = [True] * (n + 1)
#         p = 2
#         while (p * p <= n):
#             if is_prime[p]:
#                 for i in range(p * p, n + 1, p):
#                     is_prime[i] = False
#             p += 1
#         primes = [p for p in range(2, n + 1) if is_prime[p]]
#         return primes

#     """Find the maximum value
#     in nums to limit the sieve """
#     max_n = max(nums) if nums else 0
#     primes = sieve(max_n)

#     def count_moves(n):
#         """ Helper function to simulate
#         the game for a
#         given n and
#         return the winner
#         (True if Maria wins, False if
#         Ben wins) """

#         moves = 0
#         numbers = [True] * (n + 1)
#         """Initialize numbers from 1 to n as
#         True (available to pick) """
#         for prime in primes:
#             if prime > n:
#                 break
#             if numbers[prime]:
#                 moves += 1
#                 for multiple in range(prime, n + 1, prime):
#                     numbers[multiple] = False

#         return moves % 2 == 1
#         """Maria wins if the total moves are
#         odd, Ben wins if even"""

#     maria_wins = 0
#     ben_wins = 0

#     for n in nums:
#         if n == 1:
#             ben_wins += 1
#         elif count_moves(n):
#             maria_wins += 1
#         else:
#             ben_wins += 1

#     if maria_wins > ben_wins:
#         return "Maria"
#     elif ben_wins > maria_wins:
#         return "Ben"
#     else:
#         return None
def isWinner(x, nums):
    """isWinner function
         x- rounds
         nums - numbers list
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
