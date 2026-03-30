# Risk Assessment

| Risk                          | Severity | Notes                                                                 |
|-------------------------------|----------|----------------------------------------------------------------------|
| Missing input validation      | High     | Functions like createPlace() and addReview() do not validate inputs. |
| Weak authentication handling  | High     | authenticateUser() lacks token expiration checks.                    |
| No authorization checks       | High     | addReview() does not verify if user is authenticated.                |
| Poor error handling           | Medium   | Errors are not consistently handled or returned clearly.             |
| Inefficient database queries  | Medium   | Pagination may become slow with large datasets.                      |
| Lack of default parameters    | Medium   | getPlacesWithPagination() may fail without defaults.                 |
| No rating constraints         | Medium   | addReview() does not enforce rating limits (e.g., 1–5).              |
| Tight coupling to database    | Low      | Direct DB calls in controllers reduce flexibility.                   |
| Missing logging mechanism     | Low      | Harder to debug and trace issues in production.                      |