# Training Guide

## Multi-Source Model Training with Google Colab

This guide explains how to train your own career recommendation model using multiple data sources.

## Overview

The training pipeline supports:
- **Multiple data sources**: Career Q&A, skills mapping, job descriptions, books
- **Flexible datasets**: Use any combination of data sources
- **GPU acceleration**: Train in 10-15 minutes on Google Colab
- **CPU-optimized export**: Lightweight model for Streamlit deployment

## Table of Contents

1. [Dataset Preparation](#dataset-preparation)
2. [Training Process](#training-process)
3. [Model Deployment](#model-deployment)
4. [Advanced Configuration](#advanced-configuration)

## Dataset Preparation

### Required CSV Format

#### 1. Career Q&A (`career_qa.csv`)

**Columns**: `role`, `question`, `answer`

```csv
role,question,answer
Data Scientist,"What does a Data Scientist do?","Analyzes data..."
Software Engineer,"What skills are needed?","Programming, algorithms..."
```

**Guidelines:**
- At least 5 questions per career
- Diverse question types (what, how, why)
- Comprehensive answers (50-200 words)

#### 2. Skills Mapping (`skills_mapping.csv`)

**Columns**: `role`, `skills`, `description`

```csv
role,skills,description
Data Scientist,"Python, ML, Statistics","Works with data and models..."
```

**Guidelines:**
- List 5-10 key skills per role
- Comma-separated skills
- Clear role descriptions

#### 3. Job Descriptions (`job_descriptions.csv`)

**Columns**: `role`, `description`, `requirements`

```csv
role,description,requirements
Data Scientist,"Analyze datasets...","Python, SQL, ML experience..."
```

**Guidelines:**
- Real job posting descriptions
- Specific requirements
- Industry-standard terminology

#### 4. Books Recommendations (`books_recommendations.csv`)

**Columns**: `role`, `book_title`, `author`, `description`

```csv
role,book_title,author,description
Data Scientist,"Python for Data Analysis","Wes McKinney","Learn pandas..."
```

**Guidelines:**
- 3-5 books per career
- Include author names
- Brief but informative descriptions

### Dataset Requirements

**Minimum (for functional model):**
- 50 total training samples
- 5 career categories
- At least 1 data source

**Recommended (for good performance):**
- 500+ total training samples
- 15-20 career categories
- 2-3 data sources combined

**Optimal (for best accuracy):**
- 1000+ total training samples
- 25+ career categories
- All 4 data sources

### Data Collection Tips

**Where to Get Data:**

1. **Career Q&A:**
   - Interview question websites
   - Career forums (Reddit, Blind)
   - Company career pages
   - Your own expertise

2. **Skills Mapping:**
   - Job posting websites (LinkedIn, Indeed)
   - Career websites (O*NET)
   - Tech skill surveys
   - Industry reports

3. **Job Descriptions:**
   - Job boards (LinkedIn, Indeed, Glassdoor)
   - Company career pages
   - Scrape with permission
   - Aggregate and anonymize

4. **Books:**
   - Amazon bestsellers
   - Goodreads lists
   - Professional recommendations
   - Online course syllabi

## Training Process

### Step 1: Open Google Colab

1. Go to [Google Colab](https://colab.research.google.com/)
2. Sign in with Google account
3. Click **File** → **Upload notebook**
4. Upload `colab/Multi_Source_Career_Model_Training.ipynb`

### Step 2: Set Up Runtime

1. Click **Runtime** → **Change runtime type**
2. Select **GPU** (T4 recommended)
3. Click **Save**

### Step 3: Upload Datasets

1. Run the first few cells (setup)
2. When prompted, upload your CSV files:
   - `career_qa.csv` (required)
   - `skills_mapping.csv` (optional)
   - `job_descriptions.csv` (optional)
   - `books_recommendations.csv` (optional)

**Note**: If you skip a file, default sample data will be used.

### Step 4: Data Merging

The notebook automatically:
- Loads all datasets
- Merges into unified format
- Removes duplicates
- Validates data quality
- Shows statistics

**Review the output:**
```
✅ Merged dataset created:
  Total samples: 523
  Unique roles: 18
  
  Samples per source:
  qa       245
  skills   128
  jobs     95
  books    55
```

### Step 5: Training Configuration

Default configuration (optimized):
```python
CONFIG = {
    'base_model': 'sentence-transformers/all-MiniLM-L6-v2',
    'max_length': 128,
    'hidden_dim': 256,
    'dropout': 0.3,
    'batch_size': 32,
    'learning_rate': 2e-5,
    'num_epochs': 10,
    'warmup_steps': 100
}
```

**When to modify:**
- Increase `num_epochs` if underfitting (validation accuracy improving)
- Decrease `num_epochs` if overfitting (validation accuracy decreasing)
- Increase `hidden_dim` for more complex patterns (256 → 512)
- Adjust `learning_rate` if training unstable

### Step 6: Run Training

1. Click **Runtime** → **Run all**
2. Or run cells sequentially with Shift+Enter

**Training progress:**
```
Epoch 1/10
Training: 100% | Loss: 1.234 | Acc: 75.2%
Validation: 100% | Loss: 0.987 | Acc: 82.1%

Epoch 2/10
Training: 100% | Loss: 0.876 | Acc: 85.4%
Validation: 100% | Loss: 0.765 | Acc: 88.3%
```

**Expected training time:**
- With GPU (T4): 10-15 minutes
- With CPU: 1-2 hours (not recommended)

### Step 7: Monitor Performance

Watch for:

**Good signs:**
- ✅ Validation accuracy increasing
- ✅ Loss decreasing steadily
- ✅ Train/val accuracy gap < 10%

**Warning signs:**
- ⚠️ Validation accuracy stuck
- ⚠️ Large train/val gap (overfitting)
- ⚠️ Very slow training

**Early stopping:**
- Triggers if no improvement for 3 epochs
- Saves best model automatically

### Step 8: Download Models

After training completes:

1. Navigate to the last cell
2. Click "Download" when prompted
3. Save `trained_models.zip` to your computer

**File size:** ~100-150MB

## Model Deployment

### Step 1: Extract Files

```bash
unzip trained_models.zip
```

**Contents:**
- `career_model_cpu.pth` - CPU-optimized model (~80MB)
- `label_encoder.pkl` - Career label encoder
- `career_embeddings.npy` - Pre-computed embeddings
- `model_metadata.json` - Model configuration

### Step 2: Move to Models Directory

```bash
cp career_model_cpu.pth streamlit_app/models/
cp label_encoder.pkl streamlit_app/models/
cp career_embeddings.npy streamlit_app/models/
cp model_metadata.json streamlit_app/models/
```

Or on Windows:
```cmd
copy career_model_cpu.pth streamlit_app\models\
copy label_encoder.pkl streamlit_app\models\
copy career_embeddings.npy streamlit_app\models\
copy model_metadata.json streamlit_app\models\
```

### Step 3: Verify Deployment

```bash
cd streamlit_app
python -c "from utils.model_loader import load_model; load_model(); print('Model loaded successfully!')"
```

### Step 4: Test in Application

1. Run Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Go to "Career Matching" tab

3. Enter a test query:
   ```
   I love programming and building web applications with Python and JavaScript
   ```

4. Click "Get Career Recommendations"

5. Verify:
   - Recommendations appear within 2-3 seconds
   - Confidence scores make sense
   - Careers match the description

## Advanced Configuration

### Hyperparameter Tuning

#### Learning Rate

```python
'learning_rate': 2e-5  # Default (good for most cases)
'learning_rate': 5e-5  # Faster training, less stable
'learning_rate': 1e-5  # Slower, more stable
```

**When to adjust:**
- Loss exploding → Decrease learning rate
- Training very slow → Increase learning rate

#### Hidden Dimension

```python
'hidden_dim': 256  # Default (balanced)
'hidden_dim': 512  # More capacity, slower
'hidden_dim': 128  # Faster, less capacity
```

**When to adjust:**
- Many careers (30+) → Increase to 512
- Few careers (10-15) → Decrease to 128

#### Dropout

```python
'dropout': 0.3  # Default (moderate regularization)
'dropout': 0.5  # Strong regularization
'dropout': 0.1  # Weak regularization
```

**When to adjust:**
- Overfitting → Increase dropout
- Underfitting → Decrease dropout

#### Batch Size

```python
'batch_size': 32  # Default (good for T4 GPU)
'batch_size': 64  # Faster, needs more memory
'batch_size': 16  # Slower, less memory
```

**GPU memory errors** → Decrease batch size

### Using Different Base Models

The notebook uses `sentence-transformers/all-MiniLM-L6-v2` by default.

**Alternative options:**

```python
# Smaller and faster
'base_model': 'sentence-transformers/all-MiniLM-L12-v2'

# Better quality, larger size
'base_model': 'sentence-transformers/all-mpnet-base-v2'

# Multilingual support
'base_model': 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'
```

**Trade-offs:**
- Smaller models: Faster inference, lower accuracy
- Larger models: Better accuracy, slower inference, more memory

### Data Augmentation

Add variety to training data:

```python
# In notebook, before training
from augmentation import augment_data

# Paraphrase questions
df_augmented = augment_data(df_merged, method='paraphrase', factor=2)

# Add synonyms
df_augmented = augment_data(df_merged, method='synonym', factor=1.5)
```

### Handling Imbalanced Data

If some careers have much more data:

```python
from imblearn.over_sampling import RandomOverSampler

# Balance classes
ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X, y)
```

## Troubleshooting

### Low Validation Accuracy (<80%)

**Possible causes:**
- Insufficient training data
- Poor data quality
- Wrong hyperparameters

**Solutions:**
1. Add more training samples (aim for 500+)
2. Clean and improve data quality
3. Train for more epochs
4. Try different learning rates

### Overfitting (Train/Val Gap >15%)

**Symptoms:**
- Training accuracy: 95%
- Validation accuracy: 75%

**Solutions:**
1. Increase dropout (0.3 → 0.5)
2. Add more training data
3. Use data augmentation
4. Reduce model complexity
5. Early stopping (already implemented)

### Out of Memory Errors

**Solutions:**
1. Decrease batch size (32 → 16)
2. Decrease max_length (128 → 64)
3. Use smaller base model
4. Enable gradient checkpointing

### Very Slow Training

**On GPU:**
- Check GPU is actually being used:
  ```python
  print(torch.cuda.is_available())  # Should be True
  ```
- Verify Runtime type is "GPU"

**On CPU:**
- Training will be slow (~1-2 hours)
- Consider using Google Colab Pro for better GPUs

### Model Not Converging

**Symptoms:**
- Loss not decreasing
- Accuracy stuck at random
- NaN losses

**Solutions:**
1. Lower learning rate (2e-5 → 1e-5)
2. Check data quality
3. Initialize with different random seed
4. Try gradient clipping (already implemented)

## Best Practices

### Data Quality

✅ **Do:**
- Use real-world data
- Ensure diversity in questions/descriptions
- Clean and normalize text
- Remove duplicates
- Verify all fields are filled

❌ **Don't:**
- Use copied/pasted identical descriptions
- Leave empty fields
- Include invalid characters
- Mix languages inconsistently

### Training Strategy

1. **Start small** - Test with 100 samples
2. **Iterate** - Gradually add more data
3. **Monitor** - Watch train/val metrics
4. **Validate** - Test on real queries
5. **Improve** - Refine based on errors

### Version Control

Keep track of:
- Training date
- Dataset version
- Model configuration
- Performance metrics
- Sample predictions

### Production Checklist

Before deploying:
- [ ] Validation accuracy >85%
- [ ] Model size <150MB
- [ ] Inference time <200ms
- [ ] Tested on diverse queries
- [ ] Documented known limitations

## Advanced Topics

### Transfer Learning

Use pre-trained career models:

```python
# Start from previous model
checkpoint = torch.load('previous_model.pth')
model.load_state_dict(checkpoint['model_state_dict'])

# Fine-tune on new data
for param in model.base_model.parameters():
    param.requires_grad = False  # Freeze base
```

### Multi-Task Learning

Train on multiple related tasks:
- Career recommendation
- Skill extraction
- Salary prediction

### Model Ensembling

Combine multiple models:

```python
# Average predictions from 3 models
pred = (model1(x) + model2(x) + model3(x)) / 3
```

## Support

For training issues:
- Check notebook error messages
- Review data format requirements
- Consult troubleshooting section
- Open GitHub issue with details

## Next Steps

After successful training:
1. Deploy to Streamlit app
2. Test with real users
3. Collect feedback
4. Iterate and improve
5. Retrain with new data

---

**Happy Training!** 🚀

Build an AI model that helps people find their perfect career path.
