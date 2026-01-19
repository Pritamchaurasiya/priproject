## 2026-01-19 - Python Loop Optimization: Iterators & Conditionals vs Built-ins
**Learning:** Replacing `range(len(arr))` + indexing with `iter(arr)` and replacing `max()` calls with explicit conditional checks can yield significant performance gains (observed ~5.2x speedup in this codebase).
**Action:** In tight loops in Python, prefer iterators and explicit logic over repeated indexing and function calls like `max()` or `min()`.
