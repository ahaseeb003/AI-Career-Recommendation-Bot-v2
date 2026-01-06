"""
Model Loader for Career Recommendation System
Handles loading and inference of the trained model
"""

import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle
import json
from pathlib import Path
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

# Model paths
MODEL_DIR = Path(__file__).parent.parent / "models"
MODEL_PATH = MODEL_DIR / "career_model_cpu.pth"
ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"
EMBEDDINGS_PATH = MODEL_DIR / "career_embeddings.npy"
METADATA_PATH = MODEL_DIR / "model_metadata.json"

class CareerClassifier(nn.Module):
    """Career classification model"""
    def __init__(self, base_model_name, num_classes, hidden_dim=256, dropout=0.3):
        super(CareerClassifier, self).__init__()
        self.base_model = AutoModel.from_pretrained(base_model_name)
        self.dropout = nn.Dropout(dropout)
        self.classifier = nn.Sequential(
            nn.Linear(self.base_model.config.hidden_size, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, num_classes)
        )
    
    def forward(self, input_ids, attention_mask):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.last_hidden_state[:, 0, :]
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)
        return logits

# Global variables for model components
_model = None
_tokenizer = None
_label_encoder = None
_career_embeddings = None
_sentence_model = None
_metadata = None

def load_model():
    """Load all model components"""
    global _model, _tokenizer, _label_encoder, _career_embeddings, _sentence_model, _metadata
    
    try:
        # Load metadata
        with open(METADATA_PATH, 'r') as f:
            _metadata = json.load(f)
        
        config = _metadata['model_config']
        
        # Load label encoder
        with open(ENCODER_PATH, 'rb') as f:
            _label_encoder = pickle.load(f)
        
        # Load embeddings
        _career_embeddings = np.load(EMBEDDINGS_PATH)
        
        # Initialize tokenizer
        _tokenizer = AutoTokenizer.from_pretrained(config['base_model'])
        
        # Initialize sentence model for similarity search
        _sentence_model = SentenceTransformer(config['base_model'])
        
        # Load model
        checkpoint = torch.load(MODEL_PATH, map_location=torch.device('cpu'))
        
        _model = CareerClassifier(
            base_model_name=config['base_model'],
            num_classes=_metadata['num_classes'],
            hidden_dim=config['hidden_dim'],
            dropout=config['dropout']
        )
        
        _model.load_state_dict(checkpoint['model_state_dict'])
        _model.eval()
        
        return True
    
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return False

def get_career_recommendations(query, top_k=5, use_hybrid=True):
    """
    Get career recommendations for a given query
    
    Args:
        query: User's career description/query
        top_k: Number of recommendations to return
        use_hybrid: Use both model prediction and embedding similarity
    
    Returns:
        List of career recommendations with confidence scores
    """
    global _model, _tokenizer, _label_encoder, _career_embeddings, _sentence_model
    
    if _model is None:
        raise ValueError("Model not loaded. Call load_model() first.")
    
    results = []
    
    # Method 1: Model-based prediction
    encoding = _tokenizer(
        query,
        add_special_tokens=True,
        max_length=128,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )
    
    with torch.no_grad():
        outputs = _model(encoding['input_ids'], encoding['attention_mask'])
        probabilities = torch.nn.functional.softmax(outputs, dim=1)[0]
        
        # Get top predictions
        top_probs, top_indices = torch.topk(probabilities, k=min(top_k * 2, len(_label_encoder.classes_)))
        
        for prob, idx in zip(top_probs, top_indices):
            career = _label_encoder.inverse_transform([idx.item()])[0]
            results.append({
                'career': career,
                'confidence': prob.item() * 100,
                'method': 'model'
            })
    
    # Method 2: Embedding-based similarity (if hybrid mode)
    if use_hybrid and _sentence_model is not None:
        query_embedding = _sentence_model.encode([query])[0]
        
        # Calculate similarities
        similarities = cosine_similarity(
            query_embedding.reshape(1, -1),
            _career_embeddings
        )[0]
        
        # Get top similar careers
        top_similar_indices = np.argsort(similarities)[-top_k*2:][::-1]
        
        for idx in top_similar_indices:
            career = _label_encoder.classes_[idx]
            similarity_score = similarities[idx] * 100
            
            # Check if already in results
            existing = next((r for r in results if r['career'] == career), None)
            if existing:
                # Combine scores (weighted average)
                existing['confidence'] = (existing['confidence'] * 0.6 + similarity_score * 0.4)
                existing['method'] = 'hybrid'
            else:
                results.append({
                    'career': career,
                    'confidence': similarity_score,
                    'method': 'similarity'
                })
    
    # Sort by confidence and return top_k
    results.sort(key=lambda x: x['confidence'], reverse=True)
    return results[:top_k]

def get_model_info():
    """Get model metadata and information"""
    global _metadata
    
    if _metadata is None:
        try:
            with open(METADATA_PATH, 'r') as f:
                _metadata = json.load(f)
        except:
            return None
    
    return _metadata

def predict_career(user_input, threshold=0.5):
    """
    Simple prediction function for single career prediction
    
    Args:
        user_input: User's career description
        threshold: Minimum confidence threshold
    
    Returns:
        Predicted career and confidence, or None if below threshold
    """
    recommendations = get_career_recommendations(user_input, top_k=1)
    
    if recommendations and recommendations[0]['confidence'] >= threshold * 100:
        return recommendations[0]
    
    return None

def get_all_careers():
    """Get list of all available careers in the model"""
    global _label_encoder
    
    if _label_encoder is None:
        load_model()
    
    return sorted(_label_encoder.classes_.tolist()) if _label_encoder else []

# Cache the model loading
@st.cache_resource
def get_cached_model():
    """Cache model loading to avoid reloading on every interaction"""
    load_model()
    return True
