import collections


# find anagrams
def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        # for every string in dictionary
        # add separator.join(string's character sorted in place) to a
        # defaultdict, string is added as a linked list to that sorted character string
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [group for group in sorted_string_to_anagrams.values() if len(group) >= 2]

    # hash of an immutable set, makes sense to make it immutable to
    # so that it can only be removed and reentered( ideal for hash map )
    # hash(frozenset)


# is an anonymous letter constructable?
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    char_frequency_of_letter = collections.Counter(letter_text)

    for char in magazine_text:
        char_frequency_of_letter[char] -= 1
        if char_frequency_of_letter[char] == 0:
            del char_frequency_of_letter[char]
            if not char_frequency_of_letter:
                return True

    return False


