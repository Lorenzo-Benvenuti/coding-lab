# [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

> Decide whether `t` is an anagram of `s`, meaning it contains exactly the same characters with the same counts.

### Pattern
**Frequency counting** – suggested whenever two sequences must contain <ins>the same elements with the same multiplicities</ins>, which a dictionary of counters verifies in a single pass.

### Solution Logic
A single **dictionary** works as a balance scale, mapping each character to the difference between its occurrences in `s` and in `t`.
* **Strings of different length** can never be anagrams, and the early return also guarantees that `zip()` pairs every character, which `strict=True` makes explicit.
* **Each pair of characters** from `zip()` increments the counter of the character from `s` and decrements the one from `t`, with `get(c, 0)` covering characters seen for the first time.
* **Anagrams leave every counter at zero**, and `all()` stops at the first value that is not.

### Complexity
* **Time Complexity:** $\color{green}{O(n)}$ – A single (for loop) pass over both strings, with each dictionary update costing **O(1)** on average.
* **Space Complexity:** $\color{green}{O(1)}$ – The dictionary holds at most 26 keys under the problem's constraints, and **O(k)** for an alphabet of k distinct characters.

### Follow-Up Response
The solution already handles Unicode, because a dictionary accepts any character as a key and Python strings iterate over whole code points rather than UTF-16 units.
* **No change to the code** is needed, and space simply grows to **O(k)** for k distinct characters while time stays **O(n)**.
* **Canonically equivalent strings**, such as a precomposed `é` and an `e` followed by a combining accent, should first be normalized with `unicodedata.normalize("NFC", s)`, otherwise they produce different counters.
