## 2024-05-23 - Iterator in Tight Loops
**Learning:** Using `iter(arr)` and iterating over values directly instead of `range(1, len(arr))` with index access `arr[i]` significantly improves performance in Python tight loops (approx 4.8x speedup when combined with `max()` removal). Indexing has overhead.
**Action:** Prefer iterators over indexed loops for simple linear traversals in performance-critical Python code.
