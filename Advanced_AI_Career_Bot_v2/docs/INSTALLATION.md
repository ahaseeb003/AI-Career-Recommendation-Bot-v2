# Installation Guide

## Advanced AI Career Bot v2.0

This guide will walk you through installing and setting up the Advanced AI Career Bot on your system.

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation Methods](#installation-methods)
3. [Verification](#verification)
4. [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Python**: Version 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **Internet**: Required for initial setup and AI features

### Recommended Setup

- **Python**: 3.9 or 3.10
- **RAM**: 8GB or more
- **GPU**: Not required (CPU inference is supported)

## Installation Methods

### Method 1: Quick Installation (Recommended)

1. **Extract the ZIP file**
   ```bash
   unzip Advanced_AI_Career_Bot_v2.zip
   cd Advanced_AI_Career_Bot_v2/streamlit_app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app should automatically open at `http://localhost:8501`
   - If not, manually navigate to this URL

### Method 2: Step-by-Step Installation

#### Step 1: Install Python

If you don't have Python installed:

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer, check "Add Python to PATH"
3. Verify: `python --version`

**macOS:**
```bash
brew install python@3.10
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.10 python3-pip
```

#### Step 2: Extract and Navigate

```bash
unzip Advanced_AI_Career_Bot_v2.zip
cd Advanced_AI_Career_Bot_v2/streamlit_app
```

#### Step 3: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

#### Step 4: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

This will install:
- PyTorch (ML framework)
- Transformers (NLP models)
- Streamlit (Web framework)
- And other dependencies

#### Step 5: Verify Installation

```bash
python -c "import streamlit; import torch; print('Installation successful!')"
```

#### Step 6: Run the Application

```bash
streamlit run app.py
```

### Method 3: With Model Training

If you want to train your own model:

1. **Complete Method 1 or 2 above**

2. **Prepare your datasets** (see [Training Guide](TRAINING.md))

3. **Open Google Colab**
   - Navigate to [Google Colab](https://colab.research.google.com/)
   - Upload `colab/Multi_Source_Career_Model_Training.ipynb`

4. **Train the model**
   - Upload your dataset CSV files
   - Run all cells in the notebook
   - Download `trained_models.zip`

5. **Deploy trained models**
   ```bash
   # Extract trained models
   unzip trained_models.zip
   
   # Move to models directory
   mv career_model_cpu.pth streamlit_app/models/
   mv label_encoder.pkl streamlit_app/models/
   mv career_embeddings.npy streamlit_app/models/
   mv model_metadata.json streamlit_app/models/
   ```

6. **Run the app**
   ```bash
   cd streamlit_app
   streamlit run app.py
   ```

## Configuration

### OpenRouter API Key (Optional but Recommended)

For AI Career Coach features:

1. Sign up at [openrouter.ai](https://openrouter.ai)
2. Get your API key
3. Enter it in the app sidebar

### Environment Variables (Optional)

Create a `.env` file in `streamlit_app/`:

```bash
OPENROUTER_API_KEY=your_api_key_here
DEFAULT_MODEL=anthropic/claude-3.5-sonnet
```

## Verification

### 1. Check Python Version

```bash
python --version
# Should show Python 3.8 or higher
```

### 2. Check Installed Packages

```bash
pip list | grep streamlit
pip list | grep torch
pip list | grep transformers
```

### 3. Test Application

```bash
streamlit run app.py
```

Expected output:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

### 4. Verify Model Loading

In the app:
1. Go to "Career Matching" tab
2. Enter a sample description
3. Click "Get Career Recommendations"
4. Should see recommendations within a few seconds

## Troubleshooting

### Issue 1: ModuleNotFoundError

**Error**: `ModuleNotFoundError: No module named 'streamlit'`

**Solution**:
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall requirements
pip install -r requirements.txt
```

### Issue 2: torch Installation Fails

**Error**: `ERROR: Could not find a version that satisfies the requirement torch`

**Solution**:
```bash
# Install CPU version of PyTorch
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Issue 3: Model Files Not Found

**Error**: `FileNotFoundError: Model files not found`

**Solution**:
1. Ensure you're in the correct directory
2. Check if `models/` folder exists
3. Download pre-trained models or train your own
4. Verify file paths in `utils/model_loader.py`

### Issue 4: Port Already in Use

**Error**: `Port 8501 is already in use`

**Solution**:
```bash
# Use a different port
streamlit run app.py --server.port 8502
```

Or kill the process using port 8501:
```bash
# Windows
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8501 | xargs kill -9
```

### Issue 5: Slow Performance

**Symptoms**: App is slow or unresponsive

**Solutions**:
1. **Use CPU-optimized model**
   - Ensure `career_model_cpu.pth` is being loaded
   
2. **Reduce inference batch size**
   - Edit `utils/model_loader.py`
   - Decrease `max_length` parameter

3. **Close other applications**
   - Free up RAM

4. **Use pre-computed embeddings**
   - Ensure `career_embeddings.npy` exists

### Issue 6: OpenRouter API Errors

**Error**: `401 Unauthorized` or `API Error`

**Solutions**:
1. Verify API key is correct
2. Check if you have available credits
3. Test API key at [OpenRouter Dashboard](https://openrouter.ai/dashboard)
4. Ensure internet connection is stable

### Issue 7: Import Errors

**Error**: `ImportError: cannot import name 'X'`

**Solution**:
```bash
# Reinstall specific package
pip uninstall transformers
pip install transformers --no-cache-dir

# Or reinstall all
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

## Platform-Specific Instructions

### Windows

**If you see SSL certificate errors:**
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

**If antivirus blocks installation:**
- Temporarily disable antivirus
- Add Python folder to exclusions

### macOS

**If you see permission errors:**
```bash
sudo pip3 install -r requirements.txt
```

**If Xcode tools are needed:**
```bash
xcode-select --install
```

### Linux

**If you see build errors:**
```bash
sudo apt-get install build-essential python3-dev
```

**For headless servers:**
```bash
# Install system dependencies
sudo apt-get install python3-opencv

# Run without browser opening
streamlit run app.py --server.headless true
```

## Updating

To update to a newer version:

```bash
# Pull latest code
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart app
streamlit run app.py
```

## Uninstallation

To completely remove the application:

```bash
# Deactivate virtual environment
deactivate

# Remove project directory
rm -rf Advanced_AI_Career_Bot_v2/

# Or on Windows
rmdir /s Advanced_AI_Career_Bot_v2\
```

## Next Steps

After successful installation:

1. Read the [Usage Guide](USAGE.md)
2. Try the demo with default data
3. (Optional) Train your model with custom datasets
4. (Optional) Set up OpenRouter API for AI coach

## Support

If you encounter issues not covered here:

1. Check the [main README](../README.md)
2. Search existing GitHub issues
3. Create a new issue with:
   - Your OS and Python version
   - Complete error message
   - Steps to reproduce

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)
- [OpenRouter Documentation](https://openrouter.ai/docs)

---

**Installation complete!** 🎉

You're ready to discover your perfect career path with AI-powered guidance.
