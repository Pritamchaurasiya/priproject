## 2024-05-22 - Python Loop Optimization
**Learning:** In tight Python loops, replacing `max(a, b)` calls with simple `if` statements and using `iter(arr)` instead of `range(len(arr))` + indexing avoids significant function call and attribute lookup overhead.
**Action:** For performance-critical algorithms in Python, prefer iterators and conditional logic over built-in functions inside loops. Observed ~5.3x speedup in Kadane's Algorithm.
