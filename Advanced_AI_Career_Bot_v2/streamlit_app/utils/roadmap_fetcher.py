"""
Roadmap.sh Integration
Fetches career roadmaps and learning paths from roadmap.sh
"""

import requests
from typing import Dict, List, Optional
import json

# Roadmap mapping
ROADMAP_MAPPING = {
    "Frontend Developer": "frontend",
    "Backend Developer": "backend",
    "Full Stack Developer": "full-stack",
    "DevOps Engineer": "devops",
    "Data Scientist": "ai-data-scientist",
    "Machine Learning Engineer": "mlops",
    "Cybersecurity Engineer": "cyber-security",
    "Mobile Developer": "android",
    "Cloud Engineer": "devops",
    "AI Engineer": "ai-engineer",
    "Game Developer": "game-developer",
    "Blockchain Developer": "blockchain"
}

# Roadmap.sh content (curated from roadmap.sh)
ROADMAP_CONTENT = {
    "Frontend Developer": {
        "title": "Frontend Developer Roadmap",
        "description": "Step by step guide to becoming a modern frontend developer",
        "url": "https://roadmap.sh/frontend",
        "sections": [
            {
                "title": "Internet & Web Fundamentals",
                "description": "Understand how the internet works, HTTP, browsers, DNS, domain names, and hosting.",
                "topics": [
                    "How does the internet work?",
                    "What is HTTP?",
                    "Browsers and how they work",
                    "DNS and how it works",
                    "Domain names",
                    "Hosting"
                ],
                "resources": [
                    {"title": "How the Internet Works", "url": "https://roadmap.sh/guides/what-is-internet"},
                    {"title": "HTTP Overview", "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview"}
                ]
            },
            {
                "title": "HTML - Structure",
                "description": "Learn HTML fundamentals, semantic HTML, forms, accessibility, and SEO basics.",
                "topics": [
                    "Learn the basics of HTML",
                    "Semantic HTML",
                    "Forms and Validations",
                    "Accessibility",
                    "SEO Basics"
                ],
                "resources": [
                    {"title": "HTML Tutorial - MDN", "url": "https://developer.mozilla.org/en-US/docs/Web/HTML"},
                    {"title": "Web Accessibility", "url": "https://www.w3.org/WAI/fundamentals/"}
                ]
            },
            {
                "title": "CSS - Styling",
                "description": "Master CSS fundamentals, layouts, responsive design, and modern CSS features.",
                "topics": [
                    "CSS Basics",
                    "Making Layouts (Flexbox, Grid)",
                    "Responsive Design",
                    "CSS Architecture",
                    "CSS Preprocessors (Sass, PostCSS)",
                    "Modern CSS (CSS3, CSS Variables)"
                ],
                "resources": [
                    {"title": "CSS Tutorial - MDN", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS"},
                    {"title": "Flexbox Guide", "url": "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"}
                ]
            },
            {
                "title": "JavaScript - Functionality",
                "description": "Learn JavaScript fundamentals, DOM manipulation, ES6+, and async programming.",
                "topics": [
                    "JavaScript Basics",
                    "DOM Manipulation",
                    "Fetch API / Ajax",
                    "ES6+ Features",
                    "Asynchronous JavaScript",
                    "Working with APIs"
                ],
                "resources": [
                    {"title": "JavaScript.info", "url": "https://javascript.info/"},
                    {"title": "You Don't Know JS", "url": "https://github.com/getify/You-Dont-Know-JS"}
                ]
            },
            {
                "title": "Version Control - Git",
                "description": "Master Git and GitHub for version control and collaboration.",
                "topics": [
                    "Basic Git commands",
                    "Branching and merging",
                    "GitHub/GitLab",
                    "Pull requests",
                    "Git workflows"
                ]
            },
            {
                "title": "Frontend Frameworks",
                "description": "Learn modern frontend frameworks and libraries.",
                "topics": [
                    "React (most popular)",
                    "Vue.js",
                    "Angular",
                    "Svelte",
                    "Component-based architecture",
                    "State management"
                ]
            },
            {
                "title": "Build Tools",
                "description": "Understand modern build tools and bundlers.",
                "topics": [
                    "npm/yarn/pnpm",
                    "Webpack/Vite/Parcel",
                    "Task runners",
                    "Module bundlers",
                    "Linters and formatters"
                ]
            },
            {
                "title": "Testing",
                "description": "Learn testing strategies and tools.",
                "topics": [
                    "Unit testing",
                    "Integration testing",
                    "E2E testing",
                    "Jest, Vitest",
                    "Testing Library",
                    "Cypress, Playwright"
                ]
            }
        ]
    },
    "Backend Developer": {
        "title": "Backend Developer Roadmap",
        "description": "Step by step guide to becoming a modern backend developer",
        "url": "https://roadmap.sh/backend",
        "sections": [
            {
                "title": "Internet Basics",
                "description": "Understand how the internet, protocols, and APIs work.",
                "topics": [
                    "How does the internet work?",
                    "HTTP/HTTPS protocols",
                    "APIs and REST",
                    "Authentication methods"
                ]
            },
            {
                "title": "Programming Language",
                "description": "Choose and master a backend programming language.",
                "topics": [
                    "Python (Django, Flask, FastAPI)",
                    "JavaScript (Node.js, Express)",
                    "Java (Spring Boot)",
                    "Go",
                    "C# (.NET)",
                    "Ruby (Rails)",
                    "PHP (Laravel)"
                ]
            },
            {
                "title": "Database Management",
                "description": "Learn relational and NoSQL databases.",
                "topics": [
                    "Relational Databases (PostgreSQL, MySQL)",
                    "NoSQL Databases (MongoDB, Redis)",
                    "ORMs",
                    "Database design",
                    "Transactions and ACID",
                    "Indexing and optimization"
                ]
            },
            {
                "title": "API Development",
                "description": "Master API design and development.",
                "topics": [
                    "RESTful APIs",
                    "GraphQL",
                    "Authentication & Authorization",
                    "API documentation (Swagger/OpenAPI)",
                    "Rate limiting",
                    "API versioning"
                ]
            },
            {
                "title": "Caching",
                "description": "Implement caching strategies.",
                "topics": [
                    "Redis",
                    "Memcached",
                    "CDN caching",
                    "Client-side caching"
                ]
            },
            {
                "title": "Security",
                "description": "Learn backend security best practices.",
                "topics": [
                    "HTTPS",
                    "CORS",
                    "Content Security Policy",
                    "OWASP Security Risks",
                    "SQL Injection prevention",
                    "Encryption"
                ]
            },
            {
                "title": "Testing",
                "description": "Implement comprehensive testing.",
                "topics": [
                    "Unit testing",
                    "Integration testing",
                    "Load testing",
                    "Testing frameworks"
                ]
            },
            {
                "title": "Deployment & DevOps",
                "description": "Learn deployment and infrastructure.",
                "topics": [
                    "CI/CD",
                    "Docker",
                    "Cloud platforms (AWS, Azure, GCP)",
                    "Server management",
                    "Monitoring and logging"
                ]
            }
        ]
    },
    "DevOps Engineer": {
        "title": "DevOps Engineer Roadmap",
        "description": "Guide to becoming a DevOps engineer",
        "url": "https://roadmap.sh/devops",
        "sections": [
            {
                "title": "Operating Systems",
                "description": "Master Linux and Unix systems.",
                "topics": [
                    "Linux fundamentals",
                    "Shell scripting",
                    "System administration",
                    "Process management",
                    "Networking basics"
                ]
            },
            {
                "title": "Version Control",
                "description": "Master Git and version control workflows.",
                "topics": [
                    "Git fundamentals",
                    "Branching strategies",
                    "GitFlow",
                    "Monorepos"
                ]
            },
            {
                "title": "CI/CD",
                "description": "Implement continuous integration and deployment.",
                "topics": [
                    "Jenkins",
                    "GitLab CI",
                    "GitHub Actions",
                    "CircleCI",
                    "Pipeline design"
                ]
            },
            {
                "title": "Containers",
                "description": "Learn containerization technologies.",
                "topics": [
                    "Docker",
                    "Docker Compose",
                    "Container orchestration",
                    "Image optimization"
                ]
            },
            {
                "title": "Orchestration",
                "description": "Master container orchestration.",
                "topics": [
                    "Kubernetes",
                    "Helm",
                    "Service mesh",
                    "Istio"
                ]
            },
            {
                "title": "Infrastructure as Code",
                "description": "Automate infrastructure provisioning.",
                "topics": [
                    "Terraform",
                    "Ansible",
                    "CloudFormation",
                    "Pulumi"
                ]
            },
            {
                "title": "Cloud Providers",
                "description": "Learn major cloud platforms.",
                "topics": [
                    "AWS",
                    "Azure",
                    "Google Cloud Platform",
                    "Cloud services",
                    "Cost optimization"
                ]
            },
            {
                "title": "Monitoring & Logging",
                "description": "Implement observability.",
                "topics": [
                    "Prometheus",
                    "Grafana",
                    "ELK Stack",
                    "Datadog",
                    "Application monitoring"
                ]
            }
        ]
    },
    "Data Scientist": {
        "title": "AI & Data Scientist Roadmap",
        "description": "Path to becoming a data scientist",
        "url": "https://roadmap.sh/ai-data-scientist",
        "sections": [
            {
                "title": "Mathematics & Statistics",
                "description": "Build strong mathematical foundation.",
                "topics": [
                    "Linear algebra",
                    "Calculus",
                    "Probability",
                    "Statistics",
                    "Hypothesis testing"
                ]
            },
            {
                "title": "Programming",
                "description": "Master programming for data science.",
                "topics": [
                    "Python",
                    "R",
                    "SQL",
                    "Data structures",
                    "Algorithms"
                ]
            },
            {
                "title": "Data Analysis",
                "description": "Learn data manipulation and analysis.",
                "topics": [
                    "Pandas",
                    "NumPy",
                    "Data cleaning",
                    "Exploratory data analysis",
                    "Feature engineering"
                ]
            },
            {
                "title": "Data Visualization",
                "description": "Master data visualization tools.",
                "topics": [
                    "Matplotlib",
                    "Seaborn",
                    "Plotly",
                    "Tableau",
                    "Power BI"
                ]
            },
            {
                "title": "Machine Learning",
                "description": "Learn ML algorithms and techniques.",
                "topics": [
                    "Supervised learning",
                    "Unsupervised learning",
                    "Scikit-learn",
                    "Model evaluation",
                    "Hyperparameter tuning"
                ]
            },
            {
                "title": "Deep Learning",
                "description": "Master neural networks and deep learning.",
                "topics": [
                    "Neural networks",
                    "TensorFlow/PyTorch",
                    "CNNs",
                    "RNNs",
                    "Transformers"
                ]
            },
            {
                "title": "Big Data",
                "description": "Work with large-scale data.",
                "topics": [
                    "Spark",
                    "Hadoop",
                    "Data warehousing",
                    "ETL pipelines"
                ]
            },
            {
                "title": "Deployment",
                "description": "Deploy ML models to production.",
                "topics": [
                    "MLOps",
                    "Model serving",
                    "API development",
                    "Docker",
                    "Cloud deployment"
                ]
            }
        ]
    }
}

def fetch_career_roadmap(career: str) -> Optional[Dict]:
    """
    Fetch career roadmap from curated content
    
    Args:
        career: Career name (e.g., "Frontend Developer")
    
    Returns:
        Roadmap data dictionary or None
    """
    # Return curated content if available
    if career in ROADMAP_CONTENT:
        return ROADMAP_CONTENT[career]
    
    # Try partial match
    for key in ROADMAP_CONTENT.keys():
        if career.lower() in key.lower() or key.lower() in career.lower():
            return ROADMAP_CONTENT[key]
    
    # Return generic tech roadmap structure
    return {
        "title": f"{career} Roadmap",
        "description": f"Learning path for {career}",
        "url": "https://roadmap.sh",
        "sections": [
            {
                "title": "Fundamentals",
                "description": "Core concepts and foundational knowledge",
                "topics": [
                    "Industry overview",
                    "Required skills",
                    "Common tools",
                    "Best practices"
                ]
            },
            {
                "title": "Technical Skills",
                "description": "Essential technical competencies",
                "topics": [
                    "Programming languages",
                    "Frameworks and libraries",
                    "Development tools",
                    "Version control"
                ]
            },
            {
                "title": "Advanced Topics",
                "description": "Advanced skills and specializations",
                "topics": [
                    "System design",
                    "Architecture patterns",
                    "Performance optimization",
                    "Security best practices"
                ]
            },
            {
                "title": "Professional Development",
                "description": "Career growth and continuous learning",
                "topics": [
                    "Portfolio building",
                    "Open source contribution",
                    "Networking",
                    "Staying updated with trends"
                ]
            }
        ]
    }

def get_roadmap_url(career: str) -> str:
    """Get the roadmap.sh URL for a career"""
    slug = ROADMAP_MAPPING.get(career, "")
    if slug:
        return f"https://roadmap.sh/{slug}"
    return "https://roadmap.sh"

def get_all_roadmaps() -> List[str]:
    """Get list of all available roadmaps"""
    return list(ROADMAP_CONTENT.keys())
