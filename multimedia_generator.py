#!/usr/bin/env python3
"""
Multimedia Generator App
This application can generate images, audio, and videos from documents, audio files, and prompts
using various free API services.
"""

import os
import requests
import json
import base64
from typing import Optional, Dict, Any
import tempfile
import subprocess
import sys
from config import Config

class MultimediaGenerator:
    """
    A class to generate multimedia content (images, audio, video) from various inputs
    using free API services.
    """
    
    def __init__(self):
        # Use configuration for API keys
        self.openai_api_key = Config.OPENAI_API_KEY
        self.elevenlabs_api_key = Config.ELEVENLABS_API_KEY
        
        # API endpoints from configuration
        self.api_endpoints = {
            'openai_image': Config.OPENAI_IMAGE_API_URL,
            'openai_audio_transcription': Config.OPENAI_AUDIO_TRANSCRIPTION_API_URL,
            'openai_audio_generation': Config.OPENAI_AUDIO_GENERATION_API_URL,
            'stabilityai_image': Config.STABILITYAI_IMAGE_API_URL,
            'elevenlabs_tts': Config.ELEVENLABS_TTS_API_URL,
        }
    
    def generate_image_from_prompt(self, prompt: str, output_path: str = "generated_image.png") -> str:
        """
        Generate an image from a text prompt using OpenAI DALL-E API
        """
        if not self.openai_api_key:
            print("OpenAI API key not found. Using mock response for demonstration.")
            # For demo purposes, we'll create a placeholder image
            with open(output_path, 'wb') as f:
                f.write(b"")  # Placeholder
            return output_path
        
        headers = {
            "Authorization": f"Bearer {self.openai_api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "prompt": prompt,
            "n": 1,
            "size": "1024x1024"
        }
        
        try:
            response = requests.post(self.api_endpoints['openai_image'], headers=headers, json=data)
            response.raise_for_status()
            
            image_url = response.json()['data'][0]['url']
            
            # Download the image
            image_response = requests.get(image_url)
            with open(output_path, 'wb') as f:
                f.write(image_response.content)
            
            print(f"Image saved to {output_path}")
            return output_path
        except requests.exceptions.RequestException as e:
            print(f"Error generating image: {e}")
            return None
    
    def generate_image_from_document(self, document_path: str, output_path: str = "generated_image.png") -> str:
        """
        Extract text from document and generate image based on content
        """
        text = self._extract_text_from_document(document_path)
        if text:
            # Create a prompt based on document content
            prompt = f"Visual representation of: {text[:100]}..."  # Limit prompt length
            return self.generate_image_from_prompt(prompt, output_path)
        return None
    
    def _extract_text_from_document(self, document_path: str) -> str:
        """
        Extract text from various document formats
        """
        _, ext = os.path.splitext(document_path)
        
        if ext.lower() == '.txt':
            with open(document_path, 'r', encoding='utf-8') as f:
                return f.read()
        elif ext.lower() in ['.pdf', '.docx']:
            # For demo, we'll just return a placeholder
            # In a real implementation, you'd use libraries like PyPDF2, python-docx
            print(f"Document processing for {ext} files would require additional libraries")
            return f"Content from {document_path} document"
        else:
            print(f"Unsupported document format: {ext}")
            return ""
    
    def transcribe_audio(self, audio_path: str) -> str:
        """
        Transcribe audio to text using OpenAI Whisper API
        """
        if not self.openai_api_key:
            print("OpenAI API key not found. Returning mock transcription.")
            return "Mock transcription of the audio content"
        
        headers = {
            "Authorization": f"Bearer {self.openai_api_key}"
        }
        
        with open(audio_path, 'rb') as audio_file:
            files = {
                'file': (os.path.basename(audio_path), audio_file, 'audio/mpeg'),
                'model': (None, 'whisper-1')
            }
            
            try:
                response = requests.post(
                    self.api_endpoints['openai_audio_transcription'],
                    headers=headers,
                    files=files
                )
                response.raise_for_status()
                
                transcription = response.json()['text']
                print(f"Audio transcribed: {transcription}")
                return transcription
            except requests.exceptions.RequestException as e:
                print(f"Error transcribing audio: {e}")
                return ""
    
    def generate_audio_from_text(self, text: str, output_path: str = "generated_audio.mp3") -> str:
        """
        Generate audio from text using OpenAI TTS or ElevenLabs API
        """
        if self.elevenlabs_api_key:
            return self._generate_audio_elevenlabs(text, output_path)
        elif self.openai_api_key:
            return self._generate_audio_openai(text, output_path)
        else:
            print("No API keys found. Creating mock audio file.")
            with open(output_path, 'wb') as f:
                f.write(b"")  # Placeholder
            return output_path
    
    def _generate_audio_openai(self, text: str, output_path: str = "generated_audio.mp3") -> str:
        """
        Generate audio using OpenAI TTS API
        """
        headers = {
            "Authorization": f"Bearer {self.openai_api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "tts-1",
            "input": text,
            "voice": "alloy"  # Options: alloy, echo, fable, onyx, nova, shimmer
        }
        
        try:
            response = requests.post(self.api_endpoints['openai_audio_generation'], headers=headers, json=data)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            print(f"Audio saved to {output_path}")
            return output_path
        except requests.exceptions.RequestException as e:
            print(f"Error generating audio: {e}")
            return None
    
    def _generate_audio_elevenlabs(self, text: str, output_path: str = "generated_audio.mp3") -> str:
        """
        Generate audio using ElevenLabs API
        """
        url = f"{self.api_endpoints['elevenlabs_tts']}EXAVITQu4fcEWfcMWxpD"
        headers = {
            "xi-api-key": self.elevenlabs_api_key,
            "Content-Type": "application/json"
        }
        
        data = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            print(f"Audio saved to {output_path}")
            return output_path
        except requests.exceptions.RequestException as e:
            print(f"Error generating audio with ElevenLabs: {e}")
            return None
    
    def generate_video_from_prompt(self, prompt: str, output_path: str = "generated_video.mp4") -> str:
        """
        Generate a simple video based on prompt
        Note: True video generation APIs often require paid plans.
        This is a simplified implementation.
        """
        print(f"Video generation from prompt: '{prompt}'")
        print("Note: True video generation requires paid APIs. This creates a placeholder.")
        
        # Create a placeholder video file
        with open(output_path, 'w') as f:
            f.write(f"Video placeholder for prompt: {prompt}")
        
        print(f"Placeholder video saved to {output_path}")
        return output_path
    
    def generate_multimedia_from_document(self, document_path: str, output_dir: str = "./output") -> Dict[str, str]:
        """
        Generate all multimedia types from a document
        """
        os.makedirs(output_dir, exist_ok=True)
        
        results = {}
        
        # Extract text from document
        text = self._extract_text_from_document(document_path)
        
        if text:
            # Generate image from document content
            image_path = os.path.join(output_dir, "document_image.png")
            results['image'] = self.generate_image_from_prompt(text[:100], image_path)
            
            # Generate audio from document text
            audio_path = os.path.join(output_dir, "document_audio.mp3")
            results['audio'] = self.generate_audio_from_text(text, audio_path)
            
            # Generate video from document content
            video_path = os.path.join(output_dir, "document_video.mp4")
            results['video'] = self.generate_video_from_prompt(text[:100], video_path)
        
        return results
    
    def generate_multimedia_from_audio(self, audio_path: str, output_dir: str = "./output") -> Dict[str, str]:
        """
        Generate multimedia from audio file (transcribe and then generate other media)
        """
        os.makedirs(output_dir, exist_ok=True)
        
        results = {}
        
        # Transcribe audio to text
        text = self.transcribe_audio(audio_path)
        
        if text:
            # Generate image from transcribed text
            image_path = os.path.join(output_dir, "audio_image.png")
            results['image'] = self.generate_image_from_prompt(text[:100], image_path)
            
            # Generate audio from transcribed text (could be different voice)
            audio_path_out = os.path.join(output_dir, "audio_synthesized.mp3")
            results['audio'] = self.generate_audio_from_text(text, audio_path_out)
            
            # Generate video from transcribed text
            video_path = os.path.join(output_dir, "audio_video.mp4")
            results['video'] = self.generate_video_from_prompt(text[:100], video_path)
        
        return results


def main():
    """
    Main function to demonstrate the multimedia generator
    """
    print("Multimedia Generator App")
    print("This app can generate images, audio, and videos from documents, audio files, and prompts")
    print("="*60)
    
    generator = MultimediaGenerator()
    
    # Create sample files for demonstration
    sample_text = "A beautiful landscape with mountains and a lake at sunset"
    
    print("\n1. Generating image from text prompt...")
    img_path = generator.generate_image_from_prompt(sample_text, "sample_image.png")
    print(f"Generated image: {img_path}")
    
    print("\n2. Generating audio from text...")
    audio_path = generator.generate_audio_from_text(sample_text, "sample_audio.mp3")
    print(f"Generated audio: {audio_path}")
    
    print("\n3. Generating video from text...")
    video_path = generator.generate_video_from_prompt(sample_text, "sample_video.mp4")
    print(f"Generated video: {video_path}")
    
    print("\n4. Creating a sample document...")
    with open("sample_doc.txt", "w") as f:
        f.write("The future of artificial intelligence is bright. AI systems are becoming more capable and accessible, transforming industries and daily life.")
    
    print("\n5. Generating multimedia from document...")
    results = generator.generate_multimedia_from_document("sample_doc.txt")
    print(f"Results: {results}")
    
    print("\n6. Creating a sample audio transcription (mock)...")
    # For demonstration, we'll create a mock audio file
    with open("sample_audio.txt", "w") as f:
        f.write("This is a mock audio file for demonstration purposes.")
    
    print("\nMultimedia generation complete!")
    print("\nTo use this app with real APIs:")
    print("- Set OPENAI_API_KEY environment variable for OpenAI services")
    print("- Set ELEVENLABS_API_KEY environment variable for ElevenLabs TTS")
    print("- Use real document and audio files as input")


if __name__ == "__main__":
    main()