#!/usr/bin/env python3
"""
Example usage of the Multimedia Generator App
This script demonstrates various ways to use the multimedia generator
"""

from multimedia_generator import MultimediaGenerator
import os

def example_text_to_multimedia():
    """
    Example: Generate multimedia from text prompts
    """
    print("=== Example 1: Text to Multimedia ===")
    generator = MultimediaGenerator()
    
    prompt = "A futuristic cityscape with flying vehicles and neon lights"
    
    # Generate image from text
    print("Generating image from text prompt...")
    image_path = generator.generate_image_from_prompt(prompt, "example_image.png")
    print(f"Image saved to: {image_path}")
    
    # Generate audio from text
    print("Generating audio from text...")
    audio_path = generator.generate_audio_from_text(prompt, "example_audio.mp3")
    print(f"Audio saved to: {audio_path}")
    
    # Generate video from text
    print("Generating video from text...")
    video_path = generator.generate_video_from_prompt(prompt, "example_video.mp4")
    print(f"Video saved to: {video_path}")
    print()


def example_document_to_multimedia():
    """
    Example: Generate multimedia from document
    """
    print("=== Example 2: Document to Multimedia ===")
    
    # Create a sample document
    doc_content = """
    The Future of Artificial Intelligence
    
    Artificial intelligence is rapidly transforming our world. From healthcare to transportation,
    AI systems are becoming more sophisticated and capable. Machine learning algorithms can now
    process vast amounts of data, identify patterns, and make decisions with human-like accuracy.
    
    In the coming decades, we can expect AI to revolutionize industries, create new job categories,
    and solve complex global challenges like climate change and disease detection.
    """
    
    with open("sample_document.txt", "w") as f:
        f.write(doc_content)
    
    generator = MultimediaGenerator()
    
    # Generate multimedia from document
    results = generator.generate_multimedia_from_document("sample_document.txt", "./doc_output")
    
    print("Multimedia generated from document:")
    print(f"  - Image: {results.get('image')}")
    print(f"  - Audio: {results.get('audio')}")
    print(f"  - Video: {results.get('video')}")
    print()


def example_audio_to_multimedia():
    """
    Example: Generate multimedia from audio (transcription + generation)
    """
    print("=== Example 3: Audio to Multimedia ===")
    print("Note: This example demonstrates the process. You would need an actual audio file.")
    
    # In a real scenario, you would have an audio file
    # For this example, we'll create a mock transcription
    mock_audio_transcription = "The benefits of renewable energy are becoming increasingly clear. Solar and wind power are now cost-competitive with fossil fuels in many regions."
    
    # Save mock transcription to a file to simulate audio processing
    with open("mock_audio_transcription.txt", "w") as f:
        f.write(mock_audio_transcription)
    
    generator = MultimediaGenerator()
    
    # Simulate processing audio by using the transcribed text
    print("Generating image from audio transcription...")
    image_path = generator.generate_image_from_prompt(mock_audio_transcription[:100], "audio_image.png")
    print(f"Image saved to: {image_path}")
    
    print("Generating new audio from transcription...")
    audio_path = generator.generate_audio_from_text(mock_audio_transcription, "audio_synthesized.mp3")
    print(f"Audio saved to: {audio_path}")
    
    print("Generating video from transcription...")
    video_path = generator.generate_video_from_prompt(mock_audio_transcription[:100], "audio_video.mp4")
    print(f"Video saved to: {video_path}")
    print()


def example_batch_processing():
    """
    Example: Batch processing multiple prompts
    """
    print("=== Example 4: Batch Processing ===")
    generator = MultimediaGenerator()
    
    prompts = [
        "A serene mountain landscape at sunrise",
        "An underwater coral reef with colorful fish",
        "A bustling cyberpunk marketplace",
        "A peaceful countryside with windmills"
    ]
    
    output_dir = "./batch_output"
    os.makedirs(output_dir, exist_ok=True)
    
    for i, prompt in enumerate(prompts):
        print(f"Processing prompt {i+1}: {prompt[:50]}...")
        
        # Generate image
        img_path = generator.generate_image_from_prompt(
            prompt, 
            os.path.join(output_dir, f"batch_image_{i+1}.png")
        )
        
        # Generate audio
        audio_path = generator.generate_audio_from_text(
            prompt, 
            os.path.join(output_dir, f"batch_audio_{i+1}.mp3")
        )
        
        print(f"  - Image: {img_path}")
        print(f"  - Audio: {audio_path}")
    
    print(f"All batch processing completed in {output_dir}")
    print()


def main():
    """
    Main function to run all examples
    """
    print("Multimedia Generator - Example Usage")
    print("=" * 50)
    print()
    
    example_text_to_multimedia()
    example_document_to_multimedia()
    example_audio_to_multimedia()
    example_batch_processing()
    
    print("All examples completed!")
    print()
    print("To use with real API keys:")
    print("- Set OPENAI_API_KEY environment variable")
    print("- Set ELEVENLABS_API_KEY environment variable")
    print("- Use actual document and audio files as input")


if __name__ == "__main__":
    main()