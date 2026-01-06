"""
OpenRouter AI Agent Integration
Provides intelligent career coaching using multiple LLM models
"""

import requests
import json
from typing import Optional, Dict, List

class OpenRouterAgent:
    """AI Agent powered by OpenRouter for career guidance"""
    
    def __init__(self, api_key: str, model: str = "anthropic/claude-3.5-sonnet"):
        """
        Initialize OpenRouter Agent
        
        Args:
            api_key: OpenRouter API key
            model: Model to use (default: claude-3.5-sonnet)
                   Options: 
                   - anthropic/claude-3.5-sonnet (recommended)
                   - openai/gpt-4-turbo
                   - google/gemini-pro-1.5
                   - meta-llama/llama-3.1-70b-instruct
                   - anthropic/claude-3-opus
        """
        self.api_key = api_key
        self.model = model
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "https://github.com/advanced-ai-career-bot",
            "X-Title": "Advanced AI Career Bot v2.0",
            "Content-Type": "application/json"
        }
        
        # System prompt for career coaching
        self.system_prompt = """You are an expert career coach and advisor with deep knowledge of:
- Technology careers and industry trends
- Skills development and learning paths
- Interview preparation and job search strategies
- Salary negotiations and career growth
- Work-life balance and career transitions

Provide practical, actionable advice tailored to the user's specific situation.
Be encouraging, professional, and honest. If you don't know something, say so.
Use examples and specific recommendations when possible."""
    
    def get_career_advice(
        self, 
        user_query: str, 
        context: Optional[List[Dict]] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """
        Get career advice from the AI agent
        
        Args:
            user_query: User's question or request
            context: Optional context (e.g., career recommendations)
            temperature: Response creativity (0.0-1.0)
            max_tokens: Maximum response length
        
        Returns:
            AI-generated career advice
        """
        # Build messages
        messages = [
            {"role": "system", "content": self.system_prompt}
        ]
        
        # Add context if provided
        if context:
            context_str = "User's Career Recommendations:\n"
            for i, rec in enumerate(context[:3], 1):
                context_str += f"{i}. {rec['career']} (Confidence: {rec['confidence']:.1f}%)\n"
            
            messages.append({
                "role": "system",
                "content": f"Context: {context_str}\nUse this information to provide personalized advice."
            })
        
        # Add user query
        messages.append({
            "role": "user",
            "content": user_query
        })
        
        # Make API request
        try:
            payload = {
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=60
            )
            
            response.raise_for_status()
            result = response.json()
            
            return result['choices'][0]['message']['content']
        
        except requests.exceptions.RequestException as e:
            return f"Error communicating with AI: {str(e)}\n\nPlease check your API key and try again."
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def generate_interview_questions(
        self, 
        career: str, 
        question_type: str = "technical",
        count: int = 10
    ) -> str:
        """
        Generate interview questions for a specific career
        
        Args:
            career: Career/role name
            question_type: Type of questions (technical, behavioral, system_design)
            count: Number of questions to generate
        
        Returns:
            Formatted interview questions with answer guidelines
        """
        prompt = f"""Generate {count} {question_type} interview questions for a {career} position.

For each question, provide:
1. The question
2. Key points the interviewer is looking for
3. A brief example answer or approach

Format clearly with numbers and sections."""
        
        return self.get_career_advice(prompt, max_tokens=2000)
    
    def create_learning_plan(
        self,
        current_role: str,
        target_role: str,
        timeframe: str = "6 months"
    ) -> str:
        """
        Create a personalized learning plan
        
        Args:
            current_role: User's current role/skills
            target_role: Desired career goal
            timeframe: Time available for learning
        
        Returns:
            Structured learning plan
        """
        prompt = f"""Create a detailed {timeframe} learning plan for someone transitioning from:
Current: {current_role}
Target: {target_role}

Include:
1. Skills gap analysis
2. Monthly learning milestones
3. Specific resources (courses, books, projects)
4. Practice exercises and projects
5. Community/networking recommendations

Make it actionable and realistic for the given timeframe."""
        
        return self.get_career_advice(prompt, max_tokens=2000)
    
    def analyze_resume(self, resume_text: str, target_role: str) -> str:
        """
        Analyze resume and provide feedback
        
        Args:
            resume_text: Text content of resume
            target_role: Target job role
        
        Returns:
            Resume analysis and improvement suggestions
        """
        prompt = f"""Analyze this resume for a {target_role} position:

{resume_text}

Provide:
1. Strengths
2. Areas for improvement
3. Missing keywords/skills
4. Formatting suggestions
5. Specific action items to improve the resume

Be constructive and specific."""
        
        return self.get_career_advice(prompt, max_tokens=1500)
    
    def get_salary_negotiation_advice(
        self,
        career: str,
        offered_salary: str,
        experience_years: int,
        location: str = "US"
    ) -> str:
        """
        Get salary negotiation advice
        
        Args:
            career: Job role
            offered_salary: Salary offer received
            experience_years: Years of experience
            location: Geographic location
        
        Returns:
            Negotiation strategy and advice
        """
        prompt = f"""I received a {career} job offer:
- Offered Salary: {offered_salary}
- My Experience: {experience_years} years
- Location: {location}

Provide:
1. Market rate analysis
2. Is this offer competitive?
3. Negotiation strategies
4. What to ask for besides salary
5. How to frame the negotiation conversation

Be specific and practical."""
        
        return self.get_career_advice(prompt, max_tokens=1500)
    
    def change_model(self, model: str):
        """Change the AI model being used"""
        self.model = model
    
    def get_available_models(self) -> List[str]:
        """Get list of popular models available on OpenRouter"""
        return [
            "anthropic/claude-3.5-sonnet",
            "anthropic/claude-3-opus",
            "openai/gpt-4-turbo",
            "openai/gpt-4o",
            "google/gemini-pro-1.5",
            "meta-llama/llama-3.1-70b-instruct",
            "meta-llama/llama-3.1-405b-instruct",
            "mistralai/mixtral-8x7b-instruct",
            "anthropic/claude-3-haiku"
        ]

# Utility function for streaming responses (advanced)
class StreamingOpenRouterAgent(OpenRouterAgent):
    """Extended agent with streaming support"""
    
    def stream_career_advice(self, user_query: str, context: Optional[List[Dict]] = None):
        """
        Stream career advice (for real-time responses)
        
        Yields response chunks as they arrive
        """
        messages = [
            {"role": "system", "content": self.system_prompt}
        ]
        
        if context:
            context_str = "User's Career Recommendations:\n"
            for i, rec in enumerate(context[:3], 1):
                context_str += f"{i}. {rec['career']} (Confidence: {rec['confidence']:.1f}%)\n"
            messages.append({
                "role": "system",
                "content": f"Context: {context_str}"
            })
        
        messages.append({"role": "user", "content": user_query})
        
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": True
        }
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                stream=True,
                timeout=60
            )
            
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        data = line[6:]
                        if data != '[DONE]':
                            try:
                                chunk = json.loads(data)
                                if 'choices' in chunk and len(chunk['choices']) > 0:
                                    delta = chunk['choices'][0].get('delta', {})
                                    if 'content' in delta:
                                        yield delta['content']
                            except json.JSONDecodeError:
                                continue
        
        except Exception as e:
            yield f"Error: {str(e)}"
