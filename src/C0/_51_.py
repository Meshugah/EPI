# first stage moves elements smaller than the pivot to the smaller side, by exchange
RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    for i in range(len(A)):
        # look for the smaller element
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # Second pass: group elements larger than pivot
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        for j in reversed(range(i)):
            if pivot < A[j]:
                A[i], A[j] = A[j], A[i]
                break


# element un unclassified is < pivot is exchanged with the first occurrence of the pivot
# element equal to the pivot is left alone
# element un unclassified that is > pivot is exchanged with the last unclassified element

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # divide into three subarrays
    # bottom section: A[:smaller]
    # middle section: A[smaller:equals]
    # unclassified section: A[equals: larger]
    # top section: A[larger:]
    smaller, equals, larger = 0, 0, len(A)
    # A = [1, 2, 2, 4]
    #         ^  ^  ^
    #         s     e
    #               la
    while equals < larger:
        if A[equals] < pivot:
            A[equals], A[smaller] = A[smaller], A[equals]
            equals, smaller = equals + 1, smaller + 1
        elif A[equals] == pivot:
            equals += 1
        else:
            larger -= 1
            A[equals], A[larger] = A[larger], A[equals]


def dutch_flag_four_parts(key1, key2, key3, A):
    # three sections
    # section 1 key1 [ = key1]
    # section 2 key2 [ = key2]
    # section 3 unknown [ unknown ]
    # section 4 key3 [ = key 3]
    smaller, mid, equals, larger = 0, 0, 0, len(A)
    while equals < larger:
        if A[equals] == key1:
            A[equals], A[smaller] = A[smaller], A[equals]
            equals, smaller, mid = equals + 1, smaller + 1, mid + 1
        elif A[equals] == key2:
            A[equals], A[mid] = A[mid], A[equals]
            equals, mid = equals + 1, mid + 1
        else:
            larger -= 1
            A[equals], A[larger] = A[larger], A[equals]

