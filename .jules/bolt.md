## 2024-05-23 - Python Loop Performance
**Learning:** In tight Python loops, `max()` function calls and list indexing add significant overhead. Using `iter(arr)` and replacing `max(a, b)` with conditional logic `if a > b else b` can result in massive speedups (observed ~5x).
**Action:** When optimizing hot loops in Python, prefer iterators over range/index and explicit conditionals over small utility function calls.
