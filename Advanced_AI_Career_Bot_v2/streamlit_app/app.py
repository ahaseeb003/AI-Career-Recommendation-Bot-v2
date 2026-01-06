"""
Advanced AI Career Bot v2.0
Enhanced with Multi-Source Training, OpenRouter Integration, and Roadmap.sh
"""

import streamlit as st
import sys
import os
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent))

from utils.model_loader import load_model, get_career_recommendations
from utils.resource_finder import get_learning_resources, get_salary_info
from utils.openrouter_agent import OpenRouterAgent
from utils.roadmap_fetcher import fetch_career_roadmap
from utils.books_recommender import recommend_books
import json

# Page configuration
st.set_page_config(
    page_title="Advanced AI Career Bot v2.0",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .career-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .confidence-badge {
        background: rgba(255,255,255,0.2);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin-top: 0.5rem;
    }
    .resource-box {
        background: #f8f9fa;
        border-left: 4px solid #667eea;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 5px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.1rem;
        cursor: pointer;
        transition: all 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(102,126,234,0.3);
    }
    .book-card {
        background: white;
        border: 1px solid #e0e0e0;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        transition: all 0.3s;
    }
    .book-card:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'openrouter_agent' not in st.session_state:
    st.session_state.openrouter_agent = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def main():
    # Header
    st.markdown('<h1 class="main-header">🚀 Advanced AI Career Bot v2.0</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Discover Your Perfect Career Path with AI-Powered Multi-Source Intelligence</p>',
        unsafe_allow_html=True
    )
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/clouds/200/000000/business-building.png", width=150)
        st.markdown("## 🎯 Features")
        st.markdown("""
        - ✅ **Multi-Source Training** - Career data, skills, jobs, books
        - 🤖 **OpenRouter AI Agent** - Powered by multiple LLMs
        - 🗺️ **roadmap.sh Integration** - Real-world career roadmaps
        - 📚 **Smart Book Recommendations** - Curated learning resources
        - 💰 **Salary Insights** - Industry-standard compensation
        - 🎓 **Learning Paths** - Courses, certifications, projects
        """)
        
        st.markdown("---")
        
        # OpenRouter API Key
        st.markdown("### 🔑 OpenRouter API Key")
        api_key = st.text_input(
            "Enter your OpenRouter API key",
            type="password",
            help="Get your API key from https://openrouter.ai"
        )
        
        if api_key:
            if st.session_state.openrouter_agent is None:
                st.session_state.openrouter_agent = OpenRouterAgent(api_key)
                st.success("✅ OpenRouter Agent Connected!")
        
        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.info("""
        This AI Career Bot uses multiple data sources and advanced AI models
        to provide personalized career recommendations, learning paths, and
        interactive career guidance.
        
        **Version:** 2.0  
        **Model:** Multi-Source Trained  
        **AI Agent:** OpenRouter  
        """)
    
    # Main content tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎯 Career Matching",
        "🗺️ Career Roadmap",
        "📚 Book Recommendations",
        "💬 AI Career Coach",
        "📊 Interview Prep"
    ])
    
    # Tab 1: Career Matching
    with tab1:
        st.markdown("## 🎯 Find Your Perfect Career Match")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # User input
            st.markdown("### Tell us about yourself")
            
            user_description = st.text_area(
                "Describe your skills, interests, and career goals",
                placeholder="Example: I love working with data, solving complex problems, and building machine learning models. I have experience with Python and statistics...",
                height=150
            )
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                skills = st.multiselect(
                    "Select your core skills",
                    ["Python", "JavaScript", "Java", "C++", "SQL", "Machine Learning",
                     "Data Analysis", "Web Development", "Mobile Development", "Cloud Computing",
                     "DevOps", "Cybersecurity", "UI/UX Design", "Project Management"]
                )
            
            with col_b:
                experience = st.select_slider(
                    "Experience Level",
                    options=["Beginner", "Intermediate", "Advanced", "Expert"]
                )
            
            education = st.selectbox(
                "Education Background",
                ["High School", "Associate Degree", "Bachelor's Degree", 
                 "Master's Degree", "PhD", "Self-Taught"]
            )
            
            if st.button("🔍 Get Career Recommendations", use_container_width=True):
                if not user_description:
                    st.warning("⚠️ Please describe your skills and interests first!")
                else:
                    with st.spinner("🤔 Analyzing your profile with AI..."):
                        try:
                            # Load model if not loaded
                            if not st.session_state.model_loaded:
                                load_model()
                                st.session_state.model_loaded = True
                            
                            # Create enhanced query
                            enhanced_query = f"{user_description} Skills: {', '.join(skills)}. Experience: {experience}. Education: {education}."
                            
                            # Get recommendations
                            recommendations = get_career_recommendations(enhanced_query, top_k=5)
                            st.session_state.recommendations = recommendations
                            
                            st.success("✅ Analysis complete! See your recommendations below.")
                        
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")
                            st.info("💡 Tip: Make sure the model files are in the 'models/' directory")
        
        with col2:
            st.markdown("### 💡 Quick Tips")
            st.info("""
            **For best results:**
            
            1. Be specific about your skills
            2. Mention technologies you know
            3. Describe what you enjoy doing
            4. Include any projects or experience
            5. Mention your career goals
            """)
            
            with st.expander("📖 Example Descriptions"):
                st.markdown("""
                **Example 1: Data Science**
                > "I love analyzing data and finding patterns. I'm proficient in Python, 
                > pandas, and scikit-learn. I enjoy creating visualizations and building 
                > predictive models. Looking to work with big data and ML."
                
                **Example 2: Web Development**
                > "I enjoy creating beautiful user interfaces and interactive websites. 
                > I know React, JavaScript, CSS, and have built several web applications. 
                > I want to become a full-stack developer."
                
                **Example 3: DevOps**
                > "I'm passionate about automation and infrastructure. I have experience 
                > with Docker, Kubernetes, CI/CD pipelines, and cloud platforms. 
                > Looking to work in cloud engineering."
                """)
        
        # Display recommendations
        if st.session_state.recommendations:
            st.markdown("---")
            st.markdown("## 🎓 Your Career Recommendations")
            
            for i, rec in enumerate(st.session_state.recommendations, 1):
                with st.container():
                    st.markdown(f"""
                    <div class="career-card">
                        <h2 style="margin:0; color:white;">#{i} {rec['career']}</h2>
                        <div class="confidence-badge">Confidence: {rec['confidence']:.1f}%</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("### 📚 Learning Resources")
                        resources = get_learning_resources(rec['career'])
                        
                        if resources['courses']:
                            st.markdown("**Recommended Courses:**")
                            for course in resources['courses'][:3]:
                                st.markdown(f"- {course}")
                        
                        if resources['certifications']:
                            st.markdown("**Certifications:**")
                            for cert in resources['certifications'][:2]:
                                st.markdown(f"- {cert}")
                    
                    with col2:
                        st.markdown("### 💰 Salary Information")
                        salary_info = get_salary_info(rec['career'])
                        
                        st.metric("Entry Level", salary_info['entry'])
                        st.metric("Mid Level", salary_info['mid'])
                        st.metric("Senior Level", salary_info['senior'])
                    
                    st.markdown("---")
    
    # Tab 2: Career Roadmap
    with tab2:
        st.markdown("## 🗺️ Career Learning Roadmap")
        st.markdown("*Powered by [roadmap.sh](https://roadmap.sh)*")
        
        selected_career = st.selectbox(
            "Select a career path to explore",
            ["Frontend Developer", "Backend Developer", "Full Stack Developer",
             "DevOps Engineer", "Data Scientist", "Machine Learning Engineer",
             "Cybersecurity Engineer", "Mobile Developer", "Cloud Engineer",
             "AI Engineer", "Game Developer", "Blockchain Developer"]
        )
        
        if st.button("📖 Load Career Roadmap", use_container_width=True):
            with st.spinner(f"Loading roadmap for {selected_career}..."):
                roadmap = fetch_career_roadmap(selected_career)
                
                if roadmap:
                    st.success(f"✅ Roadmap loaded for {selected_career}")
                    
                    # Display roadmap sections
                    for section in roadmap['sections']:
                        with st.expander(f"📍 {section['title']}", expanded=True):
                            st.markdown(section['description'])
                            
                            if 'topics' in section:
                                st.markdown("**Key Topics:**")
                                for topic in section['topics']:
                                    st.markdown(f"- {topic}")
                            
                            if 'resources' in section:
                                st.markdown("**Learning Resources:**")
                                for resource in section['resources']:
                                    st.markdown(f"- [{resource['title']}]({resource['url']})")
                else:
                    st.warning("⚠️ Roadmap not available for this career path yet.")
                    st.info("💡 Try exploring the AI Career Coach tab for personalized guidance!")
    
    # Tab 3: Book Recommendations
    with tab3:
        st.markdown("## 📚 Curated Book Recommendations")
        st.markdown("Find the best books to advance your career")
        
        career_for_books = st.selectbox(
            "Select your career interest",
            ["Data Science", "Machine Learning", "Software Engineering",
             "Web Development", "DevOps", "Cybersecurity", "Cloud Computing",
             "AI & Deep Learning", "Mobile Development", "Game Development",
             "Product Management", "System Design"]
        )
        
        if st.button("📖 Get Book Recommendations", use_container_width=True):
            books = recommend_books(career_for_books)
            
            st.markdown(f"### Top Books for {career_for_books}")
            
            cols = st.columns(2)
            for idx, book in enumerate(books):
                with cols[idx % 2]:
                    st.markdown(f"""
                    <div class="book-card">
                        <h4>{book['title']}</h4>
                        <p><strong>Author:</strong> {book['author']}</p>
                        <p><strong>Level:</strong> {book['level']}</p>
                        <p>{book['description']}</p>
                        <p><em>⭐ Rating: {book['rating']}/5</em></p>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Tab 4: AI Career Coach
    with tab4:
        st.markdown("## 💬 AI Career Coach")
        st.markdown("*Powered by OpenRouter - Access to 300+ AI models*")
        
        if not api_key:
            st.warning("⚠️ Please enter your OpenRouter API key in the sidebar to use the AI Career Coach")
            st.info("""
            **How to get started:**
            1. Sign up at [OpenRouter](https://openrouter.ai)
            2. Get your API key
            3. Enter it in the sidebar
            4. Start chatting with your AI career coach!
            """)
        else:
            # Chat interface
            st.markdown("### Ask me anything about your career!")
            
            # Display chat history
            for message in st.session_state.chat_history:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            # User input
            user_input = st.chat_input("Ask about career paths, skills, salary, interview tips, etc.")
            
            if user_input:
                # Add user message
                st.session_state.chat_history.append({"role": "user", "content": user_input})
                
                with st.chat_message("user"):
                    st.markdown(user_input)
                
                # Get AI response
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = st.session_state.openrouter_agent.get_career_advice(
                            user_input,
                            context=st.session_state.recommendations
                        )
                        st.markdown(response)
                        
                        # Add to history
                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": response
                        })
            
            # Clear chat button
            if st.button("🗑️ Clear Chat History"):
                st.session_state.chat_history = []
                st.rerun()
    
    # Tab 5: Interview Prep
    with tab5:
        st.markdown("## 📊 Interview Preparation")
        
        interview_career = st.selectbox(
            "Select career to prepare for",
            ["Software Engineer", "Data Scientist", "DevOps Engineer",
             "Frontend Developer", "Backend Developer", "Product Manager",
             "Machine Learning Engineer", "Cybersecurity Engineer"]
        )
        
        interview_type = st.radio(
            "Interview Type",
            ["Technical Questions", "Behavioral Questions", "System Design", "Coding Practice"]
        )
        
        if st.button("📝 Generate Interview Questions", use_container_width=True):
            if not api_key:
                st.warning("⚠️ Please enter your OpenRouter API key in the sidebar")
            else:
                with st.spinner("Generating interview questions..."):
                    prompt = f"Generate 10 {interview_type.lower()} for a {interview_career} interview. Include the questions and brief answer guidelines."
                    
                    questions = st.session_state.openrouter_agent.get_career_advice(prompt)
                    st.markdown(questions)
        
        st.markdown("---")
        st.markdown("### 💡 Interview Tips")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Before the Interview:**
            - Research the company
            - Review job description
            - Prepare STAR stories
            - Practice coding problems
            - Prepare questions to ask
            """)
        
        with col2:
            st.markdown("""
            **During the Interview:**
            - Think out loud
            - Ask clarifying questions
            - Be honest about what you don't know
            - Show enthusiasm
            - Take notes
            """)

if __name__ == "__main__":
    main()
