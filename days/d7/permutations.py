# exploring ways of permutation - essentially a cartesian product
# and how to implement it in python without using itertools.product


def product(*args, repeat=1):
    # Prepare the pools: replicate input iterables based on the `repeat` value
    pools = [tuple(pool) for pool in args] * repeat
    print(f"pools: {pools}")
    result = [[]]  # Start with an empty list as the initial product

    # Iteratively build combinations
    for pool in pools:
        new_result = []
        # this doubles the amount of results for each iteration of "repeat"
        # and makes sure we try each ordering of the symbols
        for prefix in result:
            for item in pool: # adds new item for each existing prefix 
                new_result.append(prefix + [item])  # Append item to each prefix
        result = new_result
        print(f"result: {result}")

    # Convert list of lists into tuples
    for combination in result:
        # yield each combination as a tuple
        # important since this function can be used
        # for large combinations and we don't want to store them all in memory
        yield tuple(combination)

# Example usage
symbols = ["*", "+"]
times = 3
combinations = product(symbols, repeat=times)

# Print results
for combo in combinations:
    print("".join(combo))  # Joining tuples for clean output

# Much simpler implementation for 3 symbols
# ofc this does not generalize to bigger combinations
# and you have to manually add for loop for each character
# added to the combination string
for sym in symbols:
    for sym2 in symbols:
        for sym3 in symbols:
            print(sym + sym2 + sym3)


