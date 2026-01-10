"""
Configuration file for Multimedia Generator App
"""

import os
from typing import Optional

class Config:
    """
    Configuration class to manage API keys and settings
    """
    
    # API Keys - can be set as environment variables
    OPENAI_API_KEY: Optional[str] = os.getenv('OPENAI_API_KEY')
    ELEVENLABS_API_KEY: Optional[str] = os.getenv('ELEVENLABS_API_KEY')
    
    # API Endpoints
    OPENAI_IMAGE_API_URL: str = "https://api.openai.com/v1/images/generations"
    OPENAI_AUDIO_TRANSCRIPTION_API_URL: str = "https://api.openai.com/v1/audio/transcriptions"
    OPENAI_AUDIO_GENERATION_API_URL: str = "https://api.openai.com/v1/audio/speech"
    STABILITYAI_IMAGE_API_URL: str = "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image"
    ELEVENLABS_TTS_API_URL: str = "https://api.elevenlabs.io/v1/text-to-speech/"
    
    # Default settings
    DEFAULT_IMAGE_SIZE: str = "1024x1024"
    DEFAULT_AUDIO_VOICE: str = "alloy"
    DEFAULT_OUTPUT_DIR: str = "./output"
    
    # Free tier limits (approximate)
    FREE_TIER_LIMITS = {
        'openai_images_per_month': 50,  # DALL-E free tier
        'openai_minutes_per_month': 100,  # Whisper minutes
        'elevenlabs_characters_per_month': 10000,  # ElevenLabs characters
    }
    
    @classmethod
    def validate_config(cls) -> bool:
        """
        Validate that the configuration is properly set up
        """
        # For now, just check if API keys are set
        has_openai = bool(cls.OPENAI_API_KEY)
        has_elevenlabs = bool(cls.ELEVENLABS_API_KEY)
        
        if not has_openai and not has_elevenlabs:
            print("Warning: No API keys are configured. The app will use mock responses.")
            print("Please set OPENAI_API_KEY and/or ELEVENLABS_API_KEY environment variables.")
        
        return has_openai or has_elevenlabs