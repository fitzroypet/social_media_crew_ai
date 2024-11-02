import os
from dotenv import load_dotenv
from src.modules.time_optimizer import TimeOptimizer

def test_time_optimization():
    try:
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment variables
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables")

        # Initialize the time optimizer
        optimizer = TimeOptimizer(api_key)

        # Test parameters
        platform = "Instagram"
        timezone = "EST"
        audience = "young professionals"

        # Generate timing suggestions
        print("Generating posting time suggestions...")
        result = optimizer.suggest_posting_times(platform, timezone, audience)

        # Print results
        print("\n=== Suggested Posting Times ===\n")
        print(result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_time_optimization() 