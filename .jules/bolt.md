## 2024-10-18 - Python Tight Loop Optimization
**Learning:** In tight Python loops, replacing `range(len(arr))` + indexing with `iter(arr)` and replacing `max()` calls with explicit conditional checks can yield significant performance gains (~4.9x speedup).
**Action:** Prefer iterators and explicit checks over function calls in performance-critical hot loops.
