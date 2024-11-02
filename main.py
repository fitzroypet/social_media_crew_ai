import os
from dotenv import load_dotenv
from app.agents.content_strategist import ContentStrategist

# Load environment variables
load_dotenv()

def main():
    # Create content strategist
    strategist = ContentStrategist()
    
    # Test content generation
    ideas = strategist.generate_content_ideas(
        niche="Tech Startups",
        target_audience="Young Entrepreneurs"
    )
    
    print("\nGenerated Content Ideas:")
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. {idea.strip()}")

if __name__ == "__main__":
    main()
