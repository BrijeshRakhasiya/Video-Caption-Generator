from moviepy.editor import VideoFileClip
import os 


def extract_audio(video_path , output_audio_path) :
    try : 
        video = VideoFileClip(video_path)
        audio = video.audio
        if audio :
            audio.write_audiofile(output_audio_path)
            print(f"Audio extracted Successfully: {output_audio_path}")
        else :
            print(f"[!] No audio tract found in the video")
    except Exception as e :
        print(f"[!] Error extracting audio : {e}")

if __name__ == "__main__" :
    video_path = "videos/sample.mp4"
    audio_output_path = "audio/sample_audio.wav"

    os.makedirs(os.path.dirname(audio_output_path) , exist_ok=True)

    extract_audio(video_path=video_path , output_audio_path=audio_output_path)
    