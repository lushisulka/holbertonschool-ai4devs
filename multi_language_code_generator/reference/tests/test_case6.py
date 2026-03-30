import unittest
from recommendation_engine import RecommendationEngine

class TestCase6(unittest.TestCase):
    def test_no_common_items(self):
        engine = RecommendationEngine()
        engine.user_item_ratings = {1:{101:5}, 2:{102:3}}
        recs = engine.recommend_for_user(1)
        self.assertEqual(recs, [])

if __name__ == "__main__":
    unittest.main()