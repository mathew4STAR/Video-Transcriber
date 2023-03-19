import whisper 
import moviepy.editor
import os
import speech_recognition as sr

audiofile = "audio.mp3"

def finish_cleanup(result):
    write_choice = input("Do you want to write it to a file (Y)Yes or (N)No: ")
    if write_choice in "Yy":
        t_file = open("transciption.txt", "w")
        t_file.write(result)
        t_file.close()
    del_c = input("Do you want to delete source files(converted audio file) (Y)Yes or (N)No: ")
    if del_c in "Yy":
        os.remove(audiofile)

def download(link):
    print("Still in development")

def convert_audio(path):
    vid = moviepy.editor.VideoFileClip(path)
    audio = vid.audio
    audio.write_audiofile(audiofile)

def speech_text():
    mode = input("Which speech to text do you went to use Whisper(W) Google(G):")
    if mode in "Gg":
        with sr.AudioFile(audiofile) as source:
            audio_text = sr.Recognizer.listen(source)
        fresult = sr.Recognizer.recognize_google(audio_text)
        print(fresult)

    elif mode in "Ww":
        print("Which model do you want to use (t)tiny (b)base (s)small (m)medium (l)large: ")
        print("More information about these models at https://github.com/openai/whisper")
        val = input("Enter choice: ")
        vers = {"b":"base", "t":"tiny", "s":"small", "m":"medium", "l":"large"}
        model = whisper.load_model(vers[val])
        result = model.transcribe(audiofile, fp16=False)
        fresult = result['text']
    print(fresult)
    return fresult

mode = input("Do you want to transcribe from a local installed file(L) or transcribe an online video(O): ")

if mode in "Ll":
    path = input("Enter the full path for the file to be transcribed: ")
elif mode in "Oo":
    link = input("Enter the full link to the video: ")
    path = download(link)
else:
    print("Invalid choice, please choose ('O' or 'o') for Online and ('L' or 'l') for local video")

convert_audio(path)
result = speech_text()
finish_cleanup(result)
