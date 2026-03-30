import unittest
from recommendation_engine import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RecommendationEngine()
        # Example dataset
        self.engine.user_item_ratings = {
            1: {101: 5, 102: 3, 103: 2},
            2: {101: 4, 102: 2, 104: 5},
            3: {101: 2, 103: 5, 104: 3}
        }

    def test_recommend_user1(self):
        recs = self.engine.recommend_for_user(1)
        self.assertTrue(all(item["item_id"] not in [101,102,103] for item in recs))

    def test_recommend_user2(self):
        recs = self.engine.recommend_for_user(2)
        self.assertTrue(all(item["item_id"] not in [101,102,104] for item in recs))

    def test_top_n_limit(self):
        recs = self.engine.recommend_for_user(1, top_n=1)
        self.assertEqual(len(recs), 1)

    def test_empty_user(self):
        self.engine.user_item_ratings[4] = {}
        recs = self.engine.recommend_for_user(4)
        self.assertEqual(recs, [])

    def test_no_common_items(self):
        self.engine.user_item_ratings[5] = {105: 5}
        recs = self.engine.recommend_for_user(5)
        self.assertEqual(recs, [])

    def test_scores_order(self):
        recs = self.engine.recommend_for_user(1)
        scores = [r["score"] for r in recs]
        self.assertEqual(scores, sorted(scores, reverse=True))

    def test_single_user(self):
        single_engine = RecommendationEngine()
        single_engine.user_item_ratings = {1: {101: 5}}
        recs = single_engine.recommend_for_user(1)
        self.assertEqual(recs, [])

    def test_single_item(self):
        single_engine = RecommendationEngine()
        single_engine.user_item_ratings = {1: {101: 5}, 2: {101: 3}}
        recs = single_engine.recommend_for_user(1)
        self.assertEqual(recs, [])

    def test_multiple_users_items(self):
        recs = self.engine.recommend_for_user(3)
        self.assertTrue(len(recs) > 0)

    def test_recommend_for_nonexistent_user(self):
        recs = self.engine.recommend_for_user(999)
        self.assertEqual(recs, [])

if __name__ == "__main__":
    unittest.main()