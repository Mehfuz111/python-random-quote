# Multimedia Generator App

This application can generate images, audio, and videos from documents, audio files, and prompts using various free API services.

## Features

- Generate images from text prompts using OpenAI DALL-E API
- Generate images from document content
- Transcribe audio files to text using OpenAI Whisper API
- Generate audio from text using OpenAI TTS or ElevenLabs API
- Generate video placeholders from text prompts
- Process various document formats (TXT, PDF, DOCX)
- Generate multimedia content from audio files by transcribing them first

## Free API Services Used

### Image Generation
1. **OpenAI DALL-E API** - Free tier with 50 credits per month
2. **Stable Diffusion API** - Free tier available from Stability AI

### Audio Processing
1. **OpenAI Whisper API** - Free tier (transcription)
2. **OpenAI TTS API** - Free tier with credits
3. **ElevenLabs API** - Free tier with limited usage

### Video Generation
1. **Runway ML** - Free tier for basic video generation
2. **Pika Labs** - Free tier available
3. **LumaLabs Dream Machine** - Free tier available

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Setup

### API Keys

To use the full functionality, you'll need to set up API keys for the services:

```bash
export OPENAI_API_KEY='your_openai_api_key'
export ELEVENLABS_API_KEY='your_elevenlabs_api_key'
```

For Windows:
```cmd
set OPENAI_API_KEY=your_openai_api_key
set ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

### Getting API Keys

1. **OpenAI API Key**:
   - Go to [OpenAI Platform](https://platform.openai.com/)
   - Create an account and generate an API key
   - Free tier provides $5 credit for new users

2. **ElevenLabs API Key**:
   - Go to [ElevenLabs](https://elevenlabs.io/)
   - Create an account and find your API key in the dashboard
   - Free tier provides 10,000 characters per month

## Usage

### Command Line

Run the application:

```bash
python multimedia_generator.py
```

### As a Library

```python
from multimedia_generator import MultimediaGenerator

generator = MultimediaGenerator()

# Generate image from prompt
image_path = generator.generate_image_from_prompt("A beautiful landscape", "output.png")

# Generate audio from text
audio_path = generator.generate_audio_from_text("Hello world", "output.mp3")

# Generate multimedia from document
results = generator.generate_multimedia_from_document("document.txt")
```

## Supported Input Formats

- Documents: .txt, .pdf, .docx (with additional libraries)
- Audio: .mp3, .wav, .m4a, .mp4 (and other formats supported by OpenAI)
- Images: Generated in PNG format

## Limitations

- Video generation requires paid APIs for full functionality
- Free API tiers have usage limits
- Document processing for PDF and DOCX requires additional libraries
- Some features may not work without API keys (will use mock responses)

## Example Usage

```python
from multimedia_generator import MultimediaGenerator

generator = MultimediaGenerator()

# Generate an image from a text prompt
image_path = generator.generate_image_from_prompt(
    "A futuristic city with flying cars at sunset",
    "futuristic_city.png"
)

# Generate audio from a text
audio_path = generator.generate_audio_from_text(
    "Welcome to the future of artificial intelligence",
    "welcome_audio.mp3"
)

# Generate all multimedia from a document
results = generator.generate_multimedia_from_document("my_document.txt")
print(f"Generated image: {results['image']}")
print(f"Generated audio: {results['audio']}")
print(f"Generated video: {results['video']}")
```

## Free API Alternatives

If you prefer other free services, here are some alternatives:

### Image Generation
- Hugging Face Diffusion Models (free tier)
- Replicate API (free tier with credits)

### Text-to-Speech
- Google Cloud Text-to-Speech (free tier)
- Amazon Polly (free tier)
- Mozilla TTS (open source)

### Video Generation
- Kaiber (free tier)
- Synthesia (limited free trial)

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to improve the application.

## License

This project is open source and available under the MIT License.