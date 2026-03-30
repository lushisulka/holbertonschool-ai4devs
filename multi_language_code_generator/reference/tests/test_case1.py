import unittest
from recommendation_engine import RecommendationEngine

class TestCase1(unittest.TestCase):
    def test_recommend_user_normal(self):
        engine = RecommendationEngine()
        engine.user_item_ratings = {
            1: {101: 5, 102: 3},
            2: {101: 4, 103: 5}
        }
        recs = engine.recommend_for_user(1)
        self.assertTrue(all(item["item_id"] not in [101, 102] for item in recs))

if __name__ == "__main__":
    unittest.main()