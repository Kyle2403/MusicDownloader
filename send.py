from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

# For using listdir()
import os
   
def send_to_Drive():
    print("Enter the origin directory from which you like to send your files (leave blank for mp3 folder)")
    path = str(input(">> ")) or './mp3'
    if not os.path.isdir(path):
        print("Origin path {} does not exist.".format(path))
        return
    if len(os.listdir(path)) == 0:
        print("There is nothing to send in the origin path, nothing sent.")
        return
    
    # Below code does the authentication
    gauth = GoogleAuth()
    # Creates local webserver and auto
    # handles authentication.
    gauth.LocalWebserverAuth()       
    drive = GoogleDrive(gauth)
    
    
    # iterating thought all the files/folder
    # of the desired directory
    for x in os.listdir(path):
        if "mp3" in x:
            f = drive.CreateFile({'title': x})
            f.SetContentFile(os.path.join(path, x))
            f.Upload()
            f = None
            file = path + "/" + x
            # delete file after uploading
            os.remove(file)
    print("All mp3 files are sent to GG Drive and removed from disk.")