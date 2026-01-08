## 2026-01-08 - Python Loop Optimization
**Learning:** In tight Python loops, avoiding indexing (using `iter`) and replacing built-in `max()`/`min()` with conditional checks can yield massive speedups (~4-5x).
**Action:** When optimizing hot paths in Python, prefer iterators over `range(len())` and simple `if` statements over function calls for simple comparisons.
