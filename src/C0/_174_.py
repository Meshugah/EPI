# Greedy Algorithms

# Boot camp
def change_making(cents):
    COINS = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for coin in COINS:
        num_coins += cents // coin
        cents %= coin
    return num_coins


# 17.4 The 3-Sum Problem
# A function, quantity or property that does not change when a specific transformation is applied.

# from We can improve the time complexity :
def has_three_sum(A, t):
    A.sort()
    return any(has_two_sum(A, t - a) for a in A)


#  two pointer has two sum
def has_two_sum(A, t):
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # A[i] + A[j] > t.
            j -= 1
    return False

# Variant1: solve three sum when three elements are distinct

def has_three_sum_distinct(A, t):
    from sortedcontainers import SortedSet
    A = SortedSet(A)
    return any(has_two_sum_distinct(A, t - a) for a in A)

def has_two_sum_distinct(A, t):
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # A[i] + A[j] > t.
            j -= 1
    return False
# Variant2: solve the same problem when k, the number of elements to sum, is an additional input
# https://cs.stackexchange.com/questions/2973/generalised-3sum-k-sum-problem
# for even k: compute a sorted list S of all sums of k/2


def has_k_sum_distinct(A, t, k):
    from sortedcontainers import SortedSet
    A = SortedSet(A)

    # base case k = 3
    if k == 3:
        return any(has_two_sum_distinct(A, t - a) for a in A)
    else:
        return any(has_k_sum_distinct(A, t - a, k - 1) for a in A)



