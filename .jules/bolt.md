## 2024-05-23 - Python Loop Optimization
**Learning:** In tight Python loops, using `iter(arr)` to avoid indexing overhead and replacing `max()` calls with conditional checks (`if x > y`) can significantly improve performance (observed ~4.5-4.8x speedup).
**Action:** When optimizing CPU-bound loops in Python, prefer iterators and simple conditionals over built-in functions like `max()` or `min()` inside the loop.
