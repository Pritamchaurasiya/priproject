## 2024-05-23 - Python Loop Micro-optimizations
**Learning:** In tight Python loops, function call overhead (like `max()`) and list indexing (`arr[i]`) can be significant bottlenecks.
**Action:** Replace `max()` with inline `if/else` logic and use `iter(arr)` to avoid indexing when iterating sequentially. In this case, it yielded a ~4.5x speedup.
