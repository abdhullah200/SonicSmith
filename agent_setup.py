from agno.agent import Agent
from agno.tools.models_labs import FileType, ModelsLabTools
from config import Config


def create_music_agent():
    """Create and configure the music generation agent"""
    # Import the appropriate model based on provider
    if Config.MODEL_PROVIDER == "anthropic":
        from agno.models.anthropic import Claude
        model = Claude(id="claude-sonnet-4-20250514", api_key=Config.ANTHROPIC_API_KEY)
    elif Config.MODEL_PROVIDER == "google":
        from agno.models.google import Gemini
        model = Gemini(id="models/gemini-pro", api_key=Config.GOOGLE_API_KEY)
    elif Config.MODEL_PROVIDER == "groq":
        from agno.models.groq import Groq
        model = Groq(id="llama-3.3-70b-versatile", api_key=Config.GROQ_API_KEY)
    else:  # openai
        from agno.models.openai import OpenAIChat
        model = OpenAIChat(id="gpt-4o", api_key=Config.OPENAI_API_KEY)
    
    return Agent(
        model=model,
        tools=[
            ModelsLabTools(
                api_key=Config.MODELSLAB_API_KEY,
                wait_for_completion=True,
                file_type=FileType.MP3
            )
        ],
        instructions=[
            "You are an AI agent that can generate music using the ModelsLabs API.",
            "When generating music, use the `generate_media` tool with detailed prompts that specify:",
            "- The genre and style of music (e.g., classical, jazz, electronic)",
            "- The instruments and sounds to include",
            "- The tempo, mood and emotional qualities",
            "- The structure (intro, verses, chorus, bridge, etc.)",
            "Create rich, descriptive prompts that capture the desired musical elements.",
            "Focus on generating high-quality, complete instrumental pieces.",
        ],
        markdown=True,
    )