import streamlit as st
import os
from dotenv import load_dotenv

# Import modules using relative paths
from ..modules.content_generator import ContentGenerator
from ..modules.time_optimizer import TimeOptimizer
from ..modules.hashtag_recommender import HashtagRecommender

# Load environment variables
load_dotenv()

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

def main():
    # Header
    st.title("🚀 Social Media Strategy Assistant")
    st.markdown("---")

    # Sidebar for inputs
    with st.sidebar:
        st.header("Configure Your Strategy")
        
        platform = st.selectbox(
            "Select Platform",
            ["Instagram", "Twitter", "LinkedIn", "TikTok"]
        )
        
        topic = st.text_input(
            "Content Topic",
            placeholder="e.g., Sustainable Fashion"
        )
        
        audience = st.text_input(
            "Target Audience",
            placeholder="e.g., Environmentally conscious millennials"
        )
        
        timezone = st.selectbox(
            "Select Timezone",
            ["EST", "CST", "MST", "PST", "GMT"]
        )
        
        generate = st.button("Generate Strategy 🎯")

    # Main content area
    if generate and topic and audience:
        try:
            with st.spinner("Generating your social media strategy..."):
                # Initialize our modules
                api_key = os.getenv('OPENAI_API_KEY')
                content_gen = ContentGenerator(api_key)
                time_opt = TimeOptimizer(api_key)
                hashtag_rec = HashtagRecommender(api_key)

                # Create three columns for results
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.subheader("📝 Content Ideas")
                    content_ideas = content_gen.generate_content_ideas(
                        topic, platform, audience
                    )
                    st.markdown(content_ideas)

                with col2:
                    st.subheader("⏰ Best Posting Times")
                    posting_times = time_opt.suggest_posting_times(
                        platform, timezone, audience
                    )
                    st.markdown(posting_times)

                with col3:
                    st.subheader("#️⃣ Recommended Hashtags")
                    hashtags = hashtag_rec.recommend_hashtags(
                        topic, platform, audience
                    )
                    st.markdown(hashtags)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    elif generate:
        st.warning("Please fill in all required fields.")

if __name__ == "__main__":
    main
