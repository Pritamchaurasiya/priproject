## 2024-05-23 - Python Loop Optimization
**Learning:** In tight Python loops, using `iter(arr)` to avoid indexing overhead and replacing `max()` calls with conditional checks (`if x > y: ...`) can yield significant performance improvements (observed ~5.4x speedup).
**Action:** When optimizing performance-critical loops in Python, consider iterator-based traversal and inline logic instead of built-in functions for simple comparisons.
