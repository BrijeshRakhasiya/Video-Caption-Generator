import subprocess
import os 

def burn_subtitles(video_path , srt_path , output_path , ffmpeg_path) : 

    video_full = os.path.abspath(video_path)
    output_full = os.path.abspath(output_path)

    command = f'"{ffmpeg_path}" -i "{video_full}" -vf "subtitles={srt_path}" "{output_full}"'

    print("Running Command : ")
    print(command)

    try : 
        subprocess.run(command , shell=True , check=True )
        print(f"Video with burned - in captions generated : {output_full}")
    except subprocess.CalledProcessError as e : 
        print(f"[!] Error burning subtitles : {e}")

if __name__ == "__main__" :

    ffmpeg_path = r"C:\ffmpeg-2025-10-01-git-1a02412170-essentials_build\bin\ffmpeg.exe"

    video_path = "videos/sample.mp4"
    srt_path = "captions/output.srt"
    output_video = "videos/output_video.mp4"

    burn_subtitles(video_path , srt_path , output_video , ffmpeg_path)
    