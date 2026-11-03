# [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

> Decide whether `t` is an anagram of `s`, meaning it contains exactly the same characters with the same counts.

### Pattern
**Frequency counting** – suggested whenever two sequences must contain <ins>the same elements with the same multiplicities</ins>, here over a fixed alphabet of 26 lowercase letters that an array can index directly.

### Solution Logic
A single **integer array** of 26 counters works as a balance scale, replacing the two frequency maps of the naive approach.
* **Strings of different length** can never be anagrams, and the early return also makes it safe to walk both strings with one shared index.
* **Each letter becomes an array index** through `c - 'a'`, so the same loop increments the counter for `s` and decrements it for `t`.
* **Anagrams leave every counter at zero**, and the final scan returns `false` at the first value that is not.

### Complexity
* **Time Complexity:** $\color{green}{O(n)}$ – A single (for loop) pass over both strings, plus a final scan of exactly 26 counters that adds only **O(1)**.
* **Space Complexity:** $\color{green}{O(1)}$ – The array always holds 26 integers, regardless of the input size.

### Follow-Up Response
With Unicode input, `c - 'a'` falls outside the range 0–25 and the fixed array throws an `ArrayIndexOutOfBoundsException`.
* **A `HashMap<Integer, Integer>`** filled from `s.codePoints()` and `t.codePoints()` handles any character, whereas counting Java `char`s, which are single UTF-16 units, would split most emojis into two surrogates.
* **Time stays O(n)**, while space grows to **O(k)** for k distinct characters, at the price of hashing and boxing overhead.
* **Canonically equivalent strings**, such as a precomposed `é` and an `e` followed by a combining accent, should first be normalized with `Normalizer.normalize(s, Normalizer.Form.NFC)`.
