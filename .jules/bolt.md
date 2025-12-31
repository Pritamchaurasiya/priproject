## 2024-05-22 - [Python Loop Optimization]
**Learning:** Using `iter(arr)` to avoid indexing overhead, combined with replacing `max()` calls with conditional checks, significantly improves performance in tight Python loops (observed ~4.5x speedup).
**Action:** When optimizing tight loops in Python, consider iterator consumption and manual conditional checks over built-in function calls like `max` or `min`.
