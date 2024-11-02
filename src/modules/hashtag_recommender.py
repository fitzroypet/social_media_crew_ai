from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

class HashtagRecommender:
    def __init__(self, openai_api_key):
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            api_key=openai_api_key
        )

    def create_hashtag_agent(self):
        return Agent(
            role='Hashtag Strategy Specialist',
            goal='Generate effective and relevant hashtags for maximum reach',
            backstory="""You are a social media hashtag expert who understands 
            trending topics, audience behavior, and hashtag optimization strategies. 
            You know how to balance popular and niche hashtags for maximum visibility.""",
            llm=self.llm
        )

    def recommend_hashtags(self, content_topic, platform, target_audience):
        agent = self.create_hashtag_agent()
        
        task = Task(
            description=f"""Generate optimized hashtag recommendations for {platform} content about {content_topic}.
            Target audience: {target_audience}
            
            Consider:
            1. Mix of popular and niche hashtags
            2. Platform-specific hashtag strategies
            3. Current trends in the topic
            4. Audience-specific hashtags""",
            expected_output="""Provide a structured list of hashtags including:
            1. 5 Popular hashtags (100k+ posts)
            2. 5 Niche-specific hashtags
            3. 5 Trending hashtags
            4. Brief explanation for each category
            5. Tips for optimal hashtag usage
            
            Format each category clearly and include post volume when relevant.""",
            agent=agent
        )

        crew = Crew(
            agents=[agent],
            tasks=[task]
        )

        result = crew.kickoff()
        return result
