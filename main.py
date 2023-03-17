import whisper 
import moviepy.editor

video = moviepy.editor.VideoFileClip("video.mp4")
audio = video.audio
audio.write_audiofile("audio.mp3")
model = whisper.load_model('base')
result = model.transcribe("audio.mp3", fp16=False)
print(result['text'])