bug1.py
Original Issue: Off-by-one error in slicing (lst[-n-1:] returns one extra item)
Fix Applied: Changed slice to lst[-n:]
Test Results: Test with n=2 returns [4, 5] → ✅ All test cases passed
bug2.js
Original Issue: Loop runs one extra iteration (i <= words.length) causing undefined entry in counts
Fix Applied: Changed loop condition to i < words.length
Test Results: Word count function works correctly; all tests passed ✅
bug3.java
Original Issue: Integer division truncates decimal (sum / nums.length)
Fix Applied: Cast numerator to double: (double) sum / nums.length
Test Results: Average calculation correct; all test cases passed ✅
bug4.py
Original Issue: sorted() changes original insertion order of elements
Fix Applied: Returned result directly instead of sorted(result)
Test Results: Duplicate removal preserves insertion order; all tests passed ✅
bug5.js
Original Issue: fetchUser() returns a Promise but await missing, causing undefined
Fix Applied: Added await when calling fetchUser()
Test Results: User name retrieved correctly; all tests passed ✅