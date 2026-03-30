import unittest
from recommendation_engine import RecommendationEngine

class TestCase5(unittest.TestCase):
    def test_top_n_limit(self):
        engine = RecommendationEngine()
        engine.user_item_ratings = {
            1:{101:5}, 2:{102:3, 103:4}
        }
        recs = engine.recommend_for_user(1, top_n=1)
        self.assertLessEqual(len(recs), 1)

if __name__ == "__main__":
    unittest.main()