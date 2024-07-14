import yt_dlp
import ffmpeg
from datetime import datetime


youtube_url = "https://www.youtube.com/watch?v=mhQjsLBfOoY"

# Get the current time with seconds precision
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_direct_stream_url(video_id):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'bestvideo[ext=mp4]/bestvideo'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_id, download=False)
        video_url = info_dict['url']
        return video_url

def capture_single_frame(video_url, output_filename='capture.jpg'):
    process = (
        ffmpeg
        .input(video_url, ss=5)  # Seek to 5 seconds into the video stream
        .output(output_filename, vframes=1, qscale=0)
        .run(capture_stdout=True, capture_stderr=True)
    )
    print(f"Image captured and saved as {output_filename}")

stream_url = get_direct_stream_url(youtube_url)

if stream_url:
    capture_single_frame(stream_url, output_filename=f'capture3_{timestamp}.jpg')