import os
from dotenv import load_dotenv
from src.modules.hashtag_recommender import HashtagRecommender

def test_hashtag_recommendations():
    try:
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment variables
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables")

        # Initialize the hashtag recommender
        recommender = HashtagRecommender(api_key)

        # Test parameters
        topic = "sustainable fashion"
        platform = "Instagram"
        audience = "environmentally conscious millennials"

        # Generate hashtag recommendations
        print("Generating hashtag recommendations...")
        result = recommender.recommend_hashtags(topic, platform, audience)

        # Print results
        print("\n=== Recommended Hashtags ===\n")
        print(result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_hashtag_recommendations() 