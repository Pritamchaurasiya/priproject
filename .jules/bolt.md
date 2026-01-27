## 2026-01-27 - Python Tight Loop Optimization
**Learning:** In tight Python loops, function call overhead (like `max()`) and repeated list indexing are significant bottlenecks. Replacing `max()` with explicit `if/else` and using `iter()` instead of `range(len())` yielded a ~4.7x speedup for Kadane's algorithm.
**Action:** Check tight loops for built-in function calls and indexing patterns that can be replaced with iterators and native operators.
