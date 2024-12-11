# Explanation

The reason this recursive memoization works so much better than an imperative solution
that actually generates the list is the following:
```python
print(transform_stone("2", 75)) # Result: 33361879939122
```
From the example on aoc we see 2 occurring multiple times only after 6 blinks: 

```python
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
```

For each of those we would add 33361879939122 stones. That is a huge number of stones to add to the list and then loop over just for one stone on 
blink 6. Obviously caching this and not adding the stones to the list is much more efficient.

But even just running:
```python
print(transform_stone("2", 75))
print(transform_stone.cache_info())
```

Shows we have 2420 cache hits just for calculating the number of stones produced by the original "2". Which drastically reduces
the number of iterations we would have to do imperatively.

To be clear, it is not that it is imperative that's the problem but rather the fact that you are generating the entire list of stones
and not caching any results. If you cached results instead of generating the list you would get a similar performance to the recursive.

What is not intuitive to me is that ***python transform_stone("2", 75)*** is so fast. It is not clear to me why the operations described repeat numbers so much.

Adding code to check unique numbers gives 54 for ***transform_stone("2", 75)*** and 3896 for the complete input. Further research

Running

```python
print("Top 5 most called functions:")
for i, (key, value) in enumerate(sorted(call_tracker.items(), key=lambda x: x[1], reverse=True)[:5]):
    print(f"{i+1}. {key} was called {value} times")
    saved = transform_stone(*key)
    print(f"iterations saved with caching for {key} -> {saved*value}")
```

Gives:
```python
Top 5 most called functions:
1. ('20', 8) was called 5214 times
iterations saved with caching for ('20', 8) -> 151206
2. ('20', 7) was called 5187 times
iterations saved with caching for ('20', 7) -> 93366
3. ('20', 9) was called 5170 times
iterations saved with caching for ('20', 9) -> 175780
4. ('20', 6) was called 5162 times
iterations saved with caching for ('20', 6) -> 46458
5. ('20', 11) was called 5138 times
iterations saved with caching for ('20', 11) -> 488110
```

Clearly we are saving a bunch of iterations and there are a total of approximatley 5 million cache entries. 

But the simplest evidence I suppose is the fact that if you add a call counter for running

```python
print(transform_stone("2", 75))
```

You get 3451 calls but 33361879939122 stones. So the unique stones are drastically fewer than the total number of stones. So if we can cache the calls:

```python
function_call(unique_stone, blink)
```

for different blinks the cost for the problem essentially becomes calculating ***unique_stone, blink***-combinations. Going down one branch of 75 blinks is obviously only 75 recursions which gave 19 unique numbers, so you're already caching a lot with 75 iterations. But when solving a problem like this you are essentially betting on unique numbers being a lot fewer than total occurrences.