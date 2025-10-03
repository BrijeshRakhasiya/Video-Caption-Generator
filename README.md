# Video Caption Generator

This project is a Video Caption Generator that extracts audio from a video, transcribes it using AI, generates SRT subtitles, and burns them into the video.

## Overview

The project consists of several Python scripts that automate the process of adding captions to videos. It uses OpenAI's Whisper model for transcription and FFmpeg for video processing.

## Files and Structure

- `burn_caption.py`: Burns subtitles into the video using FFmpeg.
- `extract_audio.py`: Extracts audio from the video using MoviePy.
- `generate_srt.py`: Transcribes audio using Whisper and generates SRT file.
- `transcribe_audio.py`: Transcribes audio and prints the text (similar to generate_srt but without SRT generation).
- `audio/`: Directory containing extracted audio files.
  - `sample_audio.wav`: Extracted audio from sample.mp4.
- `captions/`: Directory containing subtitle files.
  - `output.srt`: Generated SRT subtitle file.
- `videos/`: Directory containing video files.
  - `sample.mp4`: Input video without captions (before).
  - `output_video.mp4`: Output video with burned-in captions (after).

## Models and Libraries Used

### AI Model
- **Whisper Model**: "base" - Used for speech-to-text transcription. Whisper is an open-source automatic speech recognition (ASR) system trained on large amounts of multilingual and multitask supervised data collected from the web.

### Libraries
- **whisper**: For loading and using the Whisper model.
- **moviepy**: For video editing and audio extraction.
- **srt**: For creating and composing SRT subtitle files.
- **subprocess**: For running FFmpeg commands.
- **os**: For file path operations.
- **datetime**: For handling time deltas in SRT generation.

### External Tools
- **FFmpeg**: Command-line tool for video and audio processing. Path: `C:\ffmpeg-2025-10-01-git-1a02412170-essentials_build\bin\ffmpeg.exe`

## Workflow

1. **Extract Audio**: Use `extract_audio.py` to extract audio from `videos/sample.mp4` and save as `audio/sample_audio.wav`.
2. **Transcribe Audio**: Use `generate_srt.py` or `transcribe_audio.py` to transcribe the audio using Whisper "base" model.
3. **Generate SRT**: `generate_srt.py` converts the transcription into SRT format and saves to `captions/output.srt`.
4. **Burn Captions**: Use `burn_caption.py` to burn the SRT subtitles into the video, creating `videos/output_video.mp4`.

## Before and After Videos

- **Before (No Captions)**: `videos/sample.mp4` - The original video without any captions.
- **After (With Captions)**: `videos/output_video.mp4` - The video with captions burned in using FFmpeg.

To view the videos, you can open them in any video player that supports MP4 format.

## Installation and Setup

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