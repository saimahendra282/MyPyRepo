# main.py
# pip install pytube 
from pytube import YouTube
print("coding starts .........")
try:
    # Asking to input the  URL

    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)

    # Get the hd quality video
    yd = yt.streams.get_highest_resolution()
    
     yd.download()
    
    print("Download completed....")
    print("coding ending.........")
except Exception as e:
    print("An error occurred:", str(e))

    print("that's all")
