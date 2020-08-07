# a heap is a specialized binary tree, where the key is at least as great as
# the keys of it's children

# a priority queue with a priority, i.e, where an element de-queued is
# of a priority, either min or max.

# Heaps boot camp
# I Want to find K strings with longest length
# apparently: FOR MAX STRINGS WE WANT TO USE A MIN HEAP
# because: it has good insert, find-min and remove-min

import heapq
import itertools


def top_k(k, stream):  # (2, "abcdegfh")
    # Entries are compared by their lengths
    min_heap = [(len(s), s) for s in
                itertools.islice(stream, k)]  # this mother fucker is just used to set the format of the heap
    # okay, trying to break up the above part
    # len(of a string, and the string) for string in a by-character
    # splitter minus k elements, so a stream would just be a bunch of
    # letters togetther "abcd" . itertools.islice("abcdef, 2)
    # will give you: c d e f
    # so the above list would be the rest of the elements besides
    # what could be put into a heap. yet, here we are running heapify.
    # let's see where that goes.
    print(min_heap)
    heapq.heapify(min_heap)
    print(min_heap)
    # so uptil here we've heapified, all of the stream minus the first k
    # terms.
    for next_string in stream:
        print(next_string)
        # okay so this is doing some bs, why is it starting from the front
        # of the stream again. I'm not really sure.
        # let's go back and try and find out what heapq is doing
        # so with the abcdefgh, it's going through this next part with
        # by a single character at a time.

        # push next_string and pop the shortest, more efficient way of
        # pushing an element, and popping the min
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]


# merge sorted files
# This problem is motivated by the following scenario. Stock picking again lol
def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    # iter creates iterators
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # puts first element from each iterator in min_heap
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)  # returns the first element of that iterator or none
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))  # push the first element along with the array it belongs to

    # understand what is below this
    result = []  # empty result array
    while min_heap:  # while the min heap has elements in it, which it will continue to have for as long as any of
        # the sorted array have elements
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)  # pop off first element and the attribute that
        # describes which array it is from
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]  # smallest_array_iter is set to one of the sorted_arrays, using the index pointer of the smallest array that was just popped off, the smallest array whose element has just been assigned, is picked
        result.append(smallest_entry)  # my problem with this is, is that it should push only the smallest item, but the heap is not taking care of that or is it, apparently just popping off of min heap is giving you the smallest item
        next_element = next(smallest_array_iter, None)  # so grab the next element from any of the sorted arrays
        if next_element is not None:  # if it's not empty
            heapq.heappush(min_heap, (next_element, smallest_array_i))  # push it to the heap.
    return result

# initialize heap
# pop off heap
# add it to results
# push new element to heap


