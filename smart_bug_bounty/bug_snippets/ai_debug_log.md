bug1.py

AI Explanation: The function uses lst[-n-1:], which causes an off-by-one error and returns one extra element. For example, requesting the last 2 items returns 3 items instead.
Suggested Fix: Change the slice to lst[-n:] so it correctly returns the last n elements.
Confidence: High

bug2.js

AI Explanation: The loop condition uses i <= words.length, which causes the loop to run one extra time. This results in undefined being processed as a word and added to the counts object.
Suggested Fix: Change the loop condition to i < words.length.
Confidence: High

bug3.java

AI Explanation: The division sum / nums.length performs integer division because both operands are integers. This truncates the decimal part and produces incorrect results.
Suggested Fix: Cast one operand to double: (double) sum / nums.length.
Confidence: High

bug4.py

AI Explanation: The function removes duplicates correctly but then applies sorted(), which changes the original order of elements. This violates the requirement to preserve insertion order.
Suggested Fix: Return result directly instead of sorted(result).
Confidence: High

bug5.js

AI Explanation: The function fetchUser() returns a Promise, but getUserName() does not use await. As a result, user is a Promise object, and accessing user.name returns undefined.
Suggested Fix: Add await when calling fetchUser():

const user = await fetchUser();