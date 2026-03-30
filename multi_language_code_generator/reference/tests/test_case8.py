import unittest
from recommendation_engine import RecommendationEngine

class TestCase8(unittest.TestCase):
    def test_recommend_for_nonexistent_user(self):
        engine = RecommendationEngine()
        engine.user_item_ratings = {1:{101:5}, 2:{102:4}}
        recs = engine.recommend_for_user(999)
        self.assertEqual(recs, [])

if __name__ == "__main__":
    unittest.main()