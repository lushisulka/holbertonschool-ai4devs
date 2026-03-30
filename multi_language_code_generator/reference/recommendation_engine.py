import csv
from collections import defaultdict
from math import sqrt

class RecommendationEngine:
    def __init__(self):
        self.user_item_ratings = defaultdict(dict)

    def load_interactions(self, filepath: str):
        """Load user-item interactions from CSV file."""
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                user = int(row["user_id"])
                item = int(row["item_id"])
                rating = float(row["rating"])
                self.user_item_ratings[user][item] = rating

    def cosine_similarity(self, ratings1, ratings2):
        """Compute cosine similarity between two users/items."""
        common_items = set(ratings1.keys()) & set(ratings2.keys())
        if not common_items:
            return 0.0
        sum_xy = sum(ratings1[i] * ratings2[i] for i in common_items)
        sum_x2 = sum(ratings1[i]**2 for i in common_items)
        sum_y2 = sum(ratings2[i]**2 for i in common_items)
        return sum_xy / (sqrt(sum_x2) * sqrt(sum_y2))

    def recommend_for_user(self, user_id, top_n=5):
        """Generate top-N recommendations for a user."""
        scores = defaultdict(float)
        for other_user, ratings in self.user_item_ratings.items():
            if other_user == user_id:
                continue
            sim = self.cosine_similarity(self.user_item_ratings[user_id], ratings)
            for item, rating in ratings.items():
                if item not in self.user_item_ratings[user_id]:
                    scores[item] += sim * rating

        # Return top-N items sorted by score
        recommended = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
        return [{"item_id": item, "score": score} for item, score in recommended[:top_n]]