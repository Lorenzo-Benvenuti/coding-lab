# [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

> Decide whether any value occurs more than once in `nums`.

### Pattern
**Hash set membership** – suggested whenever the question reduces to whether <ins>an element has already appeared</ins>, a check that a hash set answers in **O(1)** on average.

### Solution Logic
A **hash set** records every number visited so far, and the boolean returned by `add()` doubles as the duplicate check.
* **Since `seen.add(n)` returns `false`** when the value is already present, a single hash operation both tests and records each number, with no separate `contains()` call.
* **The first failed insertion** returns `true` immediately, while `return false` sits after the loop and is reached only when all elements are distinct.

### Complexity
* **Time Complexity:** $\color{green}{O(n)}$ – A single (for loop) pass over the array, with each `add()` costing **O(1)** on average.
* **Space Complexity:** $\color{green}{O(n)}$ – When all the `n` elements are distinct, each one ends up in the set specifically created for this purpose.

### Alternatives
* **Sorting with `Arrays.sort(nums)`** and comparing adjacent elements trades time for memory, dropping the set at the price of **O(n log n)** time and a modified input array.
* **The stream one-liner** `Arrays.stream(nums).distinct().count() < nums.length` is compact, but it always processes the whole array and adds stream overhead, giving up the early exit.
