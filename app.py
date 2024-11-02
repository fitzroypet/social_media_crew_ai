import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
import warnings
from src.modules.content_generator import ContentGenerator
from src.modules.time_optimizer import TimeOptimizer
from src.modules.hashtag_recommender import HashtagRecommender

# Filter out the TracerProvider warning
warnings.filterwarnings('ignore', message='Overriding of current TracerProvider is not allowed')

# Initialize session state if not already done
if 'results_generated' not in st.session_state:
    st.session_state.results_generated = False

# Page configuration
st.set_page_config(
    page_title="Social Media Strategy Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern, minimalist design
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        border: none;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stSelectbox>div>div>select {
        border-radius: 5px;
    }
    h1, h2, h3 {
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

def validate_inputs(topic, audience):
    """Validate user inputs"""
    errors = []
    
    if not topic:
        errors.append("Content topic is required")
    elif len(topic) < 3:
        errors.append("Content topic must be at least 3 characters long")
        
    if not audience:
        errors.append("Target audience is required")
    elif len(audience) < 5:
        errors.append("Target audience description must be at least 5 characters long")
        
    return errors

def export_results(content_ideas, posting_times, hashtags, topic):
    """Export results to CSV"""
    # Create a dictionary with all results
    results = {
        'Topic': [topic],
        'Content Ideas': [content_ideas],
        'Posting Times': [posting_times],
        'Hashtags': [hashtags]
    }
    
    # Convert to DataFrame
    df = pd.DataFrame(results)
    
    # Generate CSV
    csv = df.to_csv(index=False)
    
    return csv

def main():
    # Header
    st.title("🚀 Social Media Strategy Assistant")
    st.markdown("---")

    try:
        # Load environment variables
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            st.error("OpenAI API key not found. Please check your .env file.")
            st.stop()

        # Sidebar for inputs
        with st.sidebar:
            st.header("Configure Your Strategy")
            
            platform = st.selectbox(
                "Select Platform",
                ["Instagram", "Twitter", "LinkedIn", "TikTok"],
                key='platform'
            )
            
            topic = st.text_input(
                "Content Topic",
                placeholder="e.g., Sustainable Fashion",
                key='topic'
            )
            
            audience = st.text_input(
                "Target Audience",
                placeholder="e.g., Environmentally conscious millennials",
                key='audience'
            )
            
            timezone = st.selectbox(
                "Select Timezone",
                ["EST", "CST", "MST", "PST", "GMT"],
                key='timezone'
            )
            
            generate = st.button("Generate Strategy 🎯", key='generate_button')

            if st.button("Clear Results", key='clear_button'):
                st.session_state.results_generated = False
                st.experimental_rerun()

        # Main content area
        if not st.session_state.results_generated:
            st.markdown("""
            ### 👋 Welcome to Social Media Strategy Assistant!
            
            1. Select your target platform
            2. Enter your content topic
            3. Define your target audience
            4. Choose your timezone
            5. Click 'Generate Strategy' to get started
            
            Your personalized social media strategy will appear here.
            """)

        if generate:
            errors = validate_inputs(topic, audience)
            if errors:
                for error in errors:
                    st.sidebar.error(error)
            else:
                try:
                    with st.spinner("Generating your social media strategy..."):
                        # Initialize our modules
                        content_gen = ContentGenerator(api_key)
                        time_opt = TimeOptimizer(api_key)
                        hashtag_rec = HashtagRecommender(api_key)

                        # Generate content
                        content_ideas = content_gen.generate_content_ideas(
                            topic, platform, audience
                        )
                        posting_times = time_opt.suggest_posting_times(
                            platform, timezone, audience
                        )
                        hashtags = hashtag_rec.recommend_hashtags(
                            topic, platform, audience
                        )

                        st.session_state.results_generated = True

                        # Display results in columns
                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.subheader("📝 Content Ideas")
                            st.markdown(content_ideas)

                        with col2:
                            st.subheader("⏰ Best Posting Times")
                            st.markdown(posting_times)

                        with col3:
                            st.subheader("#️⃣ Recommended Hashtags")
                            st.markdown(hashtags)

                        # Add success message
                        st.success("Strategy generated successfully! 🎉")

                        # Add export button
                        csv = export_results(content_ideas, posting_times, hashtags, topic)
                        st.download_button(
                            label="Download Results 📥",
                            data=csv,
                            file_name=f"social_media_strategy_{topic.lower().replace(' ', '_')}.csv",
                            mime="text/csv"
                        )

                except Exception as e:
                    st.error(f"An error occurred while generating content: {str(e)}")
                    st.error("Please try again or contact support if the problem persists.")

    except Exception as e:
        st.error(f"Application Error: {str(e)}")
        st.error("Please refresh the page or contact support.")

if __name__ == "__main__":
    main() 