# if number of 1 bits are odd, parity is 1
# O(N) time
# O(1) space
def parity(x):
    num_of_1bits = 0
    while x:
        num_of_1bits += x & 1
        x >>= 1
    return num_of_1bits % 2


# remove last bit
def remove_last_bit(x):
    return x & (x - 1)


# O(k) time
def parity_with_trick(x):
    result = 0
    while x:
        result ^= x & 1
        x &= x - 1  # remove the last bit trick
    return result


# two tips for improving bitwise performance are:
# 1) processing multiple bits at the same time
# 2) caching results

# get just the last bit
def get_last_bit(x):
    return x & ~(x - 1)

def parity_by_xor(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


# Variant
# 1
# Right propagate the rightmost set bit
def right_propagate(x):
    return x | (x-1)

def compute_x_mod_a_power_of_two(x, power):
    return x % power**2

def true_if_power_of_two(x):
    return True if x % 2 == 0 else False



