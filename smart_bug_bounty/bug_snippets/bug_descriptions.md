# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items in a list.
- **Current Issue**: Off-by-one error due to incorrect slicing (`-n-1` instead of `-n`).

## bug2.js
- **Intended Behavior**: Count occurrences of each word in a string.
- **Current Issue**: Loop runs one step too far (`i <= words.length`), causing `undefined` key.

## bug3.java
- **Intended Behavior**: Calculate the average of an array.
- **Current Issue**: Integer division truncates decimal values.

## bug4.py
- **Intended Behavior**: Remove duplicates while preserving original order.
- **Current Issue**: Using `sorted()` changes the order of elements.

## bug5.js
- **Intended Behavior**: Fetch user data asynchronously and return the name.
- **Current Issue**: Missing `await`, so it returns a Promise instead of resolved value.