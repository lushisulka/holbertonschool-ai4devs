import unittest
from recommendation_engine import RecommendationEngine

class TestCase10(unittest.TestCase):
    def test_engine_load_and_recommend(self):
        import csv, os
        engine = RecommendationEngine()
        test_file = "temp_test.csv"
        with open(test_file,"w",newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["user_id","item_id","rating"])
            writer.writeheader()
            writer.writerow({"user_id":1,"item_id":101,"rating":5})
            writer.writerow({"user_id":2,"item_id":102,"rating":3})
        engine.load_interactions(test_file)
        recs = engine.recommend_for_user(1)
        os.remove(test_file)
        self.assertIsInstance(recs, list)

if __name__ == "__main__":
    unittest.main()