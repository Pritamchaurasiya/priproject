## 2024-05-23 - Python Loop Optimization
**Learning:** In tight Python loops (like Kadane's algorithm), function calls like `max()` and list indexing `arr[i]` have significant overhead.
**Action:** Replace `max()` with conditional checks and use `iter(arr)` to iterate elements directly. This yielded a ~4.6x speedup.
