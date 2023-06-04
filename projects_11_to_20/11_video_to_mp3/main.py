import os
import shutil

from pytube import YouTube


# If you get a certificate error in the terminal run:
# /Applications/Python\ 3.11/Install\ Certificates.command


def url_to_mp3(video_url: str):
    """Takes a video url and converts it into mp3 format"""

    # Get the video file and download it as an audio-only mp4
    video_file = YouTube(video_url).streams.filter().get_audio_only()
    video_file.download()

    # Replace .mp4 with .mp3
    mp4_name: str = video_file.default_filename
    mp3_name: str = mp4_name.replace('.mp4', '.mp3')
    os.rename(mp4_name, mp3_name)

    # Move it to a folder of your choice
    shutil.move(mp3_name, 'audio')


def main():
    try:
        input_url: str = input('Please enter a url: ')
        url_to_mp3(video_url=input_url)
        print('Finished downloading!')
    except Exception as e:
        print(f'Something went wrong: {e}')


if __name__ == '__main__':
    main()
