# 🎥 Video Caption Generator

This project is a **Video Caption Generator** that extracts audio from a video, transcribes it using AI, generates SRT subtitles, and burns them into the video.

---

## 📖 Overview

This repo contains Python scripts that automate the process of adding captions to videos. It uses OpenAI's Whisper model for transcription and FFmpeg for video processing.

---

## 📁 Files and Structure

- `burn_caption.py` — Burns subtitles into the video using FFmpeg  
- `extract_audio.py` — Extracts audio from the video using MoviePy  
- `generate_srt.py` — Transcribes audio using Whisper and generates SRT file  
- `transcribe_audio.py` — Transcribes audio and prints the text  
- `audio/` — Contains extracted audio files  
  - `sample_audio.wav`  
- `captions/` — Contains subtitle files  
  - `output.srt`  
- `videos/` — Contains video files  
  - `sample.mp4` (before captions)  
  - `output_video.mp4` (after captions)

---

## 🧠 Models and Libraries Used

### 🤖 AI Model
- **Whisper (base)** — Open-source ASR system for transcription

### 📦 Libraries
- `whisper` — Whisper model interface  
- `moviepy` — Video/audio editing  
- `srt` — Subtitle file generation  
- `subprocess`, `os`, `datetime` — System utilities

### 🛠️ External Tools
- **FFmpeg**: Command-line tool for video and audio processing. Path: `C:\ffmpeg-2025-10-01-git-1a02412170-essentials_build\bin\ffmpeg.exe`


---

## ⚙️ Workflow

1. 🎧 Extract audio:  
 `python extract_audio.py`

2. 📝 Transcribe audio:  
 `python generate_srt.py` or `python transcribe_audio.py`

3. 📄 Generate SRT:  
 `generate_srt.py` creates `captions/output.srt`

4. 🔥 Burn captions:  
 `python burn_caption.py` creates `videos/output_video.mp4`

---

## 🎬 Demo Preview

Click below to view the captioned video:

[![Watch the captioned video](https://img.icons8.com/ios-filled/100/play-button-circled.png)](videos/output_video.mp4)

---

## 🎞️ Before and After Videos

- 📼 **Before (No Captions)**: [`sample.mp4`](videos/sample.mp4)  
- ✅ **After (With Captions)**: [`output_video.mp4`](videos/output_video.mp4)

> Click the links above to download or play the videos in your browser.

---

## 🛠️ Installation and Setup

1. Install required Python packages:
   ```
   pip install openai-whisper moviepy srt
   ```

2. Download and install FFmpeg from https://ffmpeg.org/download.html and update the path in `burn_caption.py`.

3. Place your input video in `videos/sample.mp4`.

4. Run the scripts in order:
   - `python extract_audio.py`
   - `python generate_srt.py`
   - `python burn_caption.py`

## Notes

- The Whisper model "base" is used for transcription. You can change to other models like "small", "medium", "large" in the code for better accuracy (but slower processing).
- Ensure FFmpeg is installed and the path is correct.
- The project assumes WAV audio format for transcription.
- SRT files are in UTF-8 encoding.

## Dependencies

- Python 3.x
- FFmpeg
- OpenAI Whisper
- MoviePy
- SRT library

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Author

**Brijesh Rakhasiya**  
AI/ML Engineer · Data Scientist · Problem Solver

---

**👨‍💻 Developed by Brijesh Rakhasiya**
