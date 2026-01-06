# Usage Guide

## Advanced AI Career Bot v2.0 - Complete User Manual

This guide provides detailed instructions on how to use all features of the Advanced AI Career Bot.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Career Matching](#career-matching)
3. [Career Roadmaps](#career-roadmaps)
4. [Book Recommendations](#book-recommendations)
5. [AI Career Coach](#ai-career-coach)
6. [Interview Preparation](#interview-preparation)
7. [Tips & Best Practices](#tips--best-practices)

## Getting Started

### First Launch

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. The app opens at `http://localhost:8501`

3. You'll see five main tabs:
   - 🎯 Career Matching
   - 🗺️ Career Roadmap
   - 📚 Book Recommendations
   - 💬 AI Career Coach
   - 📊 Interview Prep

### Sidebar Configuration

The sidebar provides:
- **Features overview** - Quick reference
- **OpenRouter API Key input** - For AI coach (optional)
- **About section** - Version and model info

## Career Matching

### Purpose
Find careers that match your skills, interests, and goals using AI-powered analysis.

### Step-by-Step Guide

1. **Navigate to Career Matching Tab**
   - Click on "🎯 Career Matching"

2. **Describe Yourself**
   - In the text area, describe:
     - Your skills and expertise
     - What you enjoy doing
     - Your career goals
     - Any relevant experience
   
   **Example**:
   ```
   I love analyzing data and finding patterns. I'm proficient in Python,
   pandas, and scikit-learn. I enjoy creating visualizations and building
   predictive models. Looking to work with big data and ML.
   ```

3. **Select Core Skills**
   - Choose from the multiselect dropdown
   - Select 3-5 primary skills
   - Options include: Python, JavaScript, ML, Data Analysis, etc.

4. **Set Experience Level**
   - Use the slider to indicate your experience:
     - Beginner: 0-2 years
     - Intermediate: 2-5 years
     - Advanced: 5-10 years
     - Expert: 10+ years

5. **Choose Education Background**
   - Select from dropdown
   - Options: High School to PhD, Self-Taught

6. **Get Recommendations**
   - Click "🔍 Get Career Recommendations"
   - Wait 2-3 seconds for AI analysis

### Understanding Results

#### Career Cards
Each recommendation shows:
- **Career name** - e.g., "Data Scientist"
- **Confidence score** - Match percentage (higher is better)
- **Rank** - Position in recommendations (#1 is best match)

#### Learning Resources
For each career, you'll see:
- **Courses** - Top 3 recommended courses
- **Certifications** - Industry-recognized credentials
- **Practice Platforms** - Where to build skills

#### Salary Information
Three salary ranges:
- **Entry Level** - Starting salary range
- **Mid Level** - With 3-7 years experience
- **Senior Level** - 7+ years, leadership roles

### Tips for Better Results

✅ **Do:**
- Be specific about your skills
- Mention technologies you know
- Include projects or experience
- Describe what motivates you

❌ **Don't:**
- Use vague descriptions
- List unrelated skills
- Forget to mention experience level

## Career Roadmaps

### Purpose
Get structured learning paths powered by roadmap.sh for major tech careers.

### How to Use

1. **Navigate to Career Roadmap Tab**
   - Click "🗺️ Career Roadmap"

2. **Select Career Path**
   - Choose from dropdown:
     - Frontend Developer
     - Backend Developer
     - DevOps Engineer
     - Data Scientist
     - And more...

3. **Load Roadmap**
   - Click "📖 Load Career Roadmap"
   - Wait for content to load

### Understanding Roadmap Structure

Each roadmap contains:

#### Sections
- **Title** - Topic name
- **Description** - Overview of the area
- **Topics** - Key concepts to learn
- **Resources** - Curated learning materials

#### How to Follow a Roadmap

1. **Start from the top** - Follow sections in order
2. **Study each topic** - Don't skip fundamentals
3. **Use provided resources** - Click links for learning materials
4. **Practice** - Build projects for each section
5. **Track progress** - Check off completed topics

### Available Roadmaps

- **Frontend Developer** - HTML, CSS, JavaScript, React, etc.
- **Backend Developer** - APIs, Databases, Server logic
- **DevOps Engineer** - CI/CD, Docker, Kubernetes
- **Data Scientist** - Python, ML, Statistics
- **And more...**

## Book Recommendations

### Purpose
Discover curated books from comprehensive datasets to advance your career.

### How to Use

1. **Navigate to Book Recommendations Tab**
   - Click "📚 Book Recommendations"

2. **Select Career Interest**
   - Choose from dropdown
   - Options: Data Science, ML, Software Engineering, etc.

3. **Get Recommendations**
   - Click "📖 Get Book Recommendations"
   - View curated list instantly

### Understanding Book Cards

Each book shows:
- **Title** - Book name
- **Author** - Writer(s)
- **Level** - Beginner, Intermediate, Advanced
- **Rating** - Out of 5 stars
- **Description** - What you'll learn

### How to Choose Books

**For Beginners:**
- Start with "Beginner" or "Beginner to Intermediate" level
- Choose highly-rated books (4.5+)
- Look for "comprehensive guide" or "introduction"

**For Intermediate:**
- Focus on "Intermediate" or "All Levels"
- Choose specific topics you want to master
- Look for "practical" or "hands-on" books

**For Advanced:**
- Choose "Advanced" level books
- Focus on specialization
- Look for "comprehensive" or "definitive guide"

### Reading Strategy

1. **Start with fundamentals** - Build strong foundation
2. **Practice while reading** - Code along with examples
3. **One book at a time** - Don't overwhelm yourself
4. **Take notes** - Document key concepts
5. **Build projects** - Apply what you learn

## AI Career Coach

### Purpose
Get personalized career advice powered by OpenRouter's 300+ AI models.

### Setup

1. **Get API Key**
   - Visit [openrouter.ai](https://openrouter.ai)
   - Sign up for free account
   - Copy your API key

2. **Enter in Sidebar**
   - Paste key in "OpenRouter API Key" field
   - Wait for "✅ OpenRouter Agent Connected!"

### Using the Chat

1. **Navigate to AI Career Coach Tab**
   - Click "💬 AI Career Coach"

2. **Start Conversation**
   - Type your question in the chat input
   - Press Enter or click send

### What to Ask

**Career Guidance:**
```
- Should I learn React or Vue for frontend development?
- How do I transition from Software Engineer to ML Engineer?
- What skills should I focus on for DevOps?
```

**Learning Strategy:**
```
- Create a 6-month learning plan to become a Data Scientist
- What's the best order to learn backend technologies?
- How should I balance theory and practical projects?
```

**Interview Prep:**
```
- How do I prepare for a FAANG software engineering interview?
- What are common Data Science interview questions?
- Tips for behavioral interviews in tech?
```

**Salary & Negotiation:**
```
- Is $120k competitive for a senior developer in SF?
- How do I negotiate a higher salary offer?
- What benefits should I ask for besides salary?
```

**Career Decisions:**
```
- Should I take a job at a startup or big tech company?
- Is it worth getting a Master's degree for ML?
- How do I know if I'm ready for a senior role?
```

### Chat Features

- **Context-Aware** - Remembers conversation history
- **Personalized** - Uses your career recommendations if available
- **Multi-Model** - Powered by Claude, GPT-4, Gemini, and more
- **Clear Chat** - Button to start fresh conversation

## Interview Preparation

### Purpose
Generate practice questions and get interview guidance for your target role.

### How to Use

1. **Navigate to Interview Prep Tab**
   - Click "📊 Interview Preparation"

2. **Select Target Career**
   - Choose the role you're interviewing for
   - e.g., Software Engineer, Data Scientist

3. **Choose Interview Type**
   - **Technical Questions** - Coding, algorithms, system knowledge
   - **Behavioral Questions** - STAR method, soft skills
   - **System Design** - Architecture, scalability
   - **Coding Practice** - Algorithm problems

4. **Generate Questions**
   - Click "📝 Generate Interview Questions"
   - Requires OpenRouter API key
   - Wait 5-10 seconds for generation

### Understanding Generated Content

#### Technical Questions
- 10 relevant questions
- Answer guidelines
- Key concepts to cover
- Example solutions

#### Behavioral Questions
- STAR method scenarios
- What interviewers look for
- Example answers
- Tips for delivery

#### System Design
- Design problems
- Requirements clarification
- Architecture approaches
- Trade-offs to discuss

### Interview Tips Section

**Before Interview:**
- Research the company
- Review job description
- Prepare STAR stories
- Practice coding problems
- Prepare questions to ask

**During Interview:**
- Think out loud
- Ask clarifying questions
- Be honest about gaps
- Show enthusiasm
- Take notes

### Practice Strategy

1. **Daily Practice** - 1-2 hours daily for 2-3 weeks
2. **Mock Interviews** - Practice with friends or AI
3. **Track Progress** - Keep log of practiced questions
4. **Focus Weak Areas** - Spend extra time on challenges
5. **Stay Updated** - Review company's recent news

## Tips & Best Practices

### General Usage

**Maximize AI Recommendations:**
- Provide detailed descriptions (100+ words)
- Be honest about experience level
- Update profile as you grow
- Try different queries to explore

**Use Multiple Features:**
- Start with Career Matching
- Follow with Roadmap
- Get Book Recommendations
- Chat with AI Coach for guidance
- Practice Interview Questions

**Track Your Progress:**
- Save recommended careers
- Bookmark useful resources
- Document learning milestones
- Update your skills regularly

### AI Coach Best Practices

**Ask Specific Questions:**
❌ "How do I become a developer?"
✅ "I know Python and want to become a backend developer. Should I learn Django or Node.js first, and why?"

**Provide Context:**
Include:
- Current role/experience
- Your goals
- Constraints (time, budget)
- What you've tried

**Follow Up:**
- Ask for clarification
- Request examples
- Dig deeper into recommendations

### Learning Strategy

**70-20-10 Rule:**
- 70% - Hands-on practice and projects
- 20% - Learning from others (courses, mentors)
- 10% - Reading and theory

**Continuous Improvement:**
1. Set specific goals
2. Create learning schedule
3. Build projects regularly
4. Share your work
5. Get feedback
6. Iterate and improve

## Troubleshooting

### Career Recommendations Not Appearing

**Possible Causes:**
- Model files missing
- Query too short/vague
- Technical error

**Solutions:**
- Ensure model files in `models/` folder
- Write more detailed description (50+ words)
- Check console for errors

### AI Coach Not Responding

**Possible Causes:**
- No API key entered
- Invalid/expired API key
- Network issues
- Out of credits

**Solutions:**
- Verify API key in sidebar
- Check API key at OpenRouter dashboard
- Ensure internet connection
- Add credits to OpenRouter account

### Slow Performance

**Solutions:**
- Close other browser tabs
- Use CPU-optimized model
- Clear browser cache
- Restart application

## Advanced Features

### Custom Dataset Training

If you want to train on your own data:
1. See [Training Guide](TRAINING.md)
2. Prepare CSV files
3. Upload to Google Colab
4. Train model
5. Download and deploy

### API Integration

For developers wanting to integrate:
1. See [API Documentation](API.md)
2. Import utility functions
3. Build custom applications

## Keyboard Shortcuts

- **Ctrl/Cmd + K** - Focus search
- **Ctrl/Cmd + R** - Refresh app
- **Ctrl/Cmd + /** - Open dev tools

## Getting Help

**Documentation:**
- README.md - Overview
- INSTALLATION.md - Setup guide
- TRAINING.md - Custom training
- API.md - Developer reference

**Support:**
- GitHub Issues - Report bugs
- Community Forum - Ask questions
- Email - Direct support

## Conclusion

You now know how to:
- ✅ Get AI-powered career recommendations
- ✅ Follow structured roadmaps
- ✅ Find the best books to read
- ✅ Get personalized advice from AI coach
- ✅ Prepare for interviews

**Start exploring your perfect career path today!** 🚀

---

*Need more help? Check out other documentation files or reach out for support.*
