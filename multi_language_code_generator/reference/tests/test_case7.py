import unittest
from recommendation_engine import RecommendationEngine

class TestCase7(unittest.TestCase):
    def test_scores_order(self):
        engine = RecommendationEngine()
        engine.user_item_ratings = {
            1:{101:5}, 2:{102:3, 103:4}, 3:{103:5}
        }
        recs = engine.recommend_for_user(1)
        scores = [r["score"] for r in recs]
        self.assertEqual(scores, sorted(scores, reverse=True))

if __name__ == "__main__":
    unittest.main()