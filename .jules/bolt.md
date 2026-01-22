## 2024-05-23 - Python Loop Optimization
**Learning:** In tight Python loops (like Kadane's algorithm), function call overhead (e.g., `max()`) and list indexing (e.g., `arr[i]`) significantly impact performance. Replacing them with explicit conditional checks and using `iter(arr)` yielded a ~5x speedup (from 3.8s to 0.76s for 100 iterations on 100k items).
**Action:** When optimizing hot loops in Python, prefer `iter()` to traverse lists and inline simple comparisons instead of using built-in functions like `max()` or `min()`.
