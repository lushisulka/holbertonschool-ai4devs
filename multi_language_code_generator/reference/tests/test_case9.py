import unittest
from recommendation_engine import RecommendationEngine

class TestCase9(unittest.TestCase):
    def test_recommend_multiple_users_items(self):
        engine = RecommendationEngine()
        engine.user_item_ratings = {
            1:{101:5,102:3}, 2:{101:4,103:5}, 3:{102:5,103:4}
        }
        recs = engine.recommend_for_user(3)
        self.assertTrue(len(recs) > 0)

if __name__ == "__main__":
    unittest.main()