import os
import unittest
from dotenv import load_dotenv
from src.modules.content_generator import ContentGenerator
from src.modules.time_optimizer import TimeOptimizer
from src.modules.hashtag_recommender import HashtagRecommender

class TestSocialMediaModules(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load environment variables
        load_dotenv()
        cls.api_key = os.getenv('OPENAI_API_KEY')
        
        # Test parameters
        cls.topic = "sustainable fashion"
        cls.platform = "Instagram"
        cls.audience = "environmentally conscious millennials"
        cls.timezone = "EST"

    def test_content_generator(self):
        generator = ContentGenerator()
        result = generator.run()
        self.assertIsInstance(result.raw, str)
        self.assertGreater(len(result.raw), 0)

    def test_time_optimizer(self):
        optimizer = TimeOptimizer(self.api_key)
        result = optimizer.run()
        self.assertIsInstance(result.raw, str)
        self.assertGreater(len(result.raw), 0)

    def test_hashtag_recommender(self):
        recommender = HashtagRecommender(self.api_key)
        result = recommender.recommend_hashtags(
            self.topic,
            self.platform,
            self.audience
        )
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main() 