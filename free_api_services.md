# Free API Services for Multimedia Generation

This document details the free API services that can be used with the multimedia generator application.

## Image Generation APIs

### 1. OpenAI DALL-E API
- **Free Tier**: $5 credit for new users, which translates to about 50-100 images depending on usage
- **Rate Limits**: Varies by plan
- **API Endpoint**: `https://api.openai.com/v1/images/generations`
- **Usage Example**:
  ```python
  import requests
  import os
  
  headers = {
      "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
      "Content-Type": "application/json"
  }
  
  data = {
      "prompt": "A beautiful landscape",
      "n": 1,
      "size": "1024x1024"
  }
  
  response = requests.post(
      "https://api.openai.com/v1/images/generations",
      headers=headers,
      json=data
  )
  ```
- **Sign Up**: https://platform.openai.com/

### 2. Stability AI (Stable Diffusion)
- **Free Tier**: 2,000 image generations per month
- **Rate Limits**: 1 request per second
- **API Endpoint**: `https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image`
- **Sign Up**: https://stability.ai/

### 3. Hugging Face Diffusion Models
- **Free Tier**: Generous free tier with no strict limits
- **API Endpoint**: Various models available
- **Usage**: Access through Hugging Face Inference API
- **Sign Up**: https://huggingface.co/

## Audio Processing APIs

### 1. OpenAI Whisper API (Transcription)
- **Free Tier**: $5 credit for new users, about 100 minutes of transcription
- **Cost**: $0.006/minute after free credits
- **API Endpoint**: `https://api.openai.com/v1/audio/transcriptions`
- **Sign Up**: https://platform.openai.com/

### 2. OpenAI Text-to-Speech (TTS)
- **Free Tier**: $5 credit for new users
- **Cost**: $15/1M characters after free credits
- **API Endpoint**: `https://api.openai.com/v1/audio/speech`
- **Sign Up**: https://platform.openai.com/

### 3. ElevenLabs TTS API
- **Free Tier**: 10,000 characters per month
- **Rate Limits**: 20 requests per minute
- **API Endpoint**: `https://api.elevenlabs.io/v1/text-to-speech/{voice-id}`
- **Sign Up**: https://elevenlabs.io/

### 4. Google Cloud Text-to-Speech
- **Free Tier**: 4 million characters per month for the first 12 months
- **Cost**: $4/1M characters after free tier
- **API Endpoint**: `https://texttospeech.googleapis.com/v1/text:synthesize`
- **Sign Up**: https://cloud.google.com/text-to-speech

### 5. Amazon Polly
- **Free Tier**: 5 million characters per month for the first 12 months
- **Cost**: $4/1M characters after free tier
- **API Endpoint**: `https://polly.us-east-1.amazonaws.com/v1/speech`
- **Sign Up**: https://aws.amazon.com/polly/

## Video Generation APIs

### 1. Runway ML
- **Free Tier**: Limited generation minutes per month
- **Features**: Green screen, motion tracking, image to video
- **Sign Up**: https://runwayml.com/

### 2. Pika Labs
- **Free Tier**: Limited generations per day
- **Features**: Text to video, image to video
- **Sign Up**: https://www.pika.art/

### 3. LumaLabs Dream Machine
- **Free Tier**: Limited generations per day
- **Features**: Text to video
- **Sign Up**: https://lumalabs.ai/

### 4. Kaiber
- **Free Tier**: 5 free generations per day
- **Features**: Image/video to video style transfer
- **Sign Up**: https://www.kaiber.ai/

## Document Processing Libraries (Free & Open Source)

### 1. PyPDF2
- **Usage**: Extract text from PDF files
- **Installation**: `pip install PyPDF2`
- **GitHub**: https://github.com/py-pdf/PyPDF2

### 2. python-docx
- **Usage**: Extract text from DOCX files
- **Installation**: `pip install python-docx`
- **GitHub**: https://github.com/python-openxml/python-docx

### 3. textract
- **Usage**: Extract text from various document formats
- **Installation**: `pip install textract`
- **GitHub**: https://github.com/deanmalmgren/textract

## Setup Instructions

### 1. Environment Variables
Set up your API keys as environment variables:

```bash
export OPENAI_API_KEY='your_openai_api_key'
export ELEVENLABS_API_KEY='your_elevenlabs_api_key'
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python multimedia_generator.py
```

## Cost Estimation

### Image Generation
- OpenAI DALL-E: ~$0.018-0.024 per image (after free credits)
- Stability AI: ~$0.008 per image (after free credits)

### Audio Processing
- OpenAI Whisper: ~$0.006 per minute of audio
- OpenAI TTS: ~$0.015 per 1,000 characters
- ElevenLabs: ~$0.01 per 1,000 characters

### Video Generation
- Runway ML: Varies by feature, typically $0.10-0.50 per second
- Pika Labs: $0.05-0.25 per generation

## Best Practices for Free Tier Usage

1. **Monitor Usage**: Keep track of your API usage to avoid unexpected charges
2. **Batch Requests**: Process multiple items in batches to reduce API calls
3. **Cache Results**: Store generated content to avoid regenerating the same content
4. **Error Handling**: Implement proper error handling for API failures
5. **Fallback Options**: Have fallback mechanisms when APIs are unavailable or rate-limited

## Alternative Open Source Solutions

### 1. Local Image Generation
- **Stable Diffusion**: Run locally using libraries like Diffusers
- **Midjourney API alternatives**: Several open-source implementations

### 2. Local Text-to-Speech
- **Coqui TTS**: Open source TTS library
- **Mozilla TTS**: Open source TTS implementation

### 3. Local Video Generation
- **ModelScope**: Open source video generation models
- **RunwayML Local**: Some features available locally

These open source alternatives can be run locally without API costs, though they require more computational resources.