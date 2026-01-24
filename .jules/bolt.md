## 2026-01-24 - Python Loop Optimization
**Learning:** In tight Python loops, replacing `range(len(arr))` + indexing with `iter(arr)` and replacing `max()` calls with explicit conditional checks can yield significant performance gains (observed ~4.5x speedup in this codebase).
**Action:** When optimizing CPU-bound Python loops, prefer iterators over indexing and inline simple comparisons instead of using built-in functions like `max()` or `min()`.
