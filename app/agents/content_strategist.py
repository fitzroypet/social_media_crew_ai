from crewai import Agent
from typing import List

class ContentStrategist:
    def __init__(self):
        self.agent = Agent(
            role='Content Strategist',
            goal='Create engaging social media content strategies',
            backstory='Expert in social media content planning',
            verbose=True
        )

    def generate_content_ideas(self, niche: str, target_audience: str) -> List[str]:
        prompt = f"""
        Generate 5 engaging content ideas for:
        Niche: {niche}
        Target Audience: {target_audience}
        
        Format each idea in a new line.
        Make them creative and engaging.
        """
        
        return self.agent.execute(prompt).split('\n')
