## 2024-05-22 - [Python Tight Loop Optimization]
**Learning:** In tight Python loops (like Kadane's algorithm), function call overhead (e.g., `max()`) and indexing (`arr[i]`) are significant bottlenecks.
**Action:** Replace `max(a, b)` with conditional logic and use `iter(arr)` to iterate elements. This yielded a ~4.5x speedup in this case.
