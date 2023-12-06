from domain.youtube_video import YoutubeVideo

class YoutubeRepository:
    def get_video(self, video_id):
        return YoutubeVideo.query.get(video_id)