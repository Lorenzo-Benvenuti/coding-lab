# [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

> Decide whether any value occurs more than once in `nums`.

### Pattern
**Hash set membership** – suggested whenever the question reduces to whether <ins>an element has already appeared</ins>, a check that a hash set answers in **O(1)** on average.

### Solution Logic
A **hash set** records every number visited so far, and each element is tested for membership before being inserted.
* **The check `n in hashset` must come first**, because `hashset.add(n)` returns `None` and silently ignores duplicates, so it cannot signal a repeat on its own.
* **The first value already in the set** returns `True` immediately, while `return False` sits after the loop and is reached only when all elements are distinct.

### Complexity
* **Time Complexity:** $\color{green}{O(n)}$ – A single (for loop) pass over the list, with each membership test and insertion costing **O(1)** on average.
* **Space Complexity:** $\color{green}{O(n)}$ – When all the `n` elements are distinct, each one ends up in the set specifically created for this purpose.

### Alternatives
* **Sorting with `nums.sort()`** and comparing adjacent elements trades time for memory, dropping the set at the price of **O(n log n)** time and a modified input list.
* **The one-liner `len(set(nums)) < len(nums)`** builds the set in C, which is fast in CPython, but it always processes the whole list, giving up the early exit.
