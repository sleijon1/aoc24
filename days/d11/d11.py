from functools import lru_cache
arrangement = open("input.txt").read().strip().split(" ")

@lru_cache(maxsize=1000)
def transform_stone(stone, blinks):
    if not blinks:
        return 0
    stones = 0
    if stone == "0":
        return transform_stone("1", blinks-1)
    elif len(stone) % 2 == 0:
        for new_stone in (stone[:len(stone)//2], str(int(stone[len(stone)//2:]))):
            stones += transform_stone(new_stone, blinks-1)
        return stones + 1
    else:
        return transform_stone(str(int(stone) * 2024), blinks-1)

print(f"part 1: {sum([transform_stone(stone, 25) + 1 for stone in arrangement])}, part 2: {sum([transform_stone(stone, 75) + 1 for stone in arrangement])}")
