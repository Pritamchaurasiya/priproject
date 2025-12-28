## 2024-05-23 - Python Loop Optimization
**Learning:** In tight Python loops, function call overhead (like `max()`) and indexing (like `arr[i]`) are significant. Replacing `range(len(arr))` with `iter(arr)` and `max()` with conditional checks yielded a ~4.7x speedup in Kadane's algorithm.
**Action:** When optimizing hot loops in Python, avoid function calls and indexing where possible. Prefer iterators and inline logic.
