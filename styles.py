def get_custom_css():
    """Return custom CSS for the application"""
    return """
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .music-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        margin: 2rem 0;
    }
    .title-container {
        text-align: center;
        padding: 2rem 0;
        color: white;
    }
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #fff, #f0f0f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .subtitle {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.9);
        font-weight: 300;
    }
    .stTextArea textarea {
        border-radius: 15px;
        border: 2px solid #e0e0e0;
        padding: 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.75rem 3rem;
        font-size: 1.1rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    .success-message {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        font-weight: 600;
        margin: 1rem 0;
    }
    .music-icon {
        font-size: 4rem;
        text-align: center;
        margin: 1rem 0;
    }
    .stDownloadButton button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stDownloadButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(245, 87, 108, 0.4);
    }
    </style>
    """
