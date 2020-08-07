# Recursion boot camp
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


# if you are asked to remove recursion from a program, consider using
# stack to mimic the call stack.

# tail recursion can be optimized with a while loop
# towers of hanoi

NUM_PEGS = 3

# Relevant link: https://www.reddit.com/r/learnprogramming/comments/ajwi3j/why_is_recursion_so_hard/
def compute_tower_hanoi(num_rings):
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move == 0:
            return
        else:
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            # Step to move last disk to
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg,
                                      to_peg, from_peg)

    # Initialize pegs
    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result


# base case: if a problem is simple enough solve it directly
# otherwise assume calling the function magically return the correct answer
# for all input sizes smaller than the correct input n.
# Given that assumption, try to solve for the problem for the (induction step)
#