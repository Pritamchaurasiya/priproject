## 2024-05-23 - Python Loop Optimization
**Learning:** In tight Python loops, replacing `range(len(arr))` + indexing with `iter(arr)` and replacing `max()` calls with explicit conditional checks can yield significant performance gains (observed ~4.7x speedup).
**Action:** Look for `max()`/`min()` calls inside heavy loops and consider unrolling them into `if/else` blocks, and use iterators over index-based access where possible.
