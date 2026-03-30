import unittest
from recommendation_engine import RecommendationEngine

class TestCase3(unittest.TestCase):
    def test_single_user(self):
        engine = RecommendationEngine()
        engine.user_item_ratings = {1:{101:5}}
        recs = engine.recommend_for_user(1)
        self.assertEqual(recs, [])

if __name__ == "__main__":
    unittest.main()