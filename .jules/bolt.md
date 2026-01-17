## 2024-05-22 - [Python Loop Optimization]
**Learning:** In tight Python loops, replacing `range(len(arr))` + indexing with `iter(arr)` and replacing `max()` calls with explicit conditional checks can yield significant performance gains (observed ~5x speedup).
**Action:** When optimizing performance-critical loops in Python, prefer iterators and explicit `if/else` logic over built-in functions like `max/min` to avoid function call overhead.
