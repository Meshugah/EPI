# Searching - We are going to be dealing with static data in this chapter
# static as in not changing very often

# Binary Search, is on a sorted array
# the idea behind sorting being, you can eliminate half the keys each search

# Bentley's Iterative Binary Search
import collections


def bsearch(t, A):
    L, U = 0, len(A) - 1
    # A = [1, 2, 3, 4]
    #      ^        ^
    #      L        U
    while L <= U:  # lets find out why the equal to works here but doesn't earlier
        # M = L + (U - L) // 2 is better
        M = (L + U) // 2  # middle equals top and bottom limit divided by 2
        if A[M] < t:  # if pivot is less than the item you are searching for, i.e, disqualify the top section
            L = M + 1  # move the lower threshold to above the middle
        elif A[M] == t:  # exactly equal to the element, return it
            return M
        else:  # else eliminate the bottom section, by moving the upper just below it
            U = M - 1  # why not plus one???
    return -1


# Boot camp
# assemble the format of the collection
Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

# return the gpa of a student, basically a getter
def compute_gpa(student):
    return student.grade_point_average, student.name

# the actual search
def search_student(students, target, comp_gpa):
    import bisect

    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))  # bisect left returns the fisrt element that is greater than or equal to the target value
    return 0 <= i < len(students) and students[i] == target

# Search a sorted array for first occurrence of k
# Binary search commonly asks for the index of any element of a sorted array
# that is equal to a specified element. The following problem has a slight
# twist on this.
# get the FIRST occurrence of it
# basically binary search, but you continue on a find with the bottom half of the array

def search_first_of_k(A, k):
    L, H, result = 0, len(A) - 1, -1
    # A[left: right + 1] is the candidate set
    while L <= H:
        M = (L + H) // 2
        if A[M] < k:
            L = M + 1
        if A[M] == k:
            result = M
            H = M - 1
        if A[M] > k:
            H = M - 1
    return result







