from youtube_dl import YoutubeDL
# Sample 1: Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=ZBOSPTaWV3w']) # Remember to put your video in a list, eventhough one video is downloaded
