# Bug Descriptions

---

## bug1.py
- **Language:** Python
- **Intended Behavior:** (1) Return the last `n` items in a list. (2) Return the average of a list of numbers.
- **Bug 1 — Off-by-one in slicing:** `lst[-n - 1:]` returns `n + 1` items instead of `n`. Should be `lst[-n:]`.
- **Bug 2 — Index out of range:** `range(len(lst) + 1)` iterates one step too far and raises `IndexError`. Should be `range(len(lst))`.

---

## bug2.py
- **Language:** Python
- **Intended Behavior:** (1) Compute factorial recursively. (2) Print numbers from `n` down to 1. (3) Return the maximum number in a list.
- **Bug 1 — Infinite recursion:** `factorial(n)` calls itself with `n` instead of `n - 1`, causing infinite recursion and a `RecursionError`.
- **Bug 2 — Infinite loop:** `count_down` never decrements `n`, so the `while` loop runs forever.
- **Bug 3 — Comparison instead of assignment:** `max_val == num` compares instead of assigning. Should be `max_val = num`.

---

## bug3.js
- **Language:** JavaScript
- **Intended Behavior:** (1) Fetch a user by ID and return their full name. (2) Sum all numbers in an array. (3) Validate a username with a regex.
- **Bug 1 — Missing await:** `response.json()` returns a Promise. Without `await`, `data` is a Promise object and accessing `.firstName` returns `undefined`.
- **Bug 2 — String instead of number:** `total` is initialised as `"0"` (string), so `+=` concatenates instead of adding. Result is `"01234"` instead of `10`.
- **Bug 3 — Missing regex anchor:** The regex `/^[a-zA-Z0-9]{3,20}/` has no `$` at the end, so it matches the valid prefix of any string. `"ok!@#$%"` passes validation when it should not. Should be `/^[a-zA-Z0-9]{3,20}$/`.

---

## bug4.js
- **Language:** JavaScript
- **Intended Behavior:** (1) Create an array of 5 functions each returning its own index. (2) Remove duplicate values from an array. (3) Deep copy an object.
- **Bug 1 — var in loop closure:** `var` is function-scoped, so all closures share the same `i`. After the loop `i` is `5`, so every function returns `5`. Fix: use `let` instead of `var`.
- **Bug 2 — Missing return true:** The `filter` callback returns `false` for duplicates but returns `undefined` (falsy) for unique items. All items are removed. Should add `return true` after `seen.push(item)`.
- **Bug 3 — Shallow copy:** `Object.assign({}, obj)` only copies top-level properties. Nested objects are still referenced, not cloned. Use `JSON.parse(JSON.stringify(obj))` or `structuredClone(obj)` for a true deep copy.

---

## bug5.java
- **Language:** Java
- **Intended Behavior:** (1) Return the first element of a list. (2) Reverse an array in place. (3) Return the sum of integers from 1 to `n`.
- **Bug 1 — NullPointerException:** `items.get(0)` can return `null` if the list contains a null element. Calling `.toUpperCase()` on `null` throws `NullPointerException`. Should add a null check before calling the method.
- **Bug 2 — Wrong loop bound:** `i <= n / 2` causes the middle element of an odd-length array to be swapped with itself, and on even-length arrays it goes one iteration too far, re-swapping elements back. Should be `i < n / 2`.
- **Bug 3 — Off-by-one in sum:** `i < n` stops before adding `n` itself. Should be `i <= n`. For `n = 5`, result is `10` instead of `15`.

---

## bug6.java
- **Language:** Java
- **Intended Behavior:** (1) Check if two strings are equal ignoring case. (2) Count the number of words in a sentence. (3) Compute the factorial of `n`.
- **Bug 1 — Reference comparison:** `==` compares object references, not string content. `"Hello".toUpperCase() == "hello".toUpperCase()` returns `false`. Should use `.equals()`.
- **Bug 2 — Multiple spaces inflate count:** `split(" ")` with a single space produces empty strings for consecutive spaces. `"hello   world"` splits into `["hello", "", "", "world"]`, returning `4` instead of `2`. Fix: use `split("\\s+")`.
- **Bug 3 — Integer overflow:** `int` holds up to ~2.1 billion. `15!` is 1,307,674,368,000 — larger than `int` max. The result silently overflows and returns a wrong value. Should use `long` or `BigInteger`.