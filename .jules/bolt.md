## 2025-02-20 - [Python Loop Optimization]
**Learning:** In tight Python loops, replacing `range(len(arr))` + indexing with `iter(arr)` and replacing `max()` calls with explicit conditional checks can yield significant performance gains (observed ~4.6x speedup).
**Action:** When optimizing hot paths in Python, prefer iterator-based loops and explicit comparisons over repeated function calls like `max()` or `min()`.
