import os
from dotenv import load_dotenv
from src.modules.content_generator import ContentGenerator

def test_content_generation():
    try:
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment variables
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables")

        # Initialize the content generator
        generator = ContentGenerator(api_key)

        # Test parameters
        topic = "sustainable fashion"
        platform = "Instagram"
        audience = "environmentally conscious millennials"

        # Generate content ideas
        print("Generating content ideas...")
        result = generator.generate_content_ideas(topic, platform, audience)

        # Print results
        print("\n=== Generated Content Ideas ===\n")
        print(result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_content_generation() 