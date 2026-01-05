## 2024-05-23 - Python Loop Performance
**Learning:** In tight Python loops, function calls (like `max()`) and list indexing have significant overhead. Replacing `max(a, b)` with conditional checks and using `iter(arr)` instead of indexing can yield ~4-5x performance improvements.
**Action:** When optimizing hot paths in Python, prefer iterators and inline logic over repeated function calls or indexing.
