"""
Books Recommender - Career-specific book recommendations
Curated books from training datasets for each career path
"""

from typing import List, Dict

# Books database organized by career
BOOKS_DATABASE = {
    "Data Science": [
        {
            "title": "Python for Data Analysis",
            "author": "Wes McKinney",
            "level": "Beginner to Intermediate",
            "rating": 4.5,
            "description": "Comprehensive guide to data manipulation with pandas, NumPy, and IPython. Perfect for getting started with Python data science tools."
        },
        {
            "title": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
            "author": "Aurélien Géron",
            "level": "Intermediate",
            "rating": 4.7,
            "description": "Practical approach to machine learning with concrete examples, intuitive explanations, and production-ready Python code."
        },
        {
            "title": "The Data Science Handbook",
            "author": "Field Cady",
            "level": "All Levels",
            "rating": 4.3,
            "description": "Comprehensive overview of data science field, covering statistics, machine learning, and practical career advice."
        },
        {
            "title": "Storytelling with Data",
            "author": "Cole Nussbaumer Knaflic",
            "level": "All Levels",
            "rating": 4.6,
            "description": "Master the art of data visualization and communicating insights effectively to stakeholders."
        },
        {
            "title": "Data Science for Business",
            "author": "Foster Provost & Tom Fawcett",
            "level": "Intermediate",
            "rating": 4.4,
            "description": "Learn fundamental data science principles and their business applications."
        },
        {
            "title": "Deep Learning",
            "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville",
            "level": "Advanced",
            "rating": 4.6,
            "description": "Comprehensive textbook on deep learning, covering mathematical foundations and practical applications."
        }
    ],
    "Machine Learning": [
        {
            "title": "Pattern Recognition and Machine Learning",
            "author": "Christopher Bishop",
            "level": "Advanced",
            "rating": 4.6,
            "description": "In-depth coverage of machine learning algorithms with strong mathematical foundations."
        },
        {
            "title": "Machine Learning Yearning",
            "author": "Andrew Ng",
            "level": "Intermediate",
            "rating": 4.5,
            "description": "Practical advice on structuring machine learning projects and making technical decisions."
        },
        {
            "title": "The Hundred-Page Machine Learning Book",
            "author": "Andriy Burkov",
            "level": "Beginner to Intermediate",
            "rating": 4.4,
            "description": "Concise introduction covering all main concepts in supervised and unsupervised learning."
        },
        {
            "title": "Designing Machine Learning Systems",
            "author": "Chip Huyen",
            "level": "Intermediate to Advanced",
            "rating": 4.7,
            "description": "Comprehensive guide to building ML systems that are reliable, scalable, and maintainable."
        },
        {
            "title": "Machine Learning Engineering",
            "author": "Andriy Burkov",
            "level": "Intermediate",
            "rating": 4.5,
            "description": "Best practices for taking ML models from research to production."
        }
    ],
    "Software Engineering": [
        {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "level": "All Levels",
            "rating": 4.7,
            "description": "Essential guide to writing readable, maintainable, and high-quality code."
        },
        {
            "title": "Design Patterns: Elements of Reusable Object-Oriented Software",
            "author": "Gang of Four",
            "level": "Intermediate",
            "rating": 4.6,
            "description": "Classic book on software design patterns essential for any software engineer."
        },
        {
            "title": "The Pragmatic Programmer",
            "author": "Andrew Hunt & David Thomas",
            "level": "All Levels",
            "rating": 4.8,
            "description": "Timeless advice on software craftsmanship, from code organization to career development."
        },
        {
            "title": "Cracking the Coding Interview",
            "author": "Gayle Laakmann McDowell",
            "level": "All Levels",
            "rating": 4.6,
            "description": "Essential preparation guide for technical interviews with 189 programming problems and solutions."
        },
        {
            "title": "Code Complete",
            "author": "Steve McConnell",
            "level": "Intermediate",
            "rating": 4.5,
            "description": "Comprehensive guide to software construction covering all aspects of software development."
        },
        {
            "title": "Refactoring: Improving the Design of Existing Code",
            "author": "Martin Fowler",
            "level": "Intermediate",
            "rating": 4.6,
            "description": "Master the art of improving code structure without changing its behavior."
        }
    ],
    "Web Development": [
        {
            "title": "Eloquent JavaScript",
            "author": "Marijn Haverbeke",
            "level": "Beginner to Intermediate",
            "rating": 4.5,
            "description": "Modern introduction to programming and JavaScript fundamentals."
        },
        {
            "title": "You Don't Know JS",
            "author": "Kyle Simpson",
            "level": "Intermediate",
            "rating": 4.7,
            "description": "Deep dive series into JavaScript core mechanisms and language features."
        },
        {
            "title": "Learning Web Design",
            "author": "Jennifer Robbins",
            "level": "Beginner",
            "rating": 4.4,
            "description": "Beginner-friendly guide to HTML, CSS, and web design fundamentals."
        },
        {
            "title": "CSS: The Definitive Guide",
            "author": "Eric Meyer",
            "level": "Intermediate to Advanced",
            "rating": 4.5,
            "description": "Comprehensive reference for CSS covering layout, animations, and modern techniques."
        },
        {
            "title": "Full Stack React",
            "author": "Anthony Accomazzo et al.",
            "level": "Intermediate",
            "rating": 4.4,
            "description": "Complete guide to building production-ready React applications."
        }
    ],
    "DevOps": [
        {
            "title": "The Phoenix Project",
            "author": "Gene Kim, Kevin Behr, George Spafford",
            "level": "All Levels",
            "rating": 4.6,
            "description": "Novel about IT transformation, DevOps, and helping business win through technology."
        },
        {
            "title": "The DevOps Handbook",
            "author": "Gene Kim et al.",
            "level": "Intermediate",
            "rating": 4.6,
            "description": "Practical guide to creating world-class agility, reliability, and security in technology organizations."
        },
        {
            "title": "Site Reliability Engineering",
            "author": "Google",
            "level": "Intermediate to Advanced",
            "rating": 4.5,
            "description": "Google's approach to building and running large-scale, reliable systems."
        },
        {
            "title": "Continuous Delivery",
            "author": "Jez Humble & David Farley",
            "level": "Intermediate",
            "rating": 4.6,
            "description": "Reliable software releases through build, test, and deployment automation."
        },
        {
            "title": "Docker Deep Dive",
            "author": "Nigel Poulton",
            "level": "Beginner to Intermediate",
            "rating": 4.5,
            "description": "Comprehensive guide to Docker containerization technology."
        },
        {
            "title": "Kubernetes Up & Running",
            "author": "Kelsey Hightower et al.",
            "level": "Intermediate",
            "rating": 4.6,
            "description": "Practical guide to deploying and managing applications on Kubernetes."
        }
    ],
    "Cybersecurity": [
        {
            "title": "The Web Application Hacker's Handbook",
            "author": "Dafydd Stuttard & Marcus Pinto",
            "level": "Intermediate to Advanced",
            "rating": 4.6,
            "description": "Comprehensive guide to discovering and exploiting security flaws in web applications."
        },
        {
            "title": "Hacking: The Art of Exploitation",
            "author": "Jon Erickson",
            "level": "Intermediate",
            "rating": 4.5,
            "description": "Learn exploitation from the ground up with C programming, networking, and assembly."
        },
        {
            "title": "The Hacker Playbook 3",
            "author": "Peter Kim",
            "level": "Intermediate",
            "rating": 4.4,
            "description": "Practical guide to penetration testing with real-world scenarios."
        },
        {
            "title": "Security Engineering",
            "author": "Ross Anderson",
            "level": "Advanced",
            "rating": 4.6,
            "description": "Comprehensive guide to building secure systems covering all aspects of security."
        },
        {
            "title": "Practical Malware Analysis",
            "author": "Michael Sikorski & Andrew Honig",
            "level": "Advanced",
            "rating": 4.5,
            "description": "Hands-on guide to dissecting malicious software."
        }
    ],
    "Cloud Computing": [
        {
            "title": "AWS Certified Solutions Architect Study Guide",
            "author": "Ben Piper & David Clinton",
            "level": "Intermediate",
            "rating": 4.5,
            "description": "Comprehensive preparation guide for AWS Solutions Architect certification."
        },
        {
            "title": "Google Cloud Platform in Action",
            "author": "JJ Geewax",
            "level": "Beginner to Intermediate",
            "rating": 4.3,
            "description": "Hands-on guide to building applications on Google Cloud Platform."
        },
        {
            "title": "Cloud Native Patterns",
            "author": "Cornelia Davis",
            "level": "Intermediate",
            "rating": 4.5,
            "description": "Design patterns for building resilient, scalable cloud applications."
        },
        {
            "title": "Terraform: Up & Running",
            "author": "Yevgeniy Brikman",
            "level": "Intermediate",
            "rating": 4.6,
            "description": "Practical guide to infrastructure as code with Terraform."
        },
        {
            "title": "Cloud Native DevOps with Kubernetes",
            "author": "John Arundel & Justin Domingus",
            "level": "Intermediate",
            "rating": 4.4,
            "description": "Build, deploy, and scale modern applications in the cloud."
        }
    ],
    "Mobile Development": [
        {
            "title": "iOS Programming: The Big Nerd Ranch Guide",
            "author": "Christian Keur & Aaron Hillegass",
            "level": "Beginner to Intermediate",
            "rating": 4.5,
            "description": "Comprehensive guide to iOS app development with Swift."
        },
        {
            "title": "Android Programming: The Big Nerd Ranch Guide",
            "author": "Bill Phillips et al.",
            "level": "Beginner to Intermediate",
            "rating": 4.4,
            "description": "Practical introduction to Android development with Kotlin."
        },
        {
            "title": "React Native in Action",
            "author": "Nader Dabit",
            "level": "Intermediate",
            "rating": 4.3,
            "description": "Build cross-platform mobile apps with React Native."
        },
        {
            "title": "Flutter in Action",
            "author": "Eric Windmill",
            "level": "Beginner to Intermediate",
            "rating": 4.4,
            "description": "Comprehensive guide to building beautiful cross-platform apps with Flutter."
        }
    ],
    "AI & Deep Learning": [
        {
            "title": "Deep Learning with Python",
            "author": "François Chollet",
            "level": "Intermediate",
            "rating": 4.7,
            "description": "Practical guide to deep learning using Python and Keras by the creator of Keras."
        },
        {
            "title": "Neural Networks and Deep Learning",
            "author": "Michael Nielsen",
            "level": "Intermediate",
            "rating": 4.6,
            "description": "Free online book providing intuitive explanations of neural networks."
        },
        {
            "title": "Artificial Intelligence: A Modern Approach",
            "author": "Stuart Russell & Peter Norvig",
            "level": "Advanced",
            "rating": 4.5,
            "description": "Comprehensive textbook covering all aspects of AI."
        },
        {
            "title": "Generative Deep Learning",
            "author": "David Foster",
            "level": "Advanced",
            "rating": 4.5,
            "description": "Teaching machines to paint, write, compose, and play."
        },
        {
            "title": "Natural Language Processing with Transformers",
            "author": "Lewis Tunstall et al.",
            "level": "Intermediate to Advanced",
            "rating": 4.6,
            "description": "Building language applications with Hugging Face."
        }
    ],
    "Game Development": [
        {
            "title": "Game Programming Patterns",
            "author": "Robert Nystrom",
            "level": "Intermediate",
            "rating": 4.6,
            "description": "Essential design patterns for game development."
        },
        {
            "title": "Unity in Action",
            "author": "Joseph Hocking",
            "level": "Beginner to Intermediate",
            "rating": 4.4,
            "description": "Multiplatform game development with Unity."
        },
        {
            "title": "Unreal Engine 4 Game Development",
            "author": "various",
            "level": "Intermediate",
            "rating": 4.3,
            "description": "Comprehensive guide to Unreal Engine 4 development."
        }
    ],
    "Product Management": [
        {
            "title": "Inspired: How to Create Tech Products Customers Love",
            "author": "Marty Cagan",
            "level": "All Levels",
            "rating": 4.6,
            "description": "Essential guide to modern product management."
        },
        {
            "title": "Cracking the PM Interview",
            "author": "Gayle Laakmann McDowell & Jackie Bavaro",
            "level": "All Levels",
            "rating": 4.5,
            "description": "How to land a product manager job in technology."
        },
        {
            "title": "The Lean Product Playbook",
            "author": "Dan Olsen",
            "level": "Intermediate",
            "rating": 4.4,
            "description": "How to innovate with minimum viable products."
        }
    ],
    "System Design": [
        {
            "title": "Designing Data-Intensive Applications",
            "author": "Martin Kleppmann",
            "level": "Advanced",
            "rating": 4.8,
            "description": "Big ideas behind reliable, scalable, and maintainable systems."
        },
        {
            "title": "System Design Interview",
            "author": "Alex Xu",
            "level": "Intermediate to Advanced",
            "rating": 4.7,
            "description": "Insider's guide to system design interviews."
        },
        {
            "title": "Building Microservices",
            "author": "Sam Newman",
            "level": "Intermediate",
            "rating": 4.5,
            "description": "Designing fine-grained systems."
        }
    ]
}

def recommend_books(career: str, count: int = 6) -> List[Dict]:
    """
    Get book recommendations for a specific career
    
    Args:
        career: Career name or field
        count: Number of books to return
    
    Returns:
        List of book dictionaries with details
    """
    # Direct match
    if career in BOOKS_DATABASE:
        return BOOKS_DATABASE[career][:count]
    
    # Partial match
    for key in BOOKS_DATABASE.keys():
        if career.lower() in key.lower() or key.lower() in career.lower():
            return BOOKS_DATABASE[key][:count]
    
    # Try related fields
    related_mappings = {
        "data scientist": "Data Science",
        "ml engineer": "Machine Learning",
        "software developer": "Software Engineering",
        "frontend": "Web Development",
        "backend": "Software Engineering",
        "security": "Cybersecurity",
        "cloud": "Cloud Computing",
        "ios": "Mobile Development",
        "android": "Mobile Development"
    }
    
    career_lower = career.lower()
    for key, value in related_mappings.items():
        if key in career_lower:
            return BOOKS_DATABASE[value][:count]
    
    # Default recommendations (general software engineering)
    return BOOKS_DATABASE["Software Engineering"][:count]

def get_all_book_categories() -> List[str]:
    """Get list of all career categories with book recommendations"""
    return list(BOOKS_DATABASE.keys())

def search_books(query: str) -> List[Dict]:
    """
    Search for books across all categories
    
    Args:
        query: Search query
    
    Returns:
        List of matching books
    """
    results = []
    query_lower = query.lower()
    
    for career, books in BOOKS_DATABASE.items():
        for book in books:
            if (query_lower in book['title'].lower() or 
                query_lower in book['author'].lower() or 
                query_lower in book['description'].lower()):
                results.append({**book, 'category': career})
    
    return results
