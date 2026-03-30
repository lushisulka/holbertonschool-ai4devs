# Risk Assessment

| Risk                         | Severity | Notes                                                                                  |
|------------------------------|----------|----------------------------------------------------------------------------------------|
| Missing input validation     | High     | Invalid or malicious data (e.g., SQL injection, empty fields) can corrupt database.   |
| Weak authentication handling | High     | Expired or forged JWT tokens may still be accepted, allowing unauthorized access.     |
| No authorization checks      | High     | Unauthenticated users could submit reviews or access protected actions.               |
| Poor error handling          | Medium   | Users receive unclear responses; debugging and issue tracking become difficult.       |
| Inefficient database queries | Medium   | Large datasets can cause slow response times and degrade system performance.          |
| Lack of default parameters   | Medium   | Missing page/limit values can crash endpoints or return inconsistent results.         |
| No rating constraints        | Medium   | Users can submit invalid ratings (e.g., 0 or 10), affecting data integrity.           |
| Tight coupling to database   | Low      | Changes in database structure require major controller modifications.                 |
| Missing logging mechanism    | Low      | Failures cannot be traced easily, increasing time to detect and fix issues.           |