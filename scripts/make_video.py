import os, requests
from gtts import gTTS
try:
    from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
except ImportError:
    from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from PIL import Image

PEXELS_KEY = "C55hGCPUQNEtGGB6ksDx5weXLz7NaE7jkAktGkAVzFODiS7kEelSMNYx"
OUT = "C:/video-ai-agent/outputs"
os.makedirs(OUT, exist_ok=True)

def create_video(topic, script, keywords):
    print("1. Generating Audio...")
    audio_path = os.path.join(OUT, "voiceover.mp3")
    gTTS(text=script, lang='en').save(audio_path)
    audio = AudioFileClip(audio_path)
    dur = audio.duration

    print("2. Downloading Pexels Images...")
    img_files = []
    headers = {"Authorization": PEXELS_KEY}
    for i, kw in enumerate(keywords):
        try:
            r = requests.get(f"https://api.pexels.com/v1/search?query={kw}&orientation=portrait&per_page=1", headers=headers).json()
            if "photos" in r and len(r["photos"]) > 0:
                url = r["photos"][0]["src"]["large"]
                path = os.path.join(OUT, f"img_{i}.jpg")
                with open(path, "wb") as f: f.write(requests.get(url).content)
                Image.open(path).resize((1080, 1920)).save(path)
                img_files.append(path)
        except Exception as e:
            print(f"Error fetching {kw}: {e}")

    print("3. Rendering 9:16 MP4 Video...")
    if not img_files:
        print("No images downloaded. Check Pexels API Key!")
        return None
    per_dur = dur / len(img_files)
    clips = [ImageClip(p).with_duration(per_dur) if hasattr(ImageClip(p), 'with_duration') else ImageClip(p).set_duration(per_dur) for p in img_files]
    video = concatenate_videoclips(clips, method="compose")
    video = video.with_audio(audio) if hasattr(video, 'with_audio') else video.set_audio(audio)
    out_file = os.path.join(OUT, "final_video.mp4")
    video.write_videofile(out_file, fps=24, codec="libx264", audio_codec="aac")
    print("FINISHED: Video created at " + out_file)
    return out_file

if __name__ == "__main__":
    create_video("AI Education", "Artificial Intelligence is transforming how we learn. With smart AI tools, students can learn complex topics in minutes.", ["technology", "student", "future"])
