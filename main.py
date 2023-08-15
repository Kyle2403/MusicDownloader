import download
import search
import send

if __name__ == '__main__':
    videos = []
    while True:
        request = input("What do you want to do (search/download/send/quit)?\n>> ")
        if request.lower() == "quit": exit()
        elif request.lower() == "search":
            videos, channels, playlists = search.youtube_search()
            search.show(videos)
        elif request.lower() == "download":
            while True:
                if len(videos) != 0:
                    option = input("Do you want to provide url (1), choose one of the search results (2) or back (3)?\n>> ")
                    if option == "1": download.download("")
                    elif option == "2":
                        search.show(videos)
                        try: num = int(input("Enter the number of the video\n>> "))
                        except:
                            print("Number must be an integer.")
                            continue
                        try:
                            num -= 1
                            url = "https://www.youtube.com/watch?v=" + videos[num][1]
                        except IndexError: print("The video with this number does not exist.")
                        download.download(url)
                    elif option == "3": break
                    else: print("Unrecognized request.")
                else:
                    download.download("")
                    break
        elif request.lower() == "send": send.send_to_Drive()
        else: print("Unrecognized request.")