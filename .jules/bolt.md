## 2024-05-22 - Python Loop Optimization
**Learning:** Using `iter(arr)` to avoid indexing overhead, combined with replacing `max()` calls with conditional checks, significantly improves performance in tight Python loops (approx. 4.8x speedup).
**Action:** Prefer iterators and explicit conditionals over indices and function calls in hot paths.
