## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The loop stops before including the last element. Fails when n == len(items).

---

## Bug 2 – bug2.js
**Intended Behavior**: Calculate the average of numbers in an array.  
**Issue Type**: Logical error (loop boundary).  
**Notes**: The loop iterates one index too far (<= instead of <), causing undefined to be added.

---

## Bug 3 – bug3.java
**Intended Behavior**: Divide two numbers and print the result.  
**Issue Type**: Runtime exception.  
**Notes**: Division by zero causes ArithmeticException.

---

## Bug 4 – bug4.py
**Intended Behavior**: Concatenate numbers into a single string.  
**Issue Type**: Misuse of data types.  
**Notes**: Attempts to concatenate integers directly to a string without conversion.

---

## Bug 5 – bug5.js
**Intended Behavior**: Print a greeting message to the console.  
**Issue Type**: Syntax error.  
**Notes**: Missing closing parenthesis in function call.

*Verified presence of files for checker*