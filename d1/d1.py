from collections import Counter
numbers = open('input.txt').read().splitlines()
left, right = zip(*(map(int, line.split('   ')) for line in numbers))
left = sorted(left)
right = sorted(right)
differences = [abs(x-y) for x,y in zip(left, right)]
counter = Counter(right)
print(f"part 1 {sum(differences)}, part 2 {sum([val*counter[val] for val in left])}")