# Overview
I usually download music as mp3 files to my phone, so I write this program to automatically download audios from Youtube and send it to my Google Drive so I can easily download them to my phone. It can search for videos as well when you run it using python main.py.
# Install necessarry modules
pip install -r requirements.txt 
# Get access to Youtube API 
* Go to Google Console API and create a new project or use an existing one
* Go to Library tab, search for YouTube Data API v3 and enable it
* Back to the console and access Credentials tab -> Create Credentials -> API key
* Copy the key and paste in "Replace_me" in search.py
# Get Google Drive OAuth client ID
* Go to Google Console API
* Go to Library tab, search for Google Drive API and enable it
* Back to the console and access Credentials tab -> Create Credentials -> OAuth client ID -> Fill in information like Application name (your choice).
* Download the credentials json file, name it client_secrets.json and save in the project directory.
# Add user
* Go to OAuth consent screen and add your email as an user.
# To run automatically (download from youtube -> send to GG Drive)
* Open in.txt file and paste in youtube video urls seperared by "|" between "download" and the first "mp3"(mp3 is the default folder where mp3 files are downloaded to, you can enter a different path to change it)
* Open a terminal/command prompt and enter sh auto.sh in.txt out.txt
* A browser will open and ask you to choose a GG Drive account to allow the application to access.
* Choose an account -> Continue -> Continue until the browser displays "The authentication flow has completed."
* You can close it now, check your GG Drive to see if the videos are loaded to it.
* The output created by the program during runtime can be found in out.txt. If something goes wrong you can check it for more information.
# To run and do things yourself
* python main.py