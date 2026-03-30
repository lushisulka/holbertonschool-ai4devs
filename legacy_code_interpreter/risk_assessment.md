# Risk Assessment

| Risk                          | Severity | Notes                                                                                     |
|-------------------------------|----------|-------------------------------------------------------------------------------------------|
| Missing input validation      | High     | Allows malicious input (e.g., SQL injection) that can compromise database security.      |
| Broken authentication logic   | High     | Lack of JWT expiration checks can allow unauthorized users to access protected routes.   |
| Missing authorization control | High     | Users can perform restricted actions (e.g., add reviews) without proper permissions.     |
| Unbounded database queries    | Medium   | Pagination without limits or indexing can slow down the system under large datasets.     |
| Inconsistent error handling   | Medium   | Lack of standardized error responses confuses clients and complicates debugging.         |
| Invalid user input handling   | Medium   | No constraints (e.g., rating range) leads to unreliable and inconsistent stored data.    |
| Missing default parameters    | Medium   | API may break or behave unpredictably when required query parameters are absent.         |
| Tight coupling (controller-DB)| Low      | Business logic is not separated, making testing and future changes difficult.            |
| No logging or monitoring      | Low      | System failures and security incidents cannot be tracked or analyzed effectively.        |