from pytube import YouTube
import os
from pytube.cli import on_progress 

def download(urls):
    if urls == "":
        urls = input("Enter the URLs of the videos you want to download seperated by '|' \n>> ")
    urls = urls.split("|")

    destination = get_dest()
    for url in urls:
        download_mp4(url,destination)
    rename_to_mp3(destination)

# ask for destination directory
def get_dest():
    print("Enter the destination (leave blank for mp3 folder)")
    destination = str(input(">> ")) or './mp3'
    if not os.path.isdir(destination):
        print("Destination {} does not exist, file will be saved in {} folder as default.".format(destination,os.getcwd()+"\mp3"))
        destination = './mp3'
    return destination

def download_mp4(url,destination):
    try:
        yt = YouTube(str(url),on_progress_callback=on_progress)
        video = yt.streams.get_audio_only()
    except Exception:
        print('''Something wrong with URL {}, make sure you have internet connection and include full url like 
https://www.youtube.com/watch?v=VIDID where VIDID is the ID of the video.'''.format(url))
        return

    # download the file
    print("Downloading {}".format(yt.title))
    video.download(output_path=destination)
    print("{} has been successfully downloaded.".format(yt.title))


def rename_to_mp3(path):
    for file in os.listdir(path):
        if "mp4" in file:
            base, ext = os.path.splitext(file)
            old_file = path + "/" + file
            new_file = path + "/" + base + '.mp3'
            try:
                os.rename(old_file, new_file)
            except FileExistsError:
                return