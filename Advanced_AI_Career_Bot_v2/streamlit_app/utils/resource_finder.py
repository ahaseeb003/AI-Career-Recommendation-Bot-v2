"""
Resource Finder - Learning Resources and Salary Information
Provides curated learning resources and salary data
"""

from typing import Dict, List

# Learning resources database
LEARNING_RESOURCES = {
    "Data Scientist": {
        "courses": [
            "IBM Data Science Professional Certificate (Coursera)",
            "Applied Data Science with Python (Coursera)",
            "Data Science Specialization (Johns Hopkins - Coursera)",
            "Machine Learning by Andrew Ng (Coursera)",
            "Python for Data Science and Machine Learning (Udemy)"
        ],
        "certifications": [
            "Microsoft Certified: Azure Data Scientist Associate",
            "Google Professional Data Engineer",
            "IBM Data Science Professional Certificate",
            "AWS Certified Machine Learning - Specialty"
        ],
        "practice": [
            "Kaggle Competitions",
            "DataCamp Projects",
            "HackerRank Data Science",
            "Analytics Vidhya",
            "Google Dataset Search"
        ],
        "projects": [
            "Predictive analytics dashboard",
            "Recommendation system",
            "Image classification model",
            "Time series forecasting",
            "NLP sentiment analysis"
        ]
    },
    "Software Engineer": {
        "courses": [
            "CS50 Introduction to Computer Science (Harvard - edX)",
            "Algorithms Specialization (Stanford - Coursera)",
            "Full Stack Web Development (freeCodeCamp)",
            "System Design Interview Course (Educative)",
            "The Complete Web Developer (Udemy)"
        ],
        "certifications": [
            "AWS Certified Developer",
            "Oracle Certified Professional, Java SE",
            "Microsoft Certified: Azure Developer Associate",
            "Google Associate Cloud Engineer"
        ],
        "practice": [
            "LeetCode",
            "HackerRank",
            "CodeSignal",
            "Project Euler",
            "Codewars"
        ],
        "projects": [
            "E-commerce platform",
            "Social media application",
            "Task management system",
            "Real-time chat application",
            "Portfolio website"
        ]
    },
    "DevOps Engineer": {
        "courses": [
            "DevOps Culture and Mindset (UC Berkeley - Coursera)",
            "Docker and Kubernetes: The Complete Guide (Udemy)",
            "AWS Certified DevOps Engineer (A Cloud Guru)",
            "CI/CD Pipelines with Jenkins (Udemy)",
            "Infrastructure as Code (Terraform and Ansible)"
        ],
        "certifications": [
            "AWS Certified DevOps Engineer - Professional",
            "Certified Kubernetes Administrator (CKA)",
            "Docker Certified Associate",
            "HashiCorp Certified: Terraform Associate",
            "Google Professional Cloud DevOps Engineer"
        ],
        "practice": [
            "KodeKloud",
            "A Cloud Guru Labs",
            "GitHub Actions playground",
            "Docker Hub",
            "Kubernetes Playground"
        ],
        "projects": [
            "CI/CD pipeline setup",
            "Kubernetes cluster deployment",
            "Infrastructure automation with Terraform",
            "Monitoring system with Prometheus/Grafana",
            "Container orchestration project"
        ]
    },
    "Frontend Developer": {
        "courses": [
            "Modern React with Redux (Udemy)",
            "Complete Web Developer Bootcamp (Udemy)",
            "Advanced CSS and Sass (Udemy)",
            "JavaScript Algorithms and Data Structures (freeCodeCamp)",
            "Vue - The Complete Guide (Udemy)"
        ],
        "certifications": [
            "Meta Front-End Developer Professional Certificate",
            "AWS Certified Cloud Practitioner",
            "Responsive Web Design Certification (freeCodeCamp)",
            "JavaScript Algorithms and Data Structures (freeCodeCamp)"
        ],
        "practice": [
            "Frontend Mentor",
            "CodePen",
            "CSS Battle",
            "JavaScript30",
            "100 Days CSS Challenge"
        ],
        "projects": [
            "Responsive portfolio website",
            "E-commerce storefront",
            "Interactive dashboard",
            "Progressive web app",
            "Component library"
        ]
    },
    "Backend Developer": {
        "courses": [
            "Node.js - The Complete Guide (Udemy)",
            "Django for Beginners (Real Python)",
            "Spring Boot Microservices (Udemy)",
            "REST API Design, Development & Management (Udemy)",
            "Database Design and SQL (Udemy)"
        ],
        "certifications": [
            "AWS Certified Solutions Architect",
            "Oracle Database SQL Certified Associate",
            "MongoDB Certified Developer",
            "Red Hat Certified Engineer (RHCE)"
        ],
        "practice": [
            "HackerRank",
            "SQLZoo",
            "Exercism",
            "Codewars",
            "Backend Challenges"
        ],
        "projects": [
            "RESTful API service",
            "Authentication system",
            "Microservices architecture",
            "Database-driven application",
            "GraphQL API"
        ]
    },
    "Machine Learning Engineer": {
        "courses": [
            "Machine Learning Specialization (Andrew Ng - Coursera)",
            "Deep Learning Specialization (deeplearning.ai)",
            "Natural Language Processing Specialization (Coursera)",
            "TensorFlow Developer Certificate (Coursera)",
            "PyTorch for Deep Learning (Udemy)"
        ],
        "certifications": [
            "TensorFlow Developer Certificate",
            "AWS Certified Machine Learning - Specialty",
            "Google Professional Machine Learning Engineer",
            "IBM AI Engineering Professional Certificate"
        ],
        "practice": [
            "Kaggle",
            "Papers with Code",
            "MLOps Community",
            "Weights & Biases",
            "Hugging Face"
        ],
        "projects": [
            "Image classification system",
            "Natural language processing model",
            "Recommendation engine",
            "Computer vision application",
            "Time series prediction"
        ]
    },
    "Cybersecurity Engineer": {
        "courses": [
            "CompTIA Security+ Certification (Udemy)",
            "Ethical Hacking Bootcamp (Udemy)",
            "Network Security Fundamentals (Coursera)",
            "Penetration Testing (Offensive Security)",
            "Cloud Security Fundamentals (Pluralsight)"
        ],
        "certifications": [
            "CompTIA Security+",
            "Certified Ethical Hacker (CEH)",
            "CISSP - Certified Information Systems Security Professional",
            "OSCP - Offensive Security Certified Professional",
            "GIAC Security Essentials (GSEC)"
        ],
        "practice": [
            "HackTheBox",
            "TryHackMe",
            "OverTheWire",
            "PentesterLab",
            "OWASP WebGoat"
        ],
        "projects": [
            "Vulnerability assessment tool",
            "Security monitoring system",
            "Penetration testing lab",
            "Secure authentication system",
            "Network security analyzer"
        ]
    },
    "Cloud Engineer": {
        "courses": [
            "AWS Certified Solutions Architect (A Cloud Guru)",
            "Microsoft Azure Fundamentals (Coursera)",
            "Google Cloud Platform Fundamentals (Coursera)",
            "Cloud Architecture with Google Cloud (Coursera)",
            "AWS Lambda and Serverless Framework (Udemy)"
        ],
        "certifications": [
            "AWS Certified Solutions Architect - Associate",
            "Microsoft Certified: Azure Administrator",
            "Google Cloud Professional Cloud Architect",
            "AWS Certified DevOps Engineer",
            "CompTIA Cloud+"
        ],
        "practice": [
            "AWS Free Tier",
            "Azure Free Account",
            "Google Cloud Free Tier",
            "CloudAcademy",
            "Qwiklabs"
        ],
        "projects": [
            "Multi-tier cloud application",
            "Serverless architecture",
            "Cloud migration project",
            "Auto-scaling infrastructure",
            "Cloud-native application"
        ]
    }
}

# Salary information (in USD, approximate ranges for US market)
SALARY_INFO = {
    "Data Scientist": {
        "entry": "$75,000 - $95,000",
        "mid": "$95,000 - $130,000",
        "senior": "$130,000 - $180,000+",
        "growth": "23% (Much faster than average)"
    },
    "Software Engineer": {
        "entry": "$70,000 - $95,000",
        "mid": "$95,000 - $140,000",
        "senior": "$140,000 - $200,000+",
        "growth": "22% (Much faster than average)"
    },
    "DevOps Engineer": {
        "entry": "$75,000 - $100,000",
        "mid": "$100,000 - $140,000",
        "senior": "$140,000 - $180,000+",
        "growth": "21% (Much faster than average)"
    },
    "Frontend Developer": {
        "entry": "$60,000 - $85,000",
        "mid": "$85,000 - $120,000",
        "senior": "$120,000 - $160,000+",
        "growth": "16% (Much faster than average)"
    },
    "Backend Developer": {
        "entry": "$70,000 - $95,000",
        "mid": "$95,000 - $135,000",
        "senior": "$135,000 - $180,000+",
        "growth": "22% (Much faster than average)"
    },
    "Machine Learning Engineer": {
        "entry": "$85,000 - $110,000",
        "mid": "$110,000 - $150,000",
        "senior": "$150,000 - $200,000+",
        "growth": "22% (Much faster than average)"
    },
    "Cybersecurity Engineer": {
        "entry": "$75,000 - $100,000",
        "mid": "$100,000 - $140,000",
        "senior": "$140,000 - $180,000+",
        "growth": "33% (Much faster than average)"
    },
    "Cloud Engineer": {
        "entry": "$80,000 - $105,000",
        "mid": "$105,000 - $145,000",
        "senior": "$145,000 - $190,000+",
        "growth": "22% (Much faster than average)"
    },
    "Full Stack Developer": {
        "entry": "$70,000 - $95,000",
        "mid": "$95,000 - $135,000",
        "senior": "$135,000 - $175,000+",
        "growth": "20% (Much faster than average)"
    },
    "Mobile Developer": {
        "entry": "$65,000 - $90,000",
        "mid": "$90,000 - $125,000",
        "senior": "$125,000 - $165,000+",
        "growth": "18% (Much faster than average)"
    }
}

def get_learning_resources(career: str) -> Dict[str, List[str]]:
    """
    Get learning resources for a specific career
    
    Args:
        career: Career name
    
    Returns:
        Dictionary with courses, certifications, practice platforms, and projects
    """
    # Direct match
    if career in LEARNING_RESOURCES:
        return LEARNING_RESOURCES[career]
    
    # Partial match
    for key in LEARNING_RESOURCES.keys():
        if career.lower() in key.lower() or key.lower() in career.lower():
            return LEARNING_RESOURCES[key]
    
    # Default resources
    return {
        "courses": [
            "Industry-specific courses on Coursera",
            "Udemy professional courses",
            "LinkedIn Learning career paths",
            "Pluralsight skill paths",
            "edX professional certificates"
        ],
        "certifications": [
            "Industry-recognized professional certifications",
            "Cloud provider certifications (AWS, Azure, GCP)",
            "Vendor-specific certifications"
        ],
        "practice": [
            "HackerRank",
            "LeetCode",
            "GitHub projects",
            "Open source contributions"
        ],
        "projects": [
            "Portfolio projects",
            "Open source contributions",
            "Personal projects",
            "Freelance work"
        ]
    }

def get_salary_info(career: str) -> Dict[str, str]:
    """
    Get salary information for a specific career
    
    Args:
        career: Career name
    
    Returns:
        Dictionary with salary ranges for different experience levels
    """
    # Direct match
    if career in SALARY_INFO:
        return SALARY_INFO[career]
    
    # Partial match
    for key in SALARY_INFO.keys():
        if career.lower() in key.lower() or key.lower() in career.lower():
            return SALARY_INFO[key]
    
    # Default salary info
    return {
        "entry": "$60,000 - $85,000",
        "mid": "$85,000 - $120,000",
        "senior": "$120,000 - $170,000+",
        "growth": "15-25% (Faster than average)"
    }

def get_all_career_resources() -> List[str]:
    """Get list of all careers with resources"""
    return list(LEARNING_RESOURCES.keys())
