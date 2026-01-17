import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration"""
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Free and fast!
    MODELSLAB_API_KEY = os.getenv("MODELSLAB_API_KEY")
    SAVE_DIR = "audio_generations"
    
    # Model selection: 'openai', 'anthropic', 'google', or 'groq'
    MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "groq").lower()
    
    @classmethod
    def validate(cls):
        """Validate that required API keys are present"""
        if cls.MODEL_PROVIDER == "anthropic":
            return bool(cls.ANTHROPIC_API_KEY and cls.MODELSLAB_API_KEY)
        elif cls.MODEL_PROVIDER == "google":
            return bool(cls.GOOGLE_API_KEY and cls.MODELSLAB_API_KEY)
        elif cls.MODEL_PROVIDER == "groq":
            return bool(cls.GROQ_API_KEY and cls.MODELSLAB_API_KEY)
        else:  # openai
            return bool(cls.OPENAI_API_KEY and cls.MODELSLAB_API_KEY)

