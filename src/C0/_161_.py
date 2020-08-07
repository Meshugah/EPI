# F(n) = F(n - 1) + F(n - 2)
# time complexity with recursion is n^2
# time complexity with caching is n, but space is O(1)
def fibonacci(n):
    # base condition
    if n <= 1:
        return n

    # inductive step
    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):  # range drop: for n= 5, end at 4 because we start at fib 2, n= 1,2,3,4, gets f2,3,4,5.
        f = f_minus_2 + f_minus_1  # f being third number in fib, basic fib step, current = cur-1 + cur-2
        f_minus_2, f_minus_1 = f_minus_1, f  # perspective shifts by 1
    return f_minus_1  # because of the shift


# find maximum sum over all subarray of a given array of integers
def find_maximum_subarray(A):
    min_sum = max_sum = 0
    import itertools
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)  #
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum  # end goal


# choose DP whenever you need to make CHOICES when you have to arrive at a solution. Like which subproblem to solve

# Dynamic Programming boot camp
# 16.1 Count the number of score combinations

def num_combinations_for_final_score(final_score, individual_play_scores):
    num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_scores]  # creates a 2d array, each column starting with 1 of length, final score and number of columns = the individual play scores. The excessive number of columns,is because of the idea that a combination of the 2,3 results array, at position [5], is equal to the the results array of 2 at position [5] + 2,3 results array at position [5- (new element which is in this case 3)] sp by caching all possible previous results in an array(the results array), we are able to get the solution to adding a new element in O(1) by just adding two old elements. oh and the 1s at the start of the array. It's cause any element can make 0 by just not existing.
    for i in range(len(individual_play_scores)):  # outermost array is all the possible play scores
        for j in range(1, final_score + 1):  # inner array is the range of 1 to the final score.
            without_this_play = (num_combinations_for_score[i - 1][j] if i >= 1 else 0)  # the results array, without the current item
            with_this_play = (
                num_combinations_for_score[i][j - individual_play_scores[i]] if j >= individual_play_scores[i] else 0)  # the results array a few elements ago
            num_combinations_for_score[i][j] = (without_this_play + with_this_play)
    return num_combinations_for_score[-1][-1]  # returns the very last element, of this, but why. because that's the number of time the final score can be created with all the individual scores.
