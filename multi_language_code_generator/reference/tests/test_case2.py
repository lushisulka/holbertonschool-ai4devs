import unittest
from recommendation_engine import RecommendationEngine

class TestCase2(unittest.TestCase):
    def test_empty_user(self):
        engine = RecommendationEngine()
        engine.user_item_ratings = {1:{101:5}, 2:{}}
        recs = engine.recommend_for_user(2)
        self.assertEqual(recs, [])

if __name__ == "__main__":
    unittest.main()