## 2026-01-23 - Python Loop Micro-Optimizations
**Learning:** In tight Python loops, function call overhead (like `max()`) and indexing (like `arr[i]`) can be significant bottlenecks. Replacing `range(len(arr))` + indexing with `iter(arr)` and replacing `max()` with explicit conditional checks yielded a ~6x speedup (0.76s vs 4.7s) for a simple Kadane's algorithm implementation.
**Action:** When optimizing hot loops in Python, prefer iterators and inline comparisons over function calls and repeated indexing.
