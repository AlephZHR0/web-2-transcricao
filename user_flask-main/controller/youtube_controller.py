from flask import Blueprint, jsonify, request
from service.youtube_service import YoutubeService

youtube_blueprint = Blueprint('youtube', __name__)
youtube_service = YoutubeService()

@youtube_blueprint.route('/download', methods=['POST'])
def download_video():
    data = request.json
    youtube_link = data.get('link')
    file_path = youtube_service.download_youtube_audio(youtube_link)
    if file_path:
        transcription_path, transcription_text = youtube_service.transcribe(file_path)
        return jsonify({"message": "Video downloaded and transcribed successfully",
                        "path": transcription_path,
                        "text": transcription_text,
                        }), 200
    else:
        return jsonify({"error": "Video download failed"}), 400