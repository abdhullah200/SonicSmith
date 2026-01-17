import os
from uuid import uuid4
import requests
from agno.utils.log import logger
from config import Config


class MusicGenerator:
    """Handle music generation and file operations"""
    
    def __init__(self, agent):
        self.agent = agent
        os.makedirs(Config.SAVE_DIR, exist_ok=True)
    
    def generate(self, prompt: str):
        """Generate music from prompt"""
        return self.agent.run(prompt)
    
    def download_audio(self, url: str) -> tuple[bytes, str]:
        """Download audio from URL and return bytes and filename"""
        response = requests.get(url)
        
        if not response.ok:
            raise Exception(f"Failed to download audio. Status code: {response.status_code}")
        
        content_type = response.headers.get("Content-Type", "")
        if "audio" not in content_type:
            raise Exception(f"Invalid file type returned: {content_type}")
        
        filename = f"{Config.SAVE_DIR}/music_{uuid4()}.mp3"
        with open(filename, "wb") as f:
            f.write(response.content)
        
        return response.content, filename

