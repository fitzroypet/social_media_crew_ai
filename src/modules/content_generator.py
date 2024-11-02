from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

class ContentGenerator:
    def __init__(self, openai_api_key):
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            api_key=openai_api_key
        )

    def create_content_agent(self):
        return Agent(
            role='Social Media Content Strategist',
            goal='Create engaging and relevant social media content ideas',
            backstory="""You are an experienced social media strategist with a 
            track record of creating viral content. You understand current trends,
            audience engagement, and what makes content shareable.""",
            llm=self.llm
        )

    def generate_content_ideas(self, topic, platform, audience):
        agent = self.create_content_agent()
        
        task = Task(
            description=f"""Generate 5 creative content ideas for {platform} about {topic}.
            The target audience is {audience}.
            For each idea include:
            1. Content type (post, story, reel, etc.)
            2. Main message
            3. Key elements to include
            4. Potential engagement hooks""",
            expected_output="""A list of 5 content ideas, each containing:
            - Content type
            - Main message
            - Key elements
            - Engagement hooks
            Please format each idea clearly and number them 1-5.""",
            agent=agent
        )

        crew = Crew(
            agents=[agent],
            tasks=[task]
        )

        result = crew.kickoff()
        return result
