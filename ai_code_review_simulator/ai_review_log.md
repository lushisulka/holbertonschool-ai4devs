# AI Review Log

## Inline Comments

- (tasks.py, line 3) Consider adding input validation for `tasks` to ensure it is a list.
- (tasks.py, line 5) `status` check could be stricter (e.g., avoid falsy values like empty string).
- (tasks.py, line 8) Default value for `priority` should be explicitly documented.
- (tasks.py, line 10) Loop could be replaced with list comprehension for better readability.
- (tasks.py, line 13) Function lacks docstring explaining parameters and return value.

---

## Global Feedback

- Maintainability: Function is readable but could be split if more filters are added in future.
- Performance: Current implementation is O(n), which is fine, but indexing or pre-grouping could help for large datasets.
- Security: No direct security risks, but input validation is recommended to avoid malformed task objects.
- Code Style: Add type hints for better clarity and maintainability.
- Testing: No explicit unit tests included; recommend adding pytest cases.
- Scalability: Filtering logic may become complex if more attributes are added (consider filter pipeline design).
- Documentation: Add examples of usage in docstring or README.
- Consistency: Ensure all task objects follow same schema to avoid runtime errors.

---

## Summary
Overall PR is clean and functional, but can be improved in:
- validation
- documentation
- scalability design