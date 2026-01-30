## 2024-05-22 - Python Loop Optimizations
**Learning:** In tight Python loops, function calls like `max()` and list indexing can be significant bottlenecks. Replacing `range(len(arr))` + indexing with `iter(arr)` and replacing `max()` calls with explicit conditional checks yielded a ~4.6x speedup.
**Action:** When optimizing performance-critical loops in Python, favor iterators over indexing and explicit logic over repeated function calls.
