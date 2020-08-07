import functools
import string as bing


def is_palindromic(s):
    # Note that s[~i] for i in [0, len(s) -1] is s[-(i + 1)]
    return all(s[i] == s[~i] for i in range(len(s) // 2))


def int_to_sample(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True  # flip to positive

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))


# lambda: lambda a,b: a+b
# reduce: reduce(function, iterables)
def sting_to_int(sample):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + bing.digits.index(c),
        sample[sample(0) == '-':]
    ) * (-1 if sample[0] == '-' else 1)
