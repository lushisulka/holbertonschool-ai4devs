# Cross-Language Specification - Recommendation Engine

## Algorithm
Compute personalized item recommendations for users using collaborative filtering:
- Analyze user-item interactions (ratings, purchases, clicks)
- Find similar users or items
- Generate ranked list of recommended items per user

## Inputs
- CSV file with user-item interactions: `user_id,item_id,rating`

## Outputs
- JSON mapping users to recommended items with predicted scores

## Edge Cases
- Empty interaction matrix → return empty recommendations
- Users with no interactions → return popular items or empty list
- Items with no ratings → excluded from recommendations
- Single user or single item → handle gracefully
- Ties in predicted scores → resolve consistently

## Test Cases
- `matrix_small.csv` → 3 users, 5 items → top-2 recommendations per user
- `matrix_empty.csv` → empty file → empty JSON
- `matrix_single_user.csv` → 1 user, multiple items → recommendations handled
- `matrix_single_item.csv` → multiple users, 1 item → recommendations handled
- `matrix_tied_scores.csv` → 2 users, 4 items → tie-breaking verified