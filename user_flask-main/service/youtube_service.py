import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import whisper

# Coloque a constante ACCEPTED_AUDIO_FORMATS e a inicialização do modelo aqui
ACCEPTED_AUDIO_FORMATS = ["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]
MODEL = whisper.load_model("tiny")

class YoutubeService:
    def download_youtube_audio(self, link) -> str:
        try:
            video = YouTube(link)
        except VideoUnavailable:
            print("The video is unavailable. Please check the URL.")
            return None
        stream = video.streams.get_audio_only()
        try:
            file_path = stream.download("yt_downloads")
            print("Downloading youtube video")
        except FileNotFoundError:
            os.mkdir("yt_downloads")
            file_path = stream.download("yt_downloads")
        print("Downloaded successfully")
        return os.path.abspath(file_path)

    def transcribe(self, full_path) -> None:
        # file_path, file_name_ext = os.path.split(full_path)
        # file_name, ext = os.path.splitext(file_name_ext)
        # ext = ext[1:]
        # if ext not in ACCEPTED_AUDIO_FORMATS:
        #     raise Exception(f"Invalid audio format: {ext}")
        # print(f""""{file_name}" is being transcribed...""")
        # audio = whisper.load_audio(full_path)
        # transcription = MODEL.transcribe(audio)
        # transcription_text = transcription['text']
        # print(f""""{file_name}.{ext}" was successfully transcribed!""")
        # with open(f"{file_path}/{file_name}.txt", "w", encoding='utf-8') as f:
        #     f.write(transcription_text)
        # os.remove(f"{file_path}/{file_name}.{ext}")
        transcription_text = "allalalalalalalalala"
        return ("caminho/de/teste", transcription_text)
        # return (f"{file_path}/{file_name}.txt", transcription_text)