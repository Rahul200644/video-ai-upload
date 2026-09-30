# 🎬 Video AI Agent

An automated AI-powered video creation pipeline built with n8n and Python.

## 📁 Project Structure

```
video-ai-agent/
├── assets/          # Static assets (music, overlays, etc.)
├── outputs/         # Generated outputs (images, audio, video)
│   ├── img_0.jpg
│   ├── img_2.jpg
│   ├── voiceover.mp3
│   └── final_video.mp4
└── scripts/
    └── make_video.py   # FFmpeg video rendering script
```

## 🚀 Features

- **Script Generation** – LLM-powered scene scripts (Ollama)
- **Image Generation** – AI-generated scene images
- **Text-to-Speech** – Voiceover generation (voiceover.mp3)
- **Subtitles** – Auto-generated .srt captions (zero-API)
- **Video Rendering** – FFmpeg-based final video assembly
- **SEO Optimization** – YouTube/Instagram metadata generation
- **Scheduling** – Automated publish workflow

## 🛠️ Requirements

- Python 3.10+
- FFmpeg installed and in PATH
- n8n (self-hosted or cloud)
- Ollama running locally

## ▶️ Usage

```bash
python scripts/make_video.py
```

## 📌 n8n Workflow

The full automation runs via n8n with 37 nodes covering:
- Trigger → Script → Images → Audio → Subtitles → Video → SEO → Publish
